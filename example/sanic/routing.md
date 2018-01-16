# 路由
&emsp;&emsp;用户可以通过路由来设置URL与handler之间的关联。一个基本的路由形式如下：
```python
from sanic import response

@app.route("/")
async def test(request):
    return response.text('Hello World')
```
&emsp;&emsp;sanic的handler函数必须用`async`关键字定义为异步函数。
## Request参数
&emsp;&emsp;request路由规则与flask一致，可以使用变量、正则来设置。
```python
from sanic.response import text

# 参数名: tag，可以是任意字符
@app.route('/tag/<tag>')
async def tag_handler(request, tag):
    return text('Tag - {}'.format(tag))

# 参数名: integer_arg，int类型
@app.route('/number/<integer_arg:int>')
async def integer_handler(request, integer_arg):
    return text('Integer - {}'.format(integer_arg))

@app.route('/number/<number_arg:number>')
async def number_handler(request, number_arg):
    return text('Number - {}'.format(number_arg))

# 参数名: name，英文字母
@app.route('/person/<name:[A-z]+>')
async def person_handler(request, name):
    return text('Person - {}'.format(name))

# 参数名: folder_id，英文字母+数字，0~4个字符长度
@app.route('/folder/<folder_id:[A-z0-9]{0,4}>')
async def folder_handler(request, folder_id):
    return text('Folder - {}'.format(folder_id))
```