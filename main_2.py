import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

search_str = 'Big Dick'
#search_str = ['Piano', 'Keyboard', 'Grand Piano', 'Classic']

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='c14bd3df3ade429b82f9f657fef9cf22',
                                                                              client_secret='c1d6bb186d9d4b68a0d43e7d960bbe98'))

result = sp.search(search_str, limit=50, type='playlist')

for n in range(50):
    final_desc = result['playlists']['items'][n]['description']
    final_title = result['playlists']['items'][n]['name']
    print("Titel:", final_title, 'Desc:', final_desc, '\n')
