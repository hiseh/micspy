# 中间件和监听器
中间件是一类特定方法，它们会在服务器收到request之前或之后执行，通常用来定制request和response。此外，Sanic还提供了监听器机制，可以在程序生命周期的不同点运行自己的代码。
## 中间件
有两种类型的中间件：request和response，都由`@app.middleware`装饰器定义，定义时通过字符串参数`request`或`response`来设定类型。Response中间件需要接收request和response作为参数。中间件可以修改传给它的request和response参数，同时不返回。
```python
app = Sanic(__name__)

@app.middleware('response')
async def custom_banner(request, response):
    response.headers["Server"] = "Fake-Server"

@app.middleware('response')
async def prevent_xss(request, response):
    response.headers["x-xss-protection"] = "1; mode=block"

app.run(host="0.0.0.0", port=8000)
```