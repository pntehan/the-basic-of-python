dic = {'Lucy':96, 'Mary':100,'Json':67}
# print(dic)
# print(dic['Lucy'])
k = 'Pntehan'
k = 'Mary'
if k in dic:
	print(dic.get(k))
else:
	print(dic.get(k, 'He not here'))
dic.pop(k)
# print(dic)
s =set([1,1,2,2,3,4,5])
# print(s)
s.add(5)
# print(s)
s.add(6)
# print(s)
s.remove(6)
# print(s)
s.remove(5)
# print(s)
print(s&set([2,3,7]))
print(s|set([2,3,7]))
