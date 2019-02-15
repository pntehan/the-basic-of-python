a = [i*i for i in range(1,101) if i%5==0]
# print(a)
b = [x+y for x in 'ABC' for y in 'XYZ']
# print(b)
c = (x for x in range(1,101))
# print(c)
def func(x):
	return x*x
# print(list(map(func, c)))
def is_odd(x):
	return x%2 == 1
# print(list(filter(is_odd, c)))
a = [-1,2,-3,4,5,-4]
print(sorted(a))
print(sorted(a, key=abs))#接受abs函数，实现绝对值大小排序
