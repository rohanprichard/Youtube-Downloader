from imp import lock_held
import multiprocessing
from multiprocessing.dummy import Pool 
import time
import pytube

global c,n,mb,lck

def threader(video):
    global c, n, mb, lck
    vid = video.streams.filter(file_extension='mp4').get_highest_resolution()
    lck.acquire()
    pid = c
    c += 1

    try:
        print(pid,"/",n,"\nCurrent Video: ", "\nSize:",video.title, round((vid.filesize_approx/1024)/1024),"MB")
        lck.release()
        vid.download(save)

    except:
        lck.release()
        print("Error")

    print(video.title, "done!")
    mb += round((vid.filesize_approx/1024)/1024)

c = 0
mb = 0
lck = multiprocessing.Lock()
start = time.time()

save = input("Enter Save Directory: ")
link = input("Enter Playlist Link: ")

playlis = pytube.Playlist(link)

n = playlis.length

result = Pool(n).map(threader, playlis.videos)
end = time.time()
print("_" * 50, "All videos downloaded. \nTotal space used:", mb, "MB","\nTime spent: ",(end-start)//60, "Seconds")

# https://www.youtube.com/playlist?list=PLqUS_bcV-9n5ifwdkjD3qIophRU_owEV5
# /Users/rohanrichard/Desktop/Code/YT Downloader/Downloads
