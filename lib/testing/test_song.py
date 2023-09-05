# test_song.py
import pytest
from song import Song
from config import CURSOR

def test_create_table():
    Song.create_table()
    CURSOR.execute("PRAGMA table_info(songs)")
    columns = CURSOR.fetchall()
    assert len(columns) == 3  # Check if there are 3 columns (id, name, album)

def test_create_and_save_song():
    song = Song.create("Hello", "25")
    assert song.id is not None  # Check if the song has an ID after saving
    CURSOR.execute('SELECT * FROM songs')
    rows = CURSOR.fetchall()
    assert len(rows) == 1  # Check if there is 1 row in the songs table

# Add more test cases as needed

if __name__ == '__main__':
    pytest.main()
