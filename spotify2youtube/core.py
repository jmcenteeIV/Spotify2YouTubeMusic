from lib import spotify, youtube_music

"""
Entry file for spotify2youtube
"""


def main():
    """
    Entry method for spotify2youtube
    """
    spotify_instance = spotify.Spotify()
    spotify_instance.get_playlists()
