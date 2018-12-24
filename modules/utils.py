
import time
import dateutil.parser


class Utils:
    @staticmethod
    def get_timestamp(s):
        dt = dateutil.parser.parse(s)
        return int(time.mktime(dt.timetuple()))

    @staticmethod
    def get_milli_timestamp():
        return int(round(time.time() * 1000))
