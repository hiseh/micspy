'''
the example of sanic server
'''
from sanic import Sanic, response, exceptions
import blurpoint

app = Sanic(__name__)

@app.middleware('request')
async def print_on_request(request):
    print('request middle: {url}'.format(url=request.url))

@app.middleware('response')
async def print_on_response(request, response):
    print('response middle')

app.blueprint(blurpoint.bp)

async def handler1(request, tag):
    return response.json({'tag': tag})

async def handler2(request, name):
    return response.text('handler2 name: {name}'.format(name=name))

@app.exception(exceptions.NotFound)
def _404_exception(request, exception):
    return response.text('自定义的404: {url}'.format(url=request.url))

# @app.route('/<tag:int>', methods=['POST'])
app.add_route(handler1, '/tag/<tag:[0-9]+>', methods=frozenset({'GET'}))
app.add_route(handler2, '/name/<name>', methods=frozenset({'POST'}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True, access_log=True)
