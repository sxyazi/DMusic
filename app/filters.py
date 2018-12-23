from . import app
import datetime
import dateutil.parser


@app.template_filter('timefstr')
def _filter_timefstr(ts, fmt='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.utcfromtimestamp(ts).strftime(fmt)


@app.template_filter('strftime')
def _filter_strftime(date, fmt='%Y-%m-%d %H:%M:%S'):
    dt = dateutil.parser.parse(date)
    return dt.replace(tzinfo=None).strftime(fmt)
