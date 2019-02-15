def application(environ, start_reponse):
    start_reponse('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello web!</h1>'
    return [body.encode('utf-8')]

def sign(environ, start_reponse):
    start_reponse('200 OK', [('Content-Type', 'text/html')])
    body = "<form><div><label>邮箱</label><input></div><div><label>密码</label><input></div><button>登陆</button><br><a>没有账户?点击注册</a></form>"
    return [body.encode('utf-8')]