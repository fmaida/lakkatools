import pytest
from lib.playlists import Entry, Playlist


def test_single_entry():
    e = Entry()
    e.path = "/path/to/rom/test.rom"
    e.title = "My awesome game"
    assert "My awesome game" in str(e)

def test_simple_playlist():
    p = Playlist()
    p.