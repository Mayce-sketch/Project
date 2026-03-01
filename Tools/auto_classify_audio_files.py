import os
from mutagen.mp3 import MP3
from mutagen.id3 import TPE1, TIT2, TALB, TCON, ID3, error
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
from typing import Dict, Any

# =================================================================
# MODIFY THESE LINES WITH THE VALUES YOU WISH TO APPLY
# =================================================================
FIXED_ARTIST = "Artist Name"
FIXED_ALBUM = "Album Name"
FIXED_GENRE = "Genre Name"

# REPLACE with the actual path to your music folder
music_folder = r'C:\Users\YourName\Music'
# =================================================================

def get_current_tags(audio_file: Any, extension: str) -> Dict[str, str]:
    """Retrieves current audio tags in a uniform format."""
    tags = {'title': None, 'artist': None, 'album': None, 'genre': None}

    if audio_file.tags is None:
        return tags

    if extension == '.mp3':
        tags['title'] = str(audio_file.tags.get('TIT2', [None])[0]) if audio_file.tags.get('TIT2') else None
        tags['artist'] = str(audio_file.tags.get('TPE1', [None])[0]) if audio_file.tags.get('TPE1') else None
        tags['album'] = str(audio_file.tags.get('TALB', [None])[0]) if audio_file.tags.get('TALB') else None
        tags['genre'] = str(audio_file.tags.get('TCON', [None])[0]) if audio_file.tags.get('TCON') else None

    elif extension in ('.flac', '.ogg'):
        tags['title'] = audio_file.get('title', [None])[0]
        tags['artist'] = audio_file.get('artist', [None])[0]
        tags['album'] = audio_file.get('album', [None])[0]
        tags['genre'] = audio_file.get('genre', [None])[0]

    for k, v in tags.items():
        if v is not None:
            tags[k] = v.strip()

    return tags


def update_music_tags_by_filename(folder_path):
    """
    Updates 'Title', 'Artist', 'Album', and 'Genre' tags only if
    they don't already match the target values.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid folder.")
        return

    print(f"Target folder: **{os.path.basename(folder_path)}**")
    print("-" * 30)

    AUDIO_EXTENSIONS = ('.mp3', '.flac', '.ogg')

    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                name_no_ext, extension = os.path.splitext(filename)
                extension = extension.lower()

                if extension in AUDIO_EXTENSIONS:
                    new_title = name_no_ext
                    tags_updated = False

                    try:
                        audio = None

                        # Load file based on extension
                        if extension == '.mp3':
                            audio = MP3(file_path, ID3=ID3)
                            if audio.tags is None:
                                audio.add_tags()
                        elif extension == '.flac':
                            audio = FLAC(file_path)
                        elif extension == '.ogg':
                            audio = OggVorbis(file_path)

                        # ----------------------------------------------------
                        # CHECK EXISTING TAGS
                        # ----------------------------------------------------
                        current_tags = get_current_tags(audio, extension)

                        is_title_ok = current_tags['title'] == new_title
                        is_artist_ok = current_tags['artist'] == FIXED_ARTIST
                        is_album_ok = current_tags['album'] == FIXED_ALBUM
                        is_genre_ok = current_tags['genre'] == FIXED_GENRE

                        if is_title_ok and is_artist_ok and is_album_ok and is_genre_ok:
                            print(f"Skipped: {filename} - Tags already correct.")
                            continue

                        # ----------------------------------------------------
                        # MODIFY IF NECESSARY
                        # ----------------------------------------------------
                        if extension == '.mp3':
                            if not is_title_ok:
                                audio.tags.add(TIT2(encoding=3, text=[new_title]))
                            if not is_artist_ok:
                                audio.tags.add(TPE1(encoding=3, text=[FIXED_ARTIST]))
                            if not is_album_ok:
                                audio.tags.add(TALB(encoding=3, text=[FIXED_ALBUM]))
                            if not is_genre_ok:
                                audio.tags.add(TCON(encoding=3, text=[FIXED_GENRE]))
                            audio.save()
                            tags_updated = True

                        elif extension in ('.flac', '.ogg'):
                            if not is_title_ok:
                                audio['title'] = new_title
                            if not is_artist_ok:
                                audio['artist'] = FIXED_ARTIST
                            if not is_album_ok:
                                audio['album'] = FIXED_ALBUM
                            if not is_genre_ok:
                                audio['genre'] = FIXED_GENRE
                            audio.save()
                            tags_updated = True

                        if tags_updated:
                            print(f"Updated: **{filename}** -> Title, Artist, Album, Genre synced.")

                    except error:
                        print(f"ID3 Tag Error for '{filename}'. Skipped.")
                    except Exception as e:
                        print(f" Error processing '{filename}': {e}")

    except Exception as e:
        print(f"An error occurred while scanning the folder: {e}")

# Run the script
update_music_tags_by_filename(music_folder)