import os


import spotipy

import secrets



def main():

  os.environ["SPOTIPY_CLIENT_ID"] = secrets.SPOTIFY_CLIENT_ID
  os.environ["SPOTIPY_CLIENT_SECRET"] = secrets.SPOTIFY_CLIENT_SECRET
  os.environ["SPOTIPY_REDIRECT_URI"] = "http://127.0.0.1:9090"
  spotify = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(scope="user-read-playback-state"))
  print(f"Successfully connected as {spotify.me()['display_name']} [{spotify.me()['id']}]")
  

  return 1



if __name__ == "__main__":
  main()