'''
the example of sanic server
'''
from sanic import Sanic, response

app = Sanic(__name__)

@app.middleware('request')


if __name__ == '__main__':
    pass

