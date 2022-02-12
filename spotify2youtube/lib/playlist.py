from typing import Any


class Playlist(object):
    """
    class to hold playlist items and interact with the streaming platforms
    """

    # Singleton instantiation and getting, code from:
    # https://python-patterns.guide/gang-of-four/singleton/
    _instance = None

    def __init__(self) -> None:
        raise RuntimeError("Game has already been instantiated")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    # End Singleton code

    def get_playlists(self, provider: str) -> list[dict[str, Any]]:

        playlist: list[dict[str, Any]] = []
        return playlist
