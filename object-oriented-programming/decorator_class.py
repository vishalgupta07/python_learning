# -*- coding: utf-8 -*-
# @Author: gvishal
# @Date:   2019-04-05 17:40:27
# @Last Modified by:   gvishal
# @Last Modified time: 2019-04-05 18:04:54

# class decorator_class(object):
# 	def __init__(self, original_function):
# 		self.original_function = original_function

# 	def __call__(self, *args, **kwargs):
# 		print(f'call method called before {self.original_function.__name__}')
# 		return self.original_function(*args, **kwargs)

# @decorator_class
# def display_info(name, age):
# 	print('display parameters are {name} {age}')

# display_info('vishal', 45) 

def my_logger(orig_func):
	import logging 
	logging.basicConfig(filename=f'{orig_func.__name__}.log',level=logging.INFO)

	def wrapper(*args, **kwargs):
		logging.info(
			f'ran with args : {args}, and kwargs : {kwargs}'
			)
		return orig_func(*args, **kwargs)
	return wrapper


def my_timer(orig_func):
	import time

	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = orig_func(*args, **kwargs)
		t2 = time.time() - t1
		print(f'time taken by {orig_func.__name__} is {t2}')
		return result

	return wrapper






import time



@my_logger
# @my_timer
def display(name, age):
	time.sleep(1) #forcibly sleep for 1secs
	print(f'display function ran with args {name}, {age}')

display('vishal', 90)