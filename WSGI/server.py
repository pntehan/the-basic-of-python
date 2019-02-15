from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('192.168.42.119', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()