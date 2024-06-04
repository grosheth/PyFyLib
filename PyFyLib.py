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

        playlists_info = {}
        for index, playlist in enumerate(playlists['items']):
            playlist_info = { index: 
                        {'name': playlist['name'],
                        'id': playlist['id'],
                        'uri': playlist['uri'],
                        'audio': playlist['external_urls']['spotify'],
                        'image': playlist['images'][0]['url'],
                        }}
            playlists_info.update(playlist_info)

        return playlists_info
    except Exception:
        return traceback.format_exc()

def play_song(track):
    try:
        spotify = spotify_login()
        spotify.start_playback(uris=track)
    except:
        return traceback.format_exc()

def play_playlist(playlist): 
    try:
        spotify = spotify_login()
        spotify.start_playback(context_uri=playlist)
    except:
        return traceback.format_exc()

def set_shuffle(state):
    try:
        spotify = spotify_login()
        spotify.shuffle(state)
    except:
        return traceback.format_exc()

def pause():
    try:
        spotify = spotify_login()
        spotify.pause_playback() 
    except:
        return traceback.format_exc()

def next(): 
    try:
        spotify = spotify_login()
        spotify.next_track() 
    except:
        return traceback.format_exc()

# Can be used to show current song image etc..
def get_current_song():
    try:
        spotify = spotify_login()
        spotify.current_playback() 
    except:
        return traceback.format_exc()

if __name__ == "__main__":
    client_id, client_secret, redirect_uri = import_vars()

    playlist = get_user_playlists()

    # tracks = get_tracks('hugo tsr', 'coma artificiel')
    # play(tracks[1]['uri'])
    # play_playlist(playlist[1]['uri'])
    set_shuffle(True)

