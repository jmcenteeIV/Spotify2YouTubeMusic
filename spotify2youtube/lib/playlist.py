from typing import Any
from . import spotify, youtube_music


class Playlist(object):
    """
    class to hold playlist items and interact with the streaming platforms
    """

    # Singleton instantiation and getting, code from:
    # https://python-patterns.guide/gang-of-four/singleton/
    _instance = None

    def __init__(self) -> None:
        raise RuntimeError("Class has already been instantiated")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    # End Singleton code
    
    
    def get_playlists(self, provider: str):
        self.playlists: dict[str, list[dict[str, str]]] = {}
        self.playlists = self.source_provider.get_playlists()

    def set_source_provider(self, provider: str, username: str, password: str) -> None:
        match provider.lower():
            case "spotify":
                self.source_provider: spotify.Spotify = spotify.Spotify(username, password)
            case _:
                raise RuntimeError("Streaming provider not recognized")

    def set_target_provider(self, provider: str, username: str, password: str) -> None:
        match provider.lower():
            case "youtube_music":
                self.target_provider: youtube_music.YoutubeMusic = youtube_music.YoutubeMusic(username, password)
            case _:
                raise RuntimeError("Streaming provider not recognized")
    

