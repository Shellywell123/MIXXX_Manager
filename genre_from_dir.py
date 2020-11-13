from mutagen.easyid3 import EasyID3
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

lib = "path to ... /Mixing_Lib"

for genre_dir in os.listdir(lib):

    print (genre_dir)

    for track in os.listdir(lib+'/'+genre_dir):
        print(' - ',track)

        try:
            audio = EasyID3(lib+'/'+genre_dir+'/'+track)
            audio['genre'] = str(genre_dir)
            audio.save()
        except:
            pass