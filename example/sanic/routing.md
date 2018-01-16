# 路由
&emsp;&emsp;用户可以通过路由来设置URL与handler之间的关联。一个基本的路由形式如下：
```python
from sanic import response

@app.route("/")
async def test(request):
    return response.text('Hello World')
```
&emsp;&emsp;当访问