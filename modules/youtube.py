import requests
import youtube_dl
from exceptions import FileTooLarge


class Youtube:
    __KEY = 'AIzaSyBJTDPkg23d3-Yylo9_XCjqdXNoD4csh5M'

    @classmethod
    def search(cls, kw):
        return cls._request_with_key('search', 'part=id,snippet&q=%s' % kw)['items']

    @classmethod
    def download_audio(cls, video_id):
        options = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': "mp3",
            'outtmpl': 'caches/%(id)s',
            'noplaylist': True, }

        with youtube_dl.YoutubeDL(options) as ydl:
            info = ydl.extract_info('http://youtu.be/%s' %
                                    video_id, download=False)
            if info['filesize'] > 10 * 1024 * 1024:
                raise FileTooLarge('文件尺寸不得超过 10M')

            ydl.download(['http://youtu.be/%s' % video_id])
            return info

    @classmethod
    def _request_with_key(cls, url, params=''):
        return requests.get('https://www.googleapis.com/youtube/v3/%s?key=%s&%s' %
                            (url, cls.__KEY, params)).json()
