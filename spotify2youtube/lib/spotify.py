import os
import re
from typing import Any
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Spotify:
    """
    Spotify API class
    """

    def __init__(
        self,
        client_id: str = os.environ["SPOTIFY_CLIENT_ID"],
        client_secret: str = os.environ["SPOTIFY_CLIENT_SECRET"],
    ):
        """
        initialization of spotify class
        """
        self.scope = "user-library-read"
        self.spotify_redirect_uri = "http://localhost"
        self.spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id,
                client_secret,
                redirect_uri=self.spotify_redirect_uri,
                scope=self.scope,
            )
        )
        self.playlist_info = {}

    def print_artist_url(self, artist: str = "") -> None:
        """
        Gets teh url to a given artist

        Args:
            artist (List, Strings): [A list og artist names]. Defaults to None.
        """
        if artist:
            name = artist
        else:
            name = "Radiohead"

        results: Any = self.spotify.search(q="artist:" + name, type="artist")  # type: ignore
        items = results["artists"]["items"]
        if len(items) > 0:
            artist_dict: dict[str, dict[Any, Any]] = items[0]
            print(artist_dict["name"], artist_dict["images"][0]["url"])

    def get_playlists(self):
        user: Any = self.spotify.current_user()  # type: ignore
        print(user)
        playlists: Any = self.spotify.current_user_playlists()  # type: ignore
        for playlist in playlists["items"]:
            name = playlist["name"]
            print(name)
            if "Heilung" in name:
                playlist_uri = playlist["tracks"]["href"]
                print(playlist_uri)
                self.playlist_info[f"{name}"] = self.get_tracks(playlist_uri)  # type: ignore

    def get_tracks(self, uri: str) -> list[dict[str, str]]:
        playlist_dict = {}
        with open(".cache", "r") as f:
            cache = f.readline()

        print(cache)
        m = re.search(
            '(?<=(access_token":\\s"))([a-z]|[A-Z]|[0-9]).*(?=(",\\s"token_type))',
            cache,
        )
        bearer_match: str = m.group()  # type: ignore
        url = uri
        payload = {}
        headers = {"Authorization": f"Bearer {bearer_match}"}

        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()
        spotify_response_dict = response.json()
        track_list: list[dict[str, str]] = []
        for track in spotify_response_dict["items"]:
            playlist_dict = {
                "name": track["track"]["name"],
                "album": track["track"]["album"]["name"],
                "artist": track["track"]["artists"][0]["name"],
            }
            track_list.append(playlist_dict)

        return track_list
