
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC

import os

# def convert_to_mp3(path_to_file):
#     """
#     converts file to mp3 using ffmpeg pytohn wrapper
#     """
#     input_form = path_to_file
#     output_form = path_to_file[:-4]+."mp3"
#     os_str = "ffmpeg -i {} -vn -ar 44100 -ac 2 -b:a 192k {}".format(input_form,output_form)
#     os.system(os_str)
#     os.system()

lib = "/home/shellywell/Music/Mixing_Lib"

for genre_dir in os.listdir(lib):

    print (genre_dir)

    for track in os.listdir(lib+'/'+genre_dir):
        fname =lib+'/'+genre_dir+'/'+track

        if track[-4:] == ".mp3":
          #  print(' - ',track

            # Read ID3 tag or create it if not present
            try: 
                tags = ID3(fname)
            except ID3NoHeaderError:
                print("Adding ID3 header")
                tags = ID3()

            tags["TCON"] = TCON(encoding=3, text=str(genre_dir))

            tags.save(fname)
 
