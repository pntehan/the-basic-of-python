#装饰器
def now():#函数名也是一个变量，可以作为参数传递
	print('Hello, World!')
# now()
f = now#此处的函数now作为变量传递给f
# print(f)
# f()
# print(f.__name__)#获得函数名

def log(func):
	def wrapper(*args, **kw):
		print('call {}:'.format(func.__name__))
		return func(*args, **kw)
	return wrapper
# log(lambda :print('Hello, World!'))()
@log
def Say_Hello(name):
	print('Hello, {}'.format(name))
Say_Hello('Pntehan')
# log(Say_Hello)('Pntehan')
# log(Say_Hello('Pntehan'))
# a = log(Say_Hello)
# a('Pntehan')

def log(text):
	def decorator(func):
		# wrapper.__name__ = func.__name__
		def wrapper(*args, **kw):
			print('{} {}():'.format(text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print('2019-01-31')
# now()
# log('execute')(now)()

import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('{} {}():'.format(text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator	
# log('execute')(now).__name__


