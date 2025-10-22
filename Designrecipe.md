
# File: lib/music_library.py

class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        pass

    def add(self, track):
        # track is an instance of Track
        # Track gets added to the library
        # Returns nothing
        pass

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        pass


# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        # title and artist are both strings
        pass

    def matches(self, keyword):
        # keyword is a string
        # Returns true if the keyword matches either the title or artist
        pass




unit tests examples without relying on other classes

MUSIC LIBRARY


Given a new MusicLibrary, 
when a track is added, 
then it should store that track in its internal list.


Given a MusicLibrary containing multiple tracks, 
when search() is called with a keyword, 
then it should call each track’s matches() method exactly once.


Given a MusicLibrary with several tracks, 
when only one track’s matches() returns True, 
then search() should return a list containing only that track.


Given a MusicLibrary where no tracks match the keyword, 
when search() is called, 
then it should return an empty list.


Given a mock track that raises an exception when matches() is called, 
when search() is executed, 
then the exception should propagate or be handled appropriately.


Given an empty MusicLibrary, 
when search() is called, 
then it should return an empty list without calling any mocks.


TRACK

Given a Track initialized with a title and artist, 
when inspected, 
then its internal attributes should match the provided arguments.


Given a Track with specific title and artist values, 
when matches() is called with a keyword matching the title, 
then it should return True.


Given a Track with specific title and artist values, 
when matches() is called with a keyword matching the artist, 
then it should return True.


Given a Track where the keyword matches neither the title nor artist, 
when matches() is called, 
then it should return False.


Given a Track with mixed-case title and artist values, 
when matches() is called with a differently cased keyword, 
then it should perform a case-insensitive comparison and return True.


Given a Track, 
when matches() is called with an empty string, 
then it should return False (no match).