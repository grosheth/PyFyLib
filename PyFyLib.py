import spotipy, dotenv, os
import logging
from spotipy.oauth2 import SpotifyClientCredentials

# Import environment variables
dotenv.load_dotenv()

def spotify_login():
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(os.getenv("SPOTIPY_CLIENT_ID"), os.getenv("SPOTIPY_CLIENT_SECRET")))
    return spotify

def search_track(artist: str, track: str):
    
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    try:
        spotify = spotify_login()

        track_id = spotify.search(q='artist:' + artist + ' track:' + track, type='track')
        tracks_info = {} 
        for index, content in enumerate(track_id['tracks']['items']): 
            track_info = { index: 
                        {'artist': content['artists'][0]['name'],
                        'track': content['name'],
                        'id': content['id']
                        }}
            tracks_info.update(track_info)

        print(tracks_info)
        return tracks_info
    except:
        print("There was an error trying to obtain the track", "The values sent are artist:", artist, "track:", track)

if __name__ == "__main__":
    spotify_login()
    tracks = search_track('Imagine Dragons', 'radioactive')
    # for track in tracks:
    #     print(f"Name: {track['name']}, Artist: {track['artist']}, Album: {track['album']}, URI: {track['uri']}")

