
class MusicLibrary():
    
    def __init__(self):
        self.track_list = []

    def add_track(self, track):
        self.track_list.append(track)

    def search(self, keyword):
        search_list = []
        for track in self.track_list:
            try:
                if track.matches(keyword):
                    search_list.append(track)
            except Exception:
                raise Exception("something went wrong")
        return search_list