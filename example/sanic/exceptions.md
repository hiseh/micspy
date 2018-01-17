# 异常
Sanic可以自动地在handler中抛出异常，异常信息会作为它的第一个参数，包含`response`的状态码。
## 抛出异常
使用Python自带的`raise`或者`exceptions.abort()`都可以抛出异常
```python
from sanic.exceptions import ServerError

@app.route('/killme')
def i_am_ready_to_die(request):
    raise ServerError("Something bad happened", status_code=500)

@app.route('/youshallnotpass')
def no_no(request):
        abort(401)
        # this won't happen
        text("OK")
```
`about()`封装了`raise`，会抛出一个基于`SanicException`的异常，除非特别指定，否则返回HTTP状态码对应的标准信息（在`response.STATUS_CODES`中设置）。