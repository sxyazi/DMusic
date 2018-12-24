import redis
import pickle
from modules import Utils
r = redis.Redis(host='127.0.0.1', port=6379, db=0)


class Storage:
    @staticmethod
    def add_recent(entity):
        r.zadd('dm:recent', {
            pickle.dumps(entity): Utils.get_milli_timestamp()})
        r.zremrangebyrank('dm:recent', 300, -1)

    @staticmethod
    def get_recent():
        return [
            {**pickle.loads(x[0]), 'created_at': x[1]/1000}
            for x in r.zrevrange('dm:recent', 0, 100, True)]
