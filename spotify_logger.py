import os
import requests


import spotipy

import secrets



def main():

  os.environ["SPOTIPY_CLIENT_ID"] = secrets.SPOTIFY_CLIENT_ID
  os.environ["SPOTIPY_CLIENT_SECRET"] = secrets.SPOTIFY_CLIENT_SECRET
  os.environ["SPOTIPY_REDIRECT_URI"] = "http://127.0.0.1:9090"
  spotify = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(scope="user-read-playback-state"))
  print(f"Successfully connected as {spotify.me()['display_name']} [{spotify.me()['id']}]")
  

  while True:

    new_item = {}

    print("Waiting for playback data...")
    try:
      playback = spotify.current_playback()
      #print(playback)
    except Exception as e:
      print("!!! error while polling for playback data:")
      print(e)
      continue

    if playback["is_playing"] == False:
      pass#continue

    new_item["timestamp"] = playback["timestamp"]
    new_item["id"] = playback["item"]['id']
    new_item["name"] = playback["item"]['name']

    artists = playback["item"]["artists"]
    new_item["artists"] = ",".join([artist["name"] for artist in artists])

    genres = []
    for artist in artists:
      print("\n", artist["name"])
      artist_info = spotify.artist(artist["id"])
      genres += artist_info['genres']
      print(artist_info)
    
    new_item["genres"] = ",".join(genres)

    song_info = spotify.track(playback["item"]["id"])
    print("\n", song_info)
    new_item["popularity"] = playback['item']["popularity"]



    print("\n\n\n")
    [print(f"{key}: {new_item[key]}") for key in new_item.keys()]
    break

  return True



if __name__ == "__main__":
  main()





"""
{
  'device': {
    'id': '30c7c4be6ea00b3309f7939ce7ed0607f747aeb0',
    'is_active': True,
    'is_private_session': False,
    'is_restricted': False,
    'name': 'DESKTOP-R4KO',
    'type': 'Computer',
    'volume_percent': 49
  },
  'shuffle_state': True,
  'repeat_state': 'off',
  'timestamp': 1660598350711,
  'context': {
    'external_urls': {
      'spotify': 'https://open.spotify.com/artist/4kqFrZkeqDfOIEqTWqbOOV'
    },
    'href': 'https://api.spotify.com/v1/artists/4kqFrZkeqDfOIEqTWqbOOV',
    'type': 'artist',
    'uri': 'spotify:artist:4kqFrZkeqDfOIEqTWqbOOV'
  },
  'progress_ms': 25545,
  'item': {
    'album': {
      'album_type': 'album',
      'artists': [
        {
          'external_urls': {
            'spotify': 'https://open.spotify.com/artist/4kqFrZkeqDfOIEqTWqbOOV'
          },
          'href': 'https://api.spotify.com/v1/artists/4kqFrZkeqDfOIEqTWqbOOV',
          'id': '4kqFrZkeqDfOIEqTWqbOOV',
          'name': 'brakence',
          'type': 'artist',
          'uri': 'spotify:artist:4kqFrZkeqDfOIEqTWqbOOV'
        }
      ],
      'available_markets': [
       
      ],
      'external_urls': {
        'spotify': 'https://open.spotify.com/album/0BAmcZfsraNVyG6rj782Og'
      },
      'href': 'https://api.spotify.com/v1/albums/0BAmcZfsraNVyG6rj782Og',
      'id': '0BAmcZfsraNVyG6rj782Og',
      'images': [
        {
          'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b273eb88e3c32c3bb61e318695b3',
          'width': 640
        },
        {
          'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e02eb88e3c32c3bb61e318695b3',
          'width': 300
        },
        {
          'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d00004851eb88e3c32c3bb61e318695b3',
          'width': 64
        }
      ],
      'name': 'punk2',
      'release_date': '2020-07-01',
      'release_date_precision': 'day',
      'total_tracks': 11,
      'type': 'album',
      'uri': 'spotify:album:0BAmcZfsraNVyG6rj782Og'
    },
    'artists': [
      {
        'external_urls': {
          'spotify': 'https://open.spotify.com/artist/4kqFrZkeqDfOIEqTWqbOOV'
        },
        'href': 'https://api.spotify.com/v1/artists/4kqFrZkeqDfOIEqTWqbOOV',
        'id': '4kqFrZkeqDfOIEqTWqbOOV',
        'name': 'brakence',
        'type': 'artist',
        'uri': 'spotify:artist:4kqFrZkeqDfOIEqTWqbOOV'
      }
    ],
    'available_markets': [
      
    ],
    'disc_number': 1,
    'duration_ms': 137751,
    'explicit': True,
    'external_ids': {
      'isrc': 'USSM12003809'
    },
    'external_urls': {
      'spotify': 'https://open.spotify.com/track/1XnnLXcvFd21B25H4IHEIY'
    },
    'href': 'https://api.spotify.com/v1/tracks/1XnnLXcvFd21B25H4IHEIY',
    'id': '1XnnLXcvFd21B25H4IHEIY',
    'is_local': False,
    'name': 'fwb',
    'popularity': 54,
    'preview_url': 'https://p.scdn.co/mp3-preview/e399070abec3e104a3bd5e410f9d9560627594d3?cid=fe463969182142bdaac06fc2b96227c9',
    'track_number': 3,
    'type': 'track',
    'uri': 'spotify:track:1XnnLXcvFd21B25H4IHEIY'
  },
  'currently_playing_type': 'track',
  'actions': {
    'disallows': {
      'resuming': True,
      'skipping_prev': True
    }
  },
  'is_playing': True
}
"""