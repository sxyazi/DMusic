from youtube import Youtube
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    videos = Youtube.search(request.form['kw'])
    return render_template('search.html', videos=videos)


@app.route('/play/<video_id>')
def play(video_id):
    Youtube.download_audio(video_id)
    return send_from_directory(directory='caches', filename=video_id)
