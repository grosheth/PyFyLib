import spotipy, dotenv, os, traceback
from spotipy.oauth2 import SpotifyOAuth

# Import environment variables
def import_vars():
    dotenv.load_dotenv()
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URL")
    return client_id, client_secret, redirect_uri

def spotify_login():
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri, scope='streaming'))
    return spotify

def get_tracks(artist: str = '', track: str = ''):
    try:
        if artist == '':
            raise Exception(f"No artist: {artist} was passed to the function")
        if track == '':
            raise Exception(f"No track: {track} name was passed to the function")

        spotify = spotify_login()
        track_id = spotify.search(q='artist:' + artist + ' track:' + track, type='track', limit=10)
        tracks_info = {} 
        for index, content in enumerate(track_id['tracks']['items']): 
            track_info = { index: 
                        {'artist': content['artists'][0]['name'],
                        'track': content['name'],
                        'id': content['id'],
                        'uri': [content['uri']],
                        'audio': content['external_urls']['spotify'],
                        'image': content['album']['images'][0]['url'],
                        'preview': content['preview_url']
                        }}
            tracks_info.update(track_info)

        if tracks_info == {}:
            raise Exception(f"Nothing was found with the following parameters: artist: {artist}  track: {track}")

        return tracks_info
    except Exception:
        return traceback.format_exc()

def get_user_playlists():
    try:
        spotify = spotify_login()
        playlists = spotify.current_user_playlists()
        print(playlists['items'])
        for i, playlist in enumerate(playlists['items']):
            print(playlist['name'])
    except Exception:
        return traceback.format_exc()

def play_track(track):
    spotify = spotify_login()
    spotify.start_playback(uris=track)

if __name__ == "__main__":
    client_id, client_secret, redirect_uri = import_vars()

    get_user_playlists()
    # tracks = get_tracks('hugo tsr', 'coma artificiel')
    # play_track(tracks[0]['uri'])

