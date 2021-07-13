# Spotify Playlist Curator Fetcher
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A small app to search for keywords and get a list of possible curators you can submit your music to.

## Requirements
- Python 3 and Pip
- PyQt 5
- Spotipy
- Spotify API secret and identity

## Install and Run

You have to get a Spotify Identity and Secret first and put it manually into main.py before using this program.
```bash
git clone https://github.com/MLK97/Spotify-Playlist-Curator-Fetcher.git
cd Spotify-Playlist-Curator-Fetcher
python spcf_main.py
```

## What and why
To get your music out there and have people listening to it no longer depends on radio stations in this decade.
However the amount of monthly listeners still varies highly from artist to artist.
An essential factor to the people you reach with your music are playlists.
Getting to know playlist curators is hard, so for me it is always great to get a website or email-adress, where
I can contact curators and ask them to consider my music.
I realised that some playlist creators put either a website link or email adress.
This app will help you with getting to know curators, thanks to the Spotify API:

- It searches playlists that contain keywords
- It looks into the description of those playlists
- If the playlist description contains email-adress or website shows the playlist

## Limitations
Currently this app only searches for spotify playlist.
If there is enough interest, I'll add support for other platforms after considering the possiblity of it.

Spotify also limits playlist searches to 50 playlists at a time, this way you will only get a fraction
of playlists if you search for big keywords, like: "Music", "Pop".
For the most and best results search for more specific keywords.

## What this is not
This app is not meant to be an automatic message bot or an email-list generator.
I still encourage everybody to write personalized messages, if you find a playlist you like.
I believe, that an honest and thoughtfull email, will always get you further, than some copy-pasted email,
that was sent to 50 other people.
This is why I didn't implement a messaging function, nor do I intend on doing so in the future.

## Planned Features
If you have an idea to make this app better or want an additional feature, don't hesitate to raise an [Issue](https://github.com/MLK97/Spotify-Playlist-Curator-Fetcher/issues)

Planned Features currently involve:
- Checking already contacted curators

## Bugs
If you find Bugs or experience probelems, please raise an [Issue](https://github.com/MLK97/Spotify-Playlist-Curator-Fetcher/issues)
