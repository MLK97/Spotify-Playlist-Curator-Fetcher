#!/usr/bin/env python

"""Spotify Search
Calls the Spotify API and searches for Playlists containing
the strings that are handed over to the search method
"""

import spotipy
import re
import sys
from spotipy.oauth2 import SpotifyClientCredentials

__author__ = "Maximilian Konrad"
__copyright__ = "Copyright 2020, SPCF-Project"
__credits__ = ["Maximilian Konrad", "Rainer Endres"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Maximilian Konrad"
__email__ = "fysikbeats@hotmail.com"
__status__ = "Development"


def search(search):
    entries = list()

    # Looking for Keywords
    identiy = 'None'
    secret = 'None'

    # Accessing Spotify-API
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=identiy,
        client_secret=secret))

    # Find and filter Results
    for element in search:
        result = sp.search(element, limit=50, type='playlist')
        for n in range(50):
            try:
                playlist_desc = result['playlists']['items'][n]['description']
                playlist_title = result['playlists']['items'][n]['name']
                playlist_email = 'none'
                playlist_url = 'none'
                if '@' in playlist_desc:
                    playlist_email = re.search(r'[\w\.-]+@[\w\.-]+',
                                               playlist_desc)
                    if playlist_email is None:
                        playlist_email = 'none'
                if 'http' in playlist_desc or \
                   'submit' in playlist_desc or \
                   'curated' in playlist_desc and not playlist_desc:
                    playlist_url = re.findall(u"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
                                              playlist_desc)
                    for item in playlist_url:
                        if "spotify" in item:
                            playlist_url.remove(item)
                    if playlist_url is None or len(playlist_url) == 0:
                        playlist_url = 'none'
                entry = {
                    "title": playlist_title,
                    "description": playlist_desc,
                    "email": playlist_email,
                    "url": playlist_url
                }
                if playlist_url != "none" or playlist_email != "none":
                    entries.append(entry)
            except (IndexError, UnicodeEncodeError):
                print("Error on line {}".format(sys.exc_info()))
                return "Sorry, I couldn't find any playlists that match your keywords"
                break
    return entries
