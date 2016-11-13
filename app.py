import hug

@hug.get('/')
def hello(name='world'):
    return {'hello': name}
