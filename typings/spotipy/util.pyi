"""
This type stub file was generated by pyright.
"""

""" Shows a user's playlists (need to be authenticated via oauth) """
__all__ = ["CLIENT_CREDS_ENV_VARS", "prompt_for_user_token"]
LOGGER = ...
CLIENT_CREDS_ENV_VARS = ...
def prompt_for_user_token(username=..., scope=..., client_id=..., client_secret=..., redirect_uri=..., cache_path=..., oauth_manager=..., show_dialog=...): # -> None:
    ...

def get_host_port(netloc): # -> tuple[Unknown, int | None]:
    ...

def normalize_scope(scope): # -> str | None:
    ...
