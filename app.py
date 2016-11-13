import hug
from redis import StrictRedis

redis = StrictRedis(host='redis')

@hug.get('/')
def hello(name='world'):
    return {
        'greeting': f'hello {name}',
        'visits': redis.incr('visits')
    }
