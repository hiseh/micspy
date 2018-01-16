简单的例子：

    from sanic import Sanic
    from sanic import response

    app = Sanic(__name__)


    @app.route("/")
    async def test(request):
        return response.json({"test": True})

    if __name__ == '__main__':
        app.run(host="0.0.0.0", port=8000)

- Sanic Sanic的入口，用来创建Sanic实例
    - name=None 可以用\_\_name\_\_预置变量，如果name为None，则从之前栈中获得module name。

