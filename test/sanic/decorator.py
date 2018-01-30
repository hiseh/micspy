from functools import wraps

def decorate_handler(method):
    @wraps(method)
    async def _deco(request, *args, **kwargs):
        print('\ndecorator\n')
        response = await method(request, *args, **kwargs)
        return response
    return _deco