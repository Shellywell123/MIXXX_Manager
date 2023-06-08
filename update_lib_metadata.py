from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC
from tqdm import tqdm
import os

#----------------------------------------------------------------------------

def UpdateMetadata(lib, exts, GenreFromDirName, TitleFromFileName):
    """
    Custom function for sorting track metadat in DJ libraries
    """
    
    tracks_total = 0
    titles_updated = []
    genres_updated = []

    # expects lib of strcture lib_root/genre/track.mp3
    for genre_dir in os.listdir(lib):

        tracks = os.listdir(lib+'/'+genre_dir)

        print ("-"*100,f"\n{genre_dir} \n{len(tracks)} tracks (mp3/wav)")
        
        for i in tqdm(range(len(tracks))):
            track = tracks[i]
            fname =lib+'/'+genre_dir+'/'+track

            if track[-4:].lower() in exts :

                tracks_total += 1

                # Read ID3 tag or create it if not present
                try: 
                    tags = ID3(fname)
                except ID3NoHeaderError:
                    tags = ID3()

                # perform updates ---------------------------------

                if GenreFromDirName:
                    tags["TCON"] = TCON(encoding=3, text=str(genre_dir))
                    genres_updated.append([track,genre_dir])
                    tags.save(fname)
                
                if TitleFromFileName:
                    tags["TIT2"] = TIT2(encoding=3, text=str(track[:-4]))
                    titles_updated.append([track,genre_dir])
                    tags.save(fname)
                
                # -------------------------------------------------
        
    # updates summary
    tracks_modified = sum([len(titles_updated), len(titles_updated)])
    if tracks_modified != 0:
        
        print(f'{tracks_modified} tracks updated.')
        print(f' - {len(titles_updated)} Title updates.')
        for track in titles_updated:
            print(f' - "{track}"')

        print(f' - {len(genres_updated)} Genre updates.')
        print(f'{len(tracks_modified)} tracks updated. \nChanged the following tracks genre metadata to "{genre_dir}" :')
        for [track,genre] in genres_updated:
            print(f' - "{track}"')
    
    # lib summary
    print(f'{tracks_total} tracks found')
    
#----------------------------------------------------------------------------

lib = "../Mixing_Lib"
exts = [".wav", '.mp3']

UpdateMetadata(lib, exts, GenreFromDirName=True, TitleFromFileName=False)