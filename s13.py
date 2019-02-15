from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
# 	print('{} => {} , {}'.format(name, member, member.value))
# print(Month.Jan)
# print(Month.Jan.name)
# print(Month.Jan.value)

#使用type()创建类
def fn(self, name='World'):
	print('Hello, {}!'.format(name))

Hello = type('Hello', (object,), dict(hello=fn))
# h = Hello()
# h.hello('Mary')

#metaclass创建类
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		attrs['remove'] = lambda self, value: self.pop(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
	pass
# L = MyList()
# L.add(1)
# print(L)
# L.pop(0)
# print(L)
#try writing a ORM
class Field(object):
	#定义field类用于存储字段名和字段类型
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type

	def __str__(self):
		return '{}:{}'.format(self.__class__.__name__, self.name)

class StringField(Field):
	"""docstring for StringField"""
	def __init__(self, name):
		super(StringField, self).__init__(name, column_type='varchar(100)')

class IntField(Field):
	"""docstring for IntField"""
	def __init__(self, name):
		super(IntField, self).__init__(name, column_type='int(10)')

class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		print('Found model:{}'.format(name))
		mappings = dict()
		for k, v in attrs.items():
			if isinstance(v, Field):
				print('Found mapping: {} ==> {}'.format(k, v))
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings
		attrs['__table__'] = name
		return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except:
			raise AttributeError('Model object has no attribute {}'.format(key))

	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))
		sql = 'insert into {}({}) values ({})'.format(self.__table__, ','.join(fields), ','.join(args))
		print('SQL: {}'.format(sql))
		print('ARGS: {}'.format(str(args)))

class User(Model):
	ID = IntField('id')
	name = StringField('name')

u = User(ID='001', name='pntehan')
u.save()














