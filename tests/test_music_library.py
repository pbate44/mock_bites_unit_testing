from unittest.mock import Mock
from lib.music_library import *
import pytest

# Given a new MusicLibrary, 
# when a track is added, 
# then it should store that track in its internal list.

def test_add_track_and_call_list():
    music = MusicLibrary()
    fake_track_1 = Mock()
    music.add_track(fake_track_1)
    assert fake_track_1 in music.track_list


# Given a MusicLibrary containing multiple tracks, 
# when search() is called with a keyword, 
# then it should call each track’s matches() method exactly once.

def test_search_triggers_match_for_each_track():
    music = MusicLibrary()
    fake_track_1 = Mock()
    music.add_track(fake_track_1)
    fake_track_2 = Mock()
    music.add_track(fake_track_2)
    fake_track_3 = Mock()
    music.add_track(fake_track_3)
    fake_track_4 = Mock()
    music.add_track(fake_track_4)
    music.search("word")
    fake_track_1.matches.assert_called_once_with("word")
    fake_track_2.matches.assert_called_once_with("word")
    fake_track_3.matches.assert_called_once_with("word")
    fake_track_4.matches.assert_called_once_with("word")


# Given a MusicLibrary with several tracks, 
# when only one track’s matches() returns True, 
# then search() should return a list containing only that track.

def test_search_returns_only_matching_track():
    music = MusicLibrary()
    fake_track_1 = Mock()
    music.add_track(fake_track_1)
    fake_track_1.matches.return_value = True
    fake_track_2 = Mock()
    music.add_track(fake_track_2)
    fake_track_2.matches.return_value = False
    result = music.search("word")
    assert result == [fake_track_1]


# Given a MusicLibrary where no tracks match the keyword, 
# when search() is called, 
# then it should return an empty list.

def test_search_returns_no_matching_track():
    music = MusicLibrary()
    fake_track_1 = Mock()
    music.add_track(fake_track_1)
    fake_track_1.matches.return_value = False
    fake_track_2 = Mock()
    music.add_track(fake_track_2)
    fake_track_2.matches.return_value = False
    result = music.search("word")
    assert result == []


# Given a mock track that raises an exception when matches() is called, 
# when search() is executed, 
# then the exception should propagate or be handled appropriately.

def test_exception_is_handled_properly():
    music = MusicLibrary()
    fake_track_1 = Mock()
    music.add_track(fake_track_1)
    fake_track_1.matches.return_value = False
    fake_track_2 = Mock()
    music.add_track(fake_track_2)
    fake_track_2.matches.side_effect = Exception("something went wrong")
    with pytest.raises(Exception) as e:
        music.search("word")
    assert str(e.value) == "something went wrong"


# Given an empty MusicLibrary, 
# when search() is called, 
# then it should return an empty list without calling any mocks.

    def test_empty_library():
        music = MusicLibrary()
        result = music.search("word")
        assert result == []



