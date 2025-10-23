from lib.track import *
from unittest.mock import Mock


# Given a Track initialized with a title and artist, 
# when inspected, 
# then its internal attributes should match the provided arguments.

def test_track_attributes():
    track = Track()
    track.artist = "artist1"
    track.name = "track1"
    assert f"{track.name} by {track.artist}" == "track1 by artist1"


# Given a Track with specific title and artist values, 
# when matches() is called with a keyword matching the title, 
# then it should return True.

def test_matches_returns_true():
    track = Track()
    track.artist = "artist1"
    track.name = "track1"
    result = track.matches("art")
    assert result == True

# Given a Track with specific title and artist values, 
# when matches() is called with a keyword matching the artist, 
# then it should return True.

def test_matches_returns_true_for_song_name():
    track = Track()
    track.artist = "artist1"
    track.name = "track1"
    result = track.matches("k1")
    assert result == True


# Given a Track where the keyword matches neither the title nor artist, 
# when matches() is called, 
# then it should return False.

def test_matches_returns_false():
    track = Track()
    track.artist = "artist1"
    track.name = "track1"
    result = track.matches("abcd")
    assert result == False


# Given a Track with mixed-case title and artist values, 
# when matches() is called with a differently cased keyword, 
# then it should perform a case-insensitive comparison and return True.

def test_matches_works_for_mixed_case():
    track = Track()
    track.artist = "artist1"
    track.name = "track1"
    result = track.matches("ACK")
    assert result == True


def test_empty_string_search_is_false():
    track = Track()
    track.artist = "artist1"
    track.name = "track1"
    result = track.matches("")
    assert result == False