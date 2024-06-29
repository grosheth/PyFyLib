import dotenv, os

def import_secrets():
    dotenv.load_dotenv()
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URL")
    return client_id, client_secret, redirect_uri
