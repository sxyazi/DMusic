import requests
import youtube_dl


class Youtube:
    __KEY = 'AIzaSyBJTDPkg23d3-Yylo9_XCjqdXNoD4csh5M'

    @classmethod
    def search(cls, kw):
        return cls._request_with_key('search', 'part=id,snippet&q=%s' % kw)['items']

    @classmethod
    def download_audio(cls, audio_id):
        options = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': "mp3",
            'outtmpl': './caches/%(id)s',
            'noplaylist': True, }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download(['http://youtu.be/%s' % audio_id])

    @classmethod
    def _request_with_key(cls, url, params=''):
        return requests.get('https://www.googleapis.com/youtube/v3/%s?key=%s&%s' %
                            (url, cls.__KEY, params)).json()
