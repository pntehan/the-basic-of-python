#多重继承
class People(object):

	def __init__(self, name, sex, age):
		self.name = name
		self.age = age
		self.sex = sex

	def __str__(self):
		return 'People object (姓名:{},性别:{},年龄:{})'.format(self.name, self.sex, self.age)

class chinese(People):
	"""docstring for chinese"""
	def __init__(self, name, sex, age):
		super(chinese, self).__init__(name, sex, age)

	def showSkill1(self):
		print('我是中国人，我有中国魂，Skr~')

class American(People):
	"""docstring for American"""
	def __init__(self, name, sex, age):
		super(American, self).__init__(name, sex, age)

	def showSkill2(self):
		print('Bro, I can\'t you why, but i can kill you and scan...')

class Skr(American, chinese):
	"""docstring for Skr"""
	def __init__(self, name, sex, age):
		super(Skr, self).__init__(name, sex, age)

# a = chinese('吴大炮', '未知', 21)
# print(a)
# a.showSkill1()
# b = American('lipump', '未知', 20)
# print(b)
# b.showSkill2()
# c = Skr('吴skr', '男', 22)
# print(c)
# c.showSkill1()
# c.showSkill2()

class fib(object):
	def __init__(self, num):
		self.num = num
		self.a = 0
		self.b = 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a+self.b
		if self.a > self.num:
			raise StopIteration();
		return self.a

# print([x for x in fib(100)])
class fib2(object):
	def __getitem__(self, num):
		if isinstance(num, int):
			a, b = 0, 1
			for i in range(num):
				a, b = b, a+b
			return a
		if isinstance(num, slice):
			a, b = 1, 1
			L = []
			for i in range(num.stop):
				if i >= num.start:
					L.append(a)
				a, b = b, a+b
			return L
# f = fib2()
# print(f[0:8])
# print(f)

class test(object):
	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return test('{}/{}'.format(self._path, path))

	def __str__(self):
		return self._path

	def __call__(self):
		print('successfully.')

a = test()
print(a.new)
a()











