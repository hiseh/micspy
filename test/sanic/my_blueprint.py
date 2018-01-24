'''
蓝图
'''
from sanic import response, Blueprint, views

bp = Blueprint('blurpoint', url_prefix='/blue')

@bp.middleware('request')
async def print_bp_request(request):
    print('blue request middle')

@bp.middleware('response')
async def print_bp_reponse(request, response):
    print('blue response middle')

@bp.route('/root')
async def bp_root(request):
    print('\ntoken:', request.token, '\n')
    return response.json({'type': 'blue print'})

class TestView(views.HTTPMethodView):
    @staticmethod
    @bp.middleware('request')
    async def print_bp_view_request(request):
        print('blue view request middle')

    @staticmethod
    @bp.middleware('response')
    async def print_bp_view_response(request, response):
        print('blue view response middle')

    async def get(self, request):
        return response.json({'type': 'view class'})

bp.add_route(TestView.as_view(), '/view')