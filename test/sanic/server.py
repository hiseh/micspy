'''
the example of sanic server
'''
import asyncio
from sanic import Sanic, response, exceptions
import my_blueprint

app = Sanic(__name__)

async def notify_server_started_after_five_seconds():
    await asyncio.sleep(5)
    print('Server successfully started!')

app.add_task(notify_server_started_after_five_seconds())

@app.listener('before_server_start')
async def before_server_start(app, loop):
    print('\n', before_server_start.__name__, '\n')

@app.listener('after_server_start')
async def after_server_start(app, loop):
    print('\n', after_server_start.__name__, '\n')

@app.listener('before_server_stop')
async def before_server_stop(app, loop):
    print('\n', before_server_stop.__name__, '\n')

@app.listener('after_server_stop')
async def after_serfer_stop(app, loop):
    print('\n', after_serfer_stop.__name__, '\n')

@app.middleware('request')
async def print_on_request(request):
    print('request middle: {url}'.format(url=request.url))


@app.middleware('response')
async def print_on_response(request, response):
    print('response middle')

app.blueprint(my_blueprint.bp, url_prefix='/bbb')


@app.route('/tag/<tag:[0-9]+>', methods=frozenset({'GET'}))
async def handler1(request, tag):
    return response.json({'tag': tag})


async def handler2(request, name):
    return response.text('handler2 name: {name}'.format(name=name))


@app.exception(exceptions.NotFound)
def _404_exception(request, exception):
    return response.text('自定义的404: {url}'.format(url=request.url))


# @app.route('/<tag:int>', methods=['POST'])
app.add_route(handler2, '/name/<name>', methods=frozenset({'POST'}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True, access_log=True)
