import os
from mutagen import File

def find_files_without_genre_tag(directory):
    # Initialize an empty list to store filenames without a genre tag
    files_without_genre_tag = []
    
    # Recursively search for music files in the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.mp3') or file_name.endswith('.flac') or file_name.endswith('.ogg'):
                file_path = os.path.join(root, file_name)
                audio = File(file_path)
                print(audio.tags.get('genre'))
                if audio.tags.get('genre') == None:
                    files_without_genre_tag.append(file_path)

    # Return the list of filenames without a genre tag
    return files_without_genre_tag

# Example usage
files_without_genre = find_files_without_genre_tag('E:\\Downloads\\mp3s')
print(files_without_genre)