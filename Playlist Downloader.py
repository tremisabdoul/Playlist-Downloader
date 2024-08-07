# Playlist Downlader - tremisabdoul

from youtubesearchpython import VideosSearch
from pytube import YouTube
from time import time

OUTPUT_DIR = "Have a nice day buddy"
INPUT_FILE = "music_list.txt"
ERROR_FILE = "musics_not_found.txt"

def youtube_search(string: str = "Numb Linkin Park"):
    # Search [string] on youtube and return the 1st result
    print("searching...")
    retry = 16
    while True:
        try:
            videosSearch = VideosSearch(string, limit = 1)
            break
        except:
            if retry == 0:
                print("\n\t*** Error: Cannot Search ***")
                print(  "\t^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
                return False
            retry -= 1
            print("Retry:", 16-retry)
    result = videosSearch.result()["result"][0]
    print(result["title"] + " (" + result["channel"]["name"] + ")" + " " + result["link"])
    return result["link"]


def youtube_download(link: str = "https://www.youtube.com/watch?v=kXYiU_JCYtU"):
    # Download [link] from youtube
    print("downloading...")
    streams = None
    yt = YouTube(link)
    s = {}
    retry = 16
    retry = 16
    while True:
        try:
            streams = yt.streams.filter(only_audio=True, type="audio", progressive=False)
            break
        except:
            if retry == 0:
                print("\n\t*** Error: Cannot Get Streams ***")
                print(  "\t^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
                return False
            retry -= 1
            print("Retry:", 16-retry)
    for stream in streams:
        if not stream.audio_codec in s.keys() or s[stream.audio_codec].bitrate < stream.bitrate:
            s[stream.audio_codec] = stream
    for audio_codec in ["opus", "mp4a.40.2", "mp4a.40.5"]:
        if audio_codec in s.keys():
            stream = s[audio_codec]
            print(stream.audio_codec, "(", stream.bitrate, "kbps )")
            stream.download(output_path=OUTPUT_DIR)
            return True
    for stream in s.values():
        print(stream.audio_codec, "(", stream.bitrate, "kbps )")
        stream.download(output_path=OUTPUT_DIR)
        return True
    print("\n\t*** Error: No Stream Found ***")
    print(  "\t^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    return False


def download_from_csv(file: str = "tracks.csv"):
    t0= time()
    errors = []
    file = open(INPUT_FILE, "r", encoding="utf8")
    track = file.readline()
    track_count = 0
    while track:
        track_count += 1
        track = file.readline()
    
    file = open(INPUT_FILE, "r", encoding="utf8")
    track = file.readline()
    i = 1
    while track:
        if track[-1] == "\n":
            track = track[:-1]
        print("\nDownloading Track:", i, "/", track_count)
        tx = int((time()-t0)+3/2) # (Average time per track + 3 seconds wich is my estimated time per track) / 2
        print("Time: " + str(tx//60) + ":" + str((tx%60)//10) + str((tx%60)%10))
        tx = (tx/i)*track_count - tx
        print("Estimated Remaining Time: " + str(int(tx//60)) + ":" + str(int((tx%60)//10)) + str(int((tx%60)%10)))
        print(track)
        link = youtube_search(track)
        if link:
            result = youtube_download(link)
        if not (bool(link) and result):
            errors.append(track)
        i += 1
        track = file.readline()
    file.close()
    print("Errors: ")
    for error in errors:
        print(error)
    file = open(ERROR_FILE, "w")
    file.writelines(errors)
    file.close()


download_from_csv()
