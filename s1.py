a = 'I\'m "ok"!'
b = '\\\n\n\n\\'
c = '''a
b
c'''

xin = ord('新')
# print(chr(xin))
huo = '或'.encode('utf-8')
# print(len(huo))
# print(huo.decode('utf-8'))

man = 'super man'
print('I\'m %s'%man)
print('I\'m {}'.format(man))
print('I\'m', man)

#input输入为字符串类型
name = input('Please input your name:')
print('Hello,', name)
