import functools
int2 = functools.partial(int,base=2)

def outprint(word):
	print('Hello, {}!'.format(word))

# outprint('world')
name_print = functools.partial(outprint,word='name')
# name_print()
max2 = functools.partial(max,10)
# print(max2(2,3,6,11))