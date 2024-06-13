import spotipy, dotenv, os, traceback
from spotipy.oauth2 import SpotifyOAuth

# Import environment variables
# These are prerequisites in apps calling this module
def import_vars():
    dotenv.load_dotenv()
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URL")
    return client_id, client_secret, redirect_uri

class PyFyLib():
    def __init__(self):
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri, scope='streaming'))

    def get_tracks(self, artist: str = '', track: str = ''):
        try:
            if artist == '':
                raise Exception(f"No artist: {artist} was passed to the function")
            if track == '':
                raise Exception(f"No track: {track} name was passed to the function")

            track_id = self.spotify.search(q='artist:' + artist + ' track:' + track, type='track', limit=10)
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

    def get_user_playlists(self):
        try:
            playlists = self.spotify.current_user_playlists()

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

    def play_song(self, track):
        try:
            self.spotify.start_playback(uris=track)
        except:
            return traceback.format_exc()

    def play_playlist(self, playlist): 
        try:
            self.spotify.start_playback(context_uri=playlist)
        except:
            return traceback.format_exc()

    def set_shuffle(self, state):
        try:
            self.spotify.shuffle(state)
        except:
            return traceback.format_exc()

    def pause(self):
        try:
            self.spotify.pause_playback()
        except:
            return traceback.format_exc()

    def next(self): 
        try:
            self.spotify.next_track()
        except:
            return traceback.format_exc()

    def previous(self): 
        try:
            self.spotify.previous_track() 
        except:
            return traceback.format_exc()

    def add_to_queue(self, track):
        try:
            self.spotify.add_to_queue(uri=track)
        except:
            return traceback.format_exc()

if __name__ == "__main__":
    print("calling PyFyLib")
    
    # client_id, client_secret, redirect_uri = import_vars()
    # playlist = get_user_playlists()
    # pyfylib = PyFyLib()

    # PyTuiFy input
    # tracks = pyfylib.get_tracks('radiohead', 'reckoner')

    # pyfylib.pause()
    # pyfylib.next()
    # pyfylib.previous()
    # pyfylib.play_song(tracks[0]['uri']) 
    # pyfylib.add_to_queue(tracks[0]['uri'][0])
    # pyfylib.play_playlist(playlist[1]['uri'])


