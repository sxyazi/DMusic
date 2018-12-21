from kkbox import KKBox
from youtube import Youtube
from flask import Flask, abort, request, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


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
        Youtube.download_audio(first_video['id']['videoId'])
        return send_from_directory(directory='caches', filename=first_video['id']['videoId'])
    except Exception:
        abort(404)


@app.route('/play/<video_id>')
def play(video_id):
    Youtube.download_audio(video_id)
    return send_from_directory(directory='caches', filename=video_id)
