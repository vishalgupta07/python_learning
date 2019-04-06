# -*- coding: utf-8 -*-
# @Author: gvishal
# @Date:   2019-04-05 10:05:15
# @Last Modified by:   gvishal
# @Last Modified time: 2019-04-05 12:06:14

def list_functions():
	#list 
	course = ['history', 'maths', 'physics', 'compsci']
	# -1 is the last element in any list or array	
	print(course[:2])	
	#append
	course.append('art')
	#insert 
	course.insert(1, 'art')
	print(course)
	#extend method
	course_1 = ['humanities', 'b tech']
	#add values to first list from second list
	course.extend(course_1)
	print(course)
	#remove method - removes the first instance of the object
	course.remove('art')
	print(course)

	#sorting the list in various method
	course.reverse()
	print(course)

	course_2 = course
	#these methods use inplace sorted
	#sort in ascemding order
	course.sort()
	print(course)
	#sort in descending order 
	course.sort(reverse=True)
	print(course)

	print(course.index('maths'))
	#conditionals 
	print('compsci' in course)

	#looping in the code 
	for item in course:
		print(item, end=" -> ")

	#looping using enmurate
	for index, item in enumerate(course):
		print(index, item)

	course_str = '., '.join(course)
	print(course_str)

	new_course = course_str.split('.,')
	print(new_course)

#problems with mutable list   
#if i change the varible pointing towards the object memory
#it is changed for all the instances/obkects pointing to that location
def tup_methods():
	tup_1 = ('history', 'maths', 'physics', 'compsci')
	tup_2 = tup_1
	#tuples are immutable in nature and thus dont as many faetures as compared to the list class
	print(tup_1)
	print(tup_2)

def set_methods():
	#order may change in accordance with the run 
	#meaning that more number of time it is run the order automatically changes
	course = {'history', 'maths', 'physics', 'compsci'}
	print(course)

def init_methods():
	empty_list = []
	empty_list = list()

	empty_tup = () 
	empty_tup = tuple()

	empty_set = {}#not correct its actaully the dictionary
	empty_set = set()

def dictionary_methods():
	 student = {'name':'vishal', 'age':21, 'courses':['maths', 'compsci']}
	 print(student['courses'])
	 #key error comes when no actual key is accesed
	 #but when key is not present then it gives out the 'None' as default  
	 print(student.get('phone'))

	 #update functiom is important for updating various values at once
	 del student['age']
	 print(student)
	 student.update({'phone':'1234', 'age':23})
	 print(student)

	 #pop the values and return the value 
	 phone_num = student.pop('phone')
	 print(phone_num)
	 print(student)

	 #getting the length of dictionary
	 print(student.keys(), student.items())

	 #looping through the dictionaty
	 for key,values in student.items():
	 	print(key, values)


dictionary_methods()