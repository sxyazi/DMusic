from . import app
from modules import Utils
from modules import KKBox
from modules import Youtube
from modules import Storage
from exceptions import FileTooLarge
from flask import abort, request, render_template, send_from_directory


@app.route('/')
def home():
    recent = Storage.get_recent()
    return render_template('index.html', recent=recent)


@app.route('/search', methods=['POST'])
def search():
    videos = Youtube.search(request.form['kw'])
    return render_template('search.html', videos=videos)


@app.route('/play')
def play_by_search():
    try:
        first_video = Youtube.search(request.args['kw'])[0]
        info = Youtube.download_audio(first_video['id']['videoId'])
    except FileTooLarge as e:
        return str(e)
    except Exception:
        abort(404)

    Storage.add_recent({
        'id': info['id'],
        'title': info['title'],
        'descr': info['description'],
        'upload_date': Utils.get_timestamp(info['upload_date'])})

    return send_from_directory('../caches', filename=info['id'])


@app.route('/play/<video_id>')
def play(video_id):
    try:
        info = Youtube.download_audio(video_id)
    except FileTooLarge as e:
        return str(e)
    except Exception:
        abort(404)

    Storage.add_recent({
        'id': info['id'],
        'title': info['title'],
        'descr': info['description'],
        'upload_date': Utils.get_timestamp(info['upload_date'])})

    return send_from_directory(directory='../caches', filename=video_id)


@app.route('/ranks')
@app.route('/ranks/<typ>')
def ranks(typ='hourly'):
    music = KKBox.ranks(typ)
    return render_template('ranks.html', music=music)
