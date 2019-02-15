#IO编程
#异步IO和同步IO的优缺点
#异步IO效率高，当编程复杂性也高，同步IO反之
#文件读写
# with open('../申请数据.txt', 'r') as f:
# 	for lines in f.readlines():
# 		print(lines.strip())
# #使用with...as...语句可以做到f一次性读取文件数据，且自动关闭文件
# with open('../test.txt', 'w') as f:
# 	f.write('Hello, World!')
#StringIO and BytsIO
# from io import StringIO

# f = StringIO()
# f.write('hello, World!')
# # print(f.getvalue())
# fp = StringIO('-Sup?\n-Nothing...\n-Fuck u!')
# for lines in fp.readlines():
# 	print(lines.strip())

# from io import BytesIO

# f = BytesIO()
# f.write('争做社会主义接班人'.encode('utf-8'))
# data = f.getvalue()
# print(data)
# fp = BytesIO(data)
# print(fp.read().decode('utf-8'))
#文件操作，大一暑假玩了一暑假文件操作，看看略了
#序列化
# import pickle
# f = open('../test.txt', 'wb')
# d = dict(name='Bob', age=20, score=88)
# pickle.dump(d, f)
# f.close()
# f = open('../test.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)
import json
d = dict(name='Pntehan', sex='Male', age=17)
jd = json.dumps(d)
print(jd)




















