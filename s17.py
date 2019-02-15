# from datetime import datetime
# #python时间操作
# now = datetime.now()
# print(now)
# now_temp = now.timestamp()
# print(now_temp)
# new_now = datetime.fromtimestamp(now_temp)
# print(new_now)

# from collections import namedtuple
# from collections import deque
# from collections import defaultdict
# #python集合类，集合模块
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1,2)
# print('x: {}, y: {}'.format(p.x, p.y))
# Circle = namedtuple('Circle', ['x', 'y', 'r'])
# R = Circle(0,0,1)
# print('x: {}, y: {}, r: {}'.format(R.x, R.y, R.r))
# q = deque(['a', 'b', 'c'])
# print(q)
# q.append('x')
# print(q)
# q.appendleft('y')
# print(q)
# d = defaultdict(lambda: 'NaN')
# d['one'] = 'one'
# print(d['one'])
# print(d['two'])

# import struct
# #解决bytes和其他二进制数据类型的转换
# p = struct.pack('>I', 2)
# print(struct.unpack('>I', p))

# import hashlib
# #python自带摘要算法的库
# md5 = hashlib.md5()
# md5.update('I use python...'.encode('utf-8'))
# print(md5.hexdigest())

# import itertools
# #python自带操作迭代对象的模块
# natuals = itertools.count(1)
# word = itertools.cycle('ABCDEF')
# repe = itertools.repeat('P', 3)
# #以上生成可无限迭代对象
# for c in itertools.chain('ABC', 'XYZ', '123456'):
# 	print(c)
# for key, group in itertools.groupby('AABBBDDEEWW'):
# 	print(key, list(group))












