from __future__ import unicode_literals
import youtube_dl
import sys

API_KEY = 'AIzaSyCJ8A8YcP_fz3X119-6gQBKcZgVtTFDSuQ'

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


music_opt = {
    'format': 'bestaudio/best',
    'outtmpl': 'C:/Users/zizou/Music/music a trier/%(title)s.%(ext)s',
    'playliststart': 1,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

playlist_opt = {
    'format': 'bestaudio/best',
    'outtmpl': 'C:/Users/zizou/Music/%(playlist)s/%(title)s.%(ext)s',
    'playliststart': 1,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

playlist = ['https://www.youtube.com/playlist?list=PLTH1GOQXUyBkWritgnPtA3aqYa6ElRCkn']

music = ['https://www.youtube.com/watch?v=9mMhWUM0KHE']

if __name__ == "__main__":
    type_dl = str(sys.argv[1])
    url = str(sys.argv[2])

    if type_dl == 'MUSIC':
        with youtube_dl.YoutubeDL(music_opt) as ydl:
            ydl.download([url])
    elif type_dl == 'PLAYLIST':
        with youtube_dl.YoutubeDL(playlist_opt) as ydl:
            ydl.download([url])

