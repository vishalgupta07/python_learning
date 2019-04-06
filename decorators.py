# -*- coding: utf-8 -*-
# @Author: gvishal
# @Date:   2019-04-05 13:22:25
# @Last Modified by:   gvishal
# @Last Modified time: 2019-04-05 17:39:43

#treating fuctions as first class functions
#first class citizens in programming means treating functions as result
def logger(msg):

	def log_message():
		 print(f'{msg} hi')

	return log_message


def first_class_functions():
	def square(x):
		return x**2

	#() parenthesis means to execute the function 
	# f = square(3)
	# print(f)

	def my_map(func, arg_list):
		result = []
		for i in arg_list:
			result.append(func(i))
		return result

	print(my_map(square, [1,2,3,4,5]))


def log_main():
	print('the lazy coder')
	logged = logger('vishal')
	logged()




def clousures_methods():
	def outer_func():
		message = 'hi'

		def inner_func():
			print(message)

		return inner_func
 
	my_func = outer_func()#my func is actually a varible now 
	my_func()
	my_func()



def decorators_method():
	# what is decorator?
	# decorator is a function that takes another function as argument and 
	# return the function with improved functionality without changing the source code 
	# of original function 

	#basic decorator function 
	def decorator_function(original_function):
		def wrapper_function(*args, **kwargs):
			print(f'wrapper executed this before {original_function.__name__}')
			return original_function(*args, **kwargs)
		return wrapper_function

	# below is similar to 
	# display = decorator_function(display)
	@decorator_function
	def display():
		print('display function ran')

	@decorator_function
	def display_info(name, age):
		print(f'diaplay_info ran with argument {name} {age}')

	display_info('vishal', 56)




def main():
	decorators_method()

if __name__ == '__main__':
	main()