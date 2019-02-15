# import os
# #Mac,linux,Unix下可以调用fork(), Windox下不能使用
# print('Process ({}) start...'.format(os.getpid()))
# pid = os.fork()
# if pid == 0:
# 	print('I am child process ({}) and my parent is {}.'.format(os.getpid(), os.getppid()))
# else:
# 	print('I ({}) just created a child process ({}).'.format(os.getpid(), os.getppid()))

# from multiprocessing import Process
# import os
# #普通进程
# def run_proc(name):
# 	print('Run child process {} ({})...'.format(name, os.getpid()))

# if __name__ == '__main__':
# 	print('Parent process {}.'.format(os.getpid()))
# 	p = Process(target=run_proc, args=('one',))
# 	print('Child process will start.')
# 	p.start()
# 	p.join()
# 	print('Child process end.')
# #进程池批量调用进程
# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name, lst):
# 	print('Run task {} ({})...'.format(name, os.getpid()))
# 	start = time.time()
# 	print(list(map(lambda x: x+1, lst)))
# 	end = time.time()
# 	print('Task %s runs %0.2f seconds.'%(name, (end-start)))

# if __name__ == '__main__':
# 	print('Parent process {}'.format(os.getpid()))
# 	p = Pool(4)
# 	for i in range(5):
# 		p.apply_async(long_time_task, args=(i,[i, i+1]))
# 	print('Waiting for all subprocesses done...')
# 	p.close()
# 	p.join()
# 	print('All subprocesses done.')
# #subprocess模块启动,控制子进程
# #多线程
# import time, threading

# def loop():
# 	print('Thread {} is running...'.format(threading.current_thread().name))
# 	n = 0
# 	while n<5:
# 		n += 1
# 		print('Thread {} >>> {}'.format(threading.current_thread().name, n))
# 		time.sleep(1)
# 	print('Thread {} ended.'.format(threading.current_thread().name))

# print('Thread {} is running...'.format(threading.current_thread().name))
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('Thread {} ended'.format(threading.current_thread().name))
# #lack
# import time, threading
# #多线程操作同一变量时，当次数过大会发生内存指向错误
# balance = 0

# def change_it(n):
# 	global balance
# 	balance += n
# 	balance -= n

# def run_thread(n):
# 	for i in range(10000000):
# 		change_it(n)

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(5,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
# import threading, time
# #使用lock锁住进程
# balance = 0
# lock = threading.Lock()

# def change_it(n):
# 	global balance
# 	balance += n
# 	balance -= n

# def run_thread(n):
# 	for i in range(10000000):
# 		lock.acquire()
# 		try:
# 			change_it(n)
# 		finally:
# 			lock.release()
# start = time.time()
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end = time.time()
# print('balance:', balance)
# print('time: %0.2fs'%(end-start))

# import threading, multiprocessing
# def loop():
# 	x = 0
# 	while True:
# 		x = x ^ 1
# for i in range(multiprocessing.cpu_count()):
# 	t = threading.Thread(target=loop)
# 	t.start()
import os, time, threading
from multiprocessing import Pool
from glob import *
import obspy
import pandas as pd

class Read_SAC(object):
	"""docstring for Read_SAC"""
	def __init__(self, file_path):
		self.file_path = file_path

	def read(self):
		return obspy.read(self.file_path)[0]

	def get_infor(self, st):
		return st.stats

	def resample_data(self, st):
		return st.resample(1/60)

	def get_data(self, st):
		return st.data

def loop(file_path):
	print('Run task {} ({})...'.format(file_path.split('\\')[-1], os.getpid()))
	start = time.time()
	f = Read_SAC(file_path)
	st = f.read()
	st = f.resample_data(st)
	print('{}: {}'.format(file_path.split('\\')[-1], f.get_data(st)))
	end = time.time()

if __name__ == '__main__':
	start = time.time()
	print('Parent process {}'.format(os.getpid()))
	dirs = glob('../AXI/*.SAC')
	p = Pool(len(dirs))
	for i in dirs:
		p.apply_async(loop, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')
	end = time.time()
	print('Time: %0.2f seconds.'%(end-start))











