def output(name, func='Hello, World!'):
	#func是默认参数
	print('I\'m', name)
	print(func)
# output('pntehan')
# output('pntehan', 'I\'m coding now.')

def sum(*number):
	#number是可变参数,转换为元组
	sum = 0
	for i in number:
		sum += i
	print(sum)
# sum(1,2,3,4,5)
# sum(*[1,2,3,4,5])

def person(name, age, **other):
	#other是关键词参数，转换为字典
	print('name:',name,'age:',age,'other:',other)
# person('pntehan', 18)
# person('pntehan', 18, city='宣城', job='程序员')

def person(name, age, *, city, job):
	#*后的参数的命令的关键词参数，调用时必须写明
	print(name, age, city, job)
# person('pntehan', 18, city='宣城', job='程序员')

def fact(num):
	#普通递归函数，递归次数不超过一千次
	if num == 1:
		return 1
	return num + fact(num-1)
# print(fact(998))

def fact_iter(num, flag):
	#尾递归，调用函数自身，python中未优化。递归次数不超过一千次
	if num == 1:
		return flag
	return fact_iter(num-1, num+flag)
# print(fact_iter(998, 1))

def move(num, a, b, c):
	if num == 1:
		print('{}-->{}'.format(a, c))
	else:
		move(num-1, a, c, b)
		print('{}-->{}'.format(a, c))
		move(num-1, b, a, c)
# move(3, 'A', 'B', 'C')