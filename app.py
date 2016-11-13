import hug

@hug.get('/')
def hello(name='world'):
    return {'greeting': f'hello {name}'}
