from . import app
import dateutil.parser


@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    dt = dateutil.parser.parse(date)
    return dt.replace(tzinfo=None).strftime(fmt)
