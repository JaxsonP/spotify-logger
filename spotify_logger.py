import os
import secrets
import time
import csv
import logging
import spotipy

import secrets



def main():

  # logging config
  #logging.basicConfig(filename='app.log', format='%(name)s - %(levelname)s - %(message)s')


  # authorization
  with open ("secrets.txt", "r") as f:
    os.environ["SPOTIPY_CLIENT_ID"] = f.readline().split("=")[1].strip()
    os.environ["SPOTIPY_CLIENT_SECRET"] = f.readline().split("=")[1].strip()
  os.environ["SPOTIPY_REDIRECT_URI"] = "http://127.0.0.1:9090"
  time.sleep(0.01)
  spotify = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(scope="user-read-playback-state"))
  print(f"Successfully connected as {spotify.me()['display_name']} [{spotify.me()['id']}]")

  current_item_id = ""

  while True:

    #time.sleep(3)
    print("Gathering playback data")
    playback = spotify.current_playback()
    #print(playback)

    # spotify not playing
    if playback == None:
      continue
    
    # spotify paused
    if not playback["is_playing"]:
      continue
    
    # song hasn't changed
    if current_item_id == playback["item"]["id"]:
      continue
    current_item_id = playback["item"]["id"]

    # writing new entry <<<<<<<
    new_entry = {}

    # basic track info
    new_entry["Timestamp"] = playback["timestamp"]
    new_entry["Item ID"] = playback["item"]["id"]
    new_entry["Item Name"] = playback["item"]["name"]
    new_entry["Item Type"] = playback["item"]["type"]

    # artist info
    """artists = []
    artist_uris = []
    for artist in playback["item"]["artists"]:
      artists.append(artist["name"])
      artist_uris.append(artist["uri"])
    new_entry["Artists"] = ",".join(artists)

    # genres
    genres = []
    artist_info = spotify.artists(",".join(artist_uris[:]))
    print(artist_info)
    for artist in artist_info["artists"]:
      print(artist["genres"])"""

    # further track info
    new_entry["Length"] = playback["item"]["duration_ms"]
    new_entry["Explicit"] = playback["item"]["explicit"]
    new_entry["Popularity"] = playback["item"]["popularity"]


    
    # writing to csv output file
    with open("song_list.csv", "w", newline='') as f:
      writer = csv.DictWriter(f, fieldnames=new_entry.keys())

      writer.writeheader()
      writer.writerow(new_entry)
    
    break

  return True



if __name__ == "__main__":
  main()





"""
{
  'device': {
    'id': '92d00828495829e5f16156ac905c3c036e392dcb',
    'is_active': True,
    'is_private_session': False,
    'is_restricted': False,
    'name': 'iPhone',
    'type': 'Smartphone',
    'volume_percent': 100
  },
  'shuffle_state': True,
  'repeat_state': 'off',
  'timestamp': 1665756907419,
  'context': {
    'external_urls': {
      'spotify': 'https://open.spotify.com/playlist/0AsFjsOazAIa19F1k1tSar'
    },
    'href': 'https://api.spotify.com/v1/playlists/0AsFjsOazAIa19F1k1tSar',
    'type': 'playlist',
    'uri': 'spotify:playlist:0AsFjsOazAIa19F1k1tSar'
  },
  'progress_ms': 34620,
  'item': {
    'album': {
      'album_type': 'album',
      'artists': [
        {
          'external_urls': {
            'spotify': 'https://open.spotify.com/artist/4hR6Bm9YYtktXzjmKhb1Cn'
          },
          'href': 'https://api.spotify.com/v1/artists/4hR6Bm9YYtktXzjmKhb1Cn',
          'id': '4hR6Bm9YYtktXzjmKhb1Cn',
          'name': 'ericdoa',
          'type': 'artist',
          'uri': 'spotify:artist:4hR6Bm9YYtktXzjmKhb1Cn'
        }
      ],
      
      'external_urls': {
        'spotify': 'https://open.spotify.com/album/72K9c2D3M69XFFVKiIZuUU'
      },
      'href': 'https://api.spotify.com/v1/albums/72K9c2D3M69XFFVKiIZuUU',
      'id': '72K9c2D3M69XFFVKiIZuUU',
      'images': [
        {
          'height': 640,
          'url': 'https://i.scdn.co/image/ab67616d0000b27340c036752aa4a53b091de6d1',
          'width': 640
        },
        {
          'height': 300,
          'url': 'https://i.scdn.co/image/ab67616d00001e0240c036752aa4a53b091de6d1',
          'width': 300
        },
        {
          'height': 64,
          'url': 'https://i.scdn.co/image/ab67616d0000485140c036752aa4a53b091de6d1',
          'width': 64
        }
      ],
      'name': 'COA',
      'release_date': '2020-11-06',
      'release_date_precision': 'day',
      'total_tracks': 11,
      'type': 'album',
      'uri': 'spotify:album:72K9c2D3M69XFFVKiIZuUU'
    },
    'artists': [
      {
        'external_urls': {
          'spotify': 'https://open.spotify.com/artist/4hR6Bm9YYtktXzjmKhb1Cn'
        },
        'href': 'https://api.spotify.com/v1/artists/4hR6Bm9YYtktXzjmKhb1Cn',
        'id': '4hR6Bm9YYtktXzjmKhb1Cn',
        'name': 'ericdoa',
        'type': 'artist',
        'uri': 'spotify:artist:4hR6Bm9YYtktXzjmKhb1Cn'
      }
    ],

    'disc_number': 1,
    'duration_ms': 126563,
    'explicit': True,
    'external_ids': {
      'isrc': 'QZMER2028979'
    },
    'external_urls': {
      'spotify': 'https://open.spotify.com/track/36TaRW67lRRJaMC9hSNy25'
    },
    'href': 'https://api.spotify.com/v1/tracks/36TaRW67lRRJaMC9hSNy25',
    'id': '36TaRW67lRRJaMC9hSNy25',
    'is_local': False,
    'name': 'self sabotage',
    'popularity': 43,
    'preview_url': 'https://p.scdn.co/mp3-preview/de85e1d7ffc8e31d16abcec0c1842cd858210d7e?cid=fe463969182142bdaac06fc2b96227c9',
    'track_number': 4,
    'type': 'track',
    'uri': 'spotify:track:36TaRW67lRRJaMC9hSNy25'
  },
  'currently_playing_type': 'track',
  'actions': {
    'disallows': {
      'resuming': True
    }
  },
  'is_playing': True
}
"""