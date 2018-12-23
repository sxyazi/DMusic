import time
from . import app
from modules import Utils
from modules import KKBox
from modules import Youtube
from modules import Storage
from flask import abort, request, render_template, send_from_directory


@app.route('/')
def home():
    recent = Storage.get_recent()
    return render_template('index.html', recent=recent)


@app.route('/ranks')
def ranks():
    music = KKBox.ranks()
    return render_template('ranks.html', music=music)


@app.route('/search', methods=['POST'])
def search():
    videos = Youtube.search(request.form['kw'])
    return render_template('search.html', videos=videos)


@app.route('/play')
def play_by_search():
    try:
        first_video = Youtube.search(request.args['kw'])[0]
        Storage.add_recent({
            'id': first_video['id']['videoId'],
            'title': first_video['snippet']['title'],
            'descr': first_video['snippet']['description'],
            'thumb': first_video['snippet']['thumbnails']['default']['url'],
            'created_at': time.time(),
            'published_at': Utils.get_timestamp(first_video['snippet']['publishedAt'])})
        Youtube.download_audio(first_video['id']['videoId'])

        return send_from_directory('/caches', filename=first_video['id']['videoId'])
    except Exception:
        abort(404)


@app.route('/play/<video_id>')
def play(video_id):
    Youtube.download_audio(video_id)
    return send_from_directory(directory='/caches', filename=video_id)
