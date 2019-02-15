# # 异步IO
# # 协程
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...'%n)
#         r = '200 OK'

# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n += 1
#         print('[PRODUCER] Producing %s...'%n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer retrun: %s'%r)
#     c.close()

# c = consumer()
# produce(c)

# #asyncio实现异步IO
# import asyncio

# @asyncio.coroutine
# def hello():
#     print('Hrllo World!')
#     r = yield from asyncio.sleep(1)
#     print('Hello again!')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()
# # 放弃了，有点难度