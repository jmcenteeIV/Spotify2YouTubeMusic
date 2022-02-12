class Provider(object):
    def __init__(self):
        pass

    def get_playlists(self)->None:
        raise NotImplementedError

    def get_tracks(self)->None:
        raise NotImplementedError

    def set_playlist(self)->None:
        raise NotImplementedError

    def set_tracks(self)->None:
        raise NotImplementedError