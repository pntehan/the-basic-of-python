def lazy_num(*args):
	def sum(ax):
		for n in args:
			ax += n
		return ax
	return sum
# f = lazy_num(1,2,3)
# print(f(5))

def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())
def count():
	def f(j):
		return j*j
	fs = []
	for j in range(1, 4):
		fs.append(f(j))
	return fs
# print([x for x in count()])

a = list(map(lambda x: x*x, [1,2,3]))
# print(a)
b = lambda x: x*x
# print(b(5))
def build(x, y):
	return lambda: x*x+y*y
# print(build(1, 2)())


#以上作为装饰器的入代码