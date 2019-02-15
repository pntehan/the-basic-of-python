class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age):
		# super(Student, self).__init__()
		self.name = name
		self.age = age
		
	def print_info(self):
		print('Name:{}, Age:{}'.format(self.name, self.age))

# a = Student('Pntehan', 17)
# b = Student('Jason', 32)
# a.print_info()
# b.print_info()

class Animal(object):
	"""docstring for Animal"""
	def __init__(self, genus):
		self.genus = genus

	def infor(self):
		print('It is a {}.'.format(self.genus))

	def run(self):
		print('{} is running...'.format(self.genus))

class Dog(Animal):
	'''定义一个Dog类继承Animal'''
	def __init__(self, color):
		super(Dog, self).__init__(Dog.__name__)
		self.color = color
	def showColor(self):
		print('Dog is {}...'.format(self.color))

class Cat(Animal):
	"""docstring for Cat"""
	def __init__(self, color):
		super(Cat, self).__init__(Cat.__name__)
		self.color = color
	def showColor(self):
		print('Cat is {}...'.format(self.color))
a = Dog('Red')
b = Cat('Orange')
if isinstance(a, Dog):
	print('Right...')
# print(getattr(a, 'color', 404))
# setattr(a, 'color', 'black')
# print(getattr(a, 'color', 404))
from types import MethodType
def set_name(self, name):
	self.name = name
a.set_name = MethodType(set_name, a)
#将set_name函数绑定到a对象上
a.set_name('a')
# print(a.name)
b = Dog('color')
# b.set_name('b')#set_name未绑定到同类其他对象
Dog.set_name = MethodType(set_name, Dog)
#将set_name绑定到Dog类上
b.set_name('b')
# print(b.name)

class student(object):
	__slots__ = ('name', 'age')
	#限制绑定属性，限制仅在当前类，对继承其的子类无效

a = student()
a.name = 'name'
a.age = 18
# a.sroce = 120#不可被绑定



