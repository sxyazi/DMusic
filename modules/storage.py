import redis
import pickle
r = redis.Redis(host='127.0.0.1', port=6379, db=0)


class Storage:
    @staticmethod
    def add_recent(entity):
        r.zadd('dm:recent', {pickle.dumps(entity): 0})
        r.zremrangebyrank('dm:recent', 300, -1)

    @staticmethod
    def get_recent():
        return [pickle.loads(x) for x in r.zrevrange('dm:recent', 0, 100)]
