import spotipy
import re
from spotipy.oauth2 import SpotifyClientCredentials

search_list = ['Piano', 'Keyboard', 'Grand Piano', 'Sleep', 'Ambient']


def search(search):
    # Looking for Keywords
    identiy = 'c14bd3df3ade429b82f9f657fef9cf22'
    secret = 'c1d6bb186d9d4b68a0d43e7d960bbe98'

    # Accessing Spotify-API
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=identiy,
        client_secret=secret))

    # Find and filter Results
    for m in range(len(search)):
        result = sp.search(search[m], limit=50, type='playlist')
        for n in range(50):
            playlist_desc = result['playlists']['items'][n]['description']
            playlist_title = result['playlists']['items'][n]['name']
            if '@' in playlist_desc:
                email = re.search(r'[\w\.-]+@[\w\.-]+', playlist_desc)
                print("Titel: ", playlist_title,
                      "Email: ", email, "\n",
                      "Desription: ", playlist_desc[0:250], "\n")
                if 'http' in playlist_desc or \
                   'submit' in playlist_desc or \
                   'curated' in playlist_desc and not playlist_desc:
                    url = re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
                                     playlist_desc)
                    print("Titel: ", playlist_title,
                          "Url: ", url, "\n",
                          "Desription: ", playlist_desc[0:250], "\n")


search(search_list)
