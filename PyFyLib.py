import spotipy, dotenv, os, traceback
from spotipy.oauth2 import SpotifyClientCredentials

# Import environment variables
def import_vars(): 
    dotenv.load_dotenv()
    id = os.getenv("SPOTIPY_CLIENT_ID")
    secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    return id, secret

def spotify_login(id, secret):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(id, secret))
    return spotify

def get_tracks(artist: str = '', track: str = ''): 
    if artist == '':
        raise Exception(f"No artist: {artist} was passed to the function")
    if track == '':
        raise Exception(f"No track: {track} name was passed to the function")

    try:
        spotify = spotify_login(id, secret)
        track_id = spotify.search(q='artist:' + artist + ' track:' + track, type='track', limit=10)
        tracks_info = {} 
        for index, content in enumerate(track_id['tracks']['items']): 
            track_info = { index: 
                        {'artist': content['artists'][0]['name'],
                        'track': content['name'],
                        'id': content['id'],
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

if __name__ == "__main__":
    id, secret = import_vars()
    tracks = get_tracks('hugo', 'coma')
    print(tracks)

