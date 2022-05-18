import threading
import pytube as yt

def threader(vide):
    video = vide
    try:
        print("Current Video: ", video.title)
        vid = video.streams.filter(file_extension='mp4').get_highest_resolution()
        vid.download(save)
    except:
        print("Error")
    print("Done!")


save = input("Enter Save Directory: ")
link = input("Enter Playlist Link: ")

playlis = yt.Playlist(link)
for video in playlis.videos:
    
    threading.Thread(target=threader,args=video).start()