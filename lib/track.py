
class Track:

    def __init__(self):
        self.artist = ""
        self.name = ""

    def matches(self, keyword):
        lower_key = keyword.lower()
        lower_track = self.name.lower()
        lower_artist = self.artist.lower()
        if lower_key.strip():
            if lower_key in lower_artist or lower_key in lower_track:
                return True
        return False
    
