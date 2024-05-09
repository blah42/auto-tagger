import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import os
#import openl3
#import soundfile as sf
from mutagen.easyid3 import EasyID3
import numpy as np
from mutagen.id3 import ID3NoHeaderError

# Step 3: Generate Tags
def tag_files(root_folder):
    i = 0
    for root, dirs, files in os.walk(root_folder):
        i= i+1
        print(i)
        print(root)
        for file_name in files:
            try:
                if file_name.endswith('.mp3'): # Check if file is an mp3
                    file_path = os.path.join(root, file_name)
                    try: # Try loading id3 tags for file, creates one if file doesn't have any
                        tags = EasyID3(file_path)
                    except ID3NoHeaderError:
                        tags = EasyID3()
                        tags.save(file_path)
                    # Get artist, album, and track info from folder structure
                    artist, album = os.path.split(root)[-2:]
                    artist = artist.lstrip(root_folder+"\\")
                    track_info = file_name.split(' - ', 1)
                    try:
                        track_num, track_title = track_info[0], track_info[1].rstrip('.mp3')
                    except IndexError: # If file name is not of the expected format, skip the file
                        continue

                    # Add tags to mp3 file
                    tags['title'] = track_title
                    tags['artist'] = artist
                    tags['album'] = album
                    tags['tracknumber'] = track_num

                    # Get genre of mp3 file and add it to tags
                    genre = tags.get('genre')
                    #if not genre:
                        #tag,tag2 = generate_tags(file_path)
                        #print(tag)
                        # tags['mood'] = mood
                    tags.save()
            except:
                continue


#def generate_tags(file_path):

root_folder = 'Z:\\inbox2\\' # Set initial (root) folder
tag_files(root_folder) # Run the function to tag all mp3 files in the root folder
