import spotipy, dotenv, os
from spotipy.oauth2 import SpotifyClientCredentials

# Import environment variables
dotenv.load_dotenv()

def spotify_login():
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(os.getenv("SPOTIPY_CLIENT_ID"), os.getenv("SPOTIPY_CLIENT_SECRET")))
    return spotify

def get_tracks(artist: str, track: str): 
    if artist == '' or track == '':
        error = f"Two parameter need to be passed: 1.artist: {artist}  2.track:, {track}"
        return error
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

        if tracks_info == {}:
            error = f"Nothing was found with the following parameters: artist: {artist}  track: {track}"
            return error
        return tracks_info
    except:
        error = "There was an error trying to obtain the track resulting in a crash in spotipy" 
        return error

if __name__ == "__main__":
    spotify_login()
    tracks = get_tracks('imagine', 'radio')
    print(tracks)
    # for track in tracks:
    #     print(f"Name: {track['name']}, Artist: {track['artist']}, Album: {track['album']}, URI: {track['uri']}")

