# -*- coding: utf-8 -*-
# @Author: gvishal
# @Date:   2019-04-06 15:14:00
# @Last Modified by:   gvishal
# @Last Modified time: 2019-04-06 15:20:08
class Employee:
	
	num_of_employees = 0
	raise_amt = 1.04 #raise amount is the member of class Employee
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f'{first}.{last}@company.com'

		Employee.num_of_employees += 1 #its nice to have static clases

	def fullname(self):
		return f'{self.first} {self.last}'


	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)



	#dinder methods
	#debugging method
	def __repr__(self):
		# print('calling self.__repr__')
		return f'Employee ( {self.first}, {self.last}, {self.pay})'

	def __str__(self):
		return f'{self.fullname()} - {self.email}'


emp1 = Employee('vishal', 'gupta', 4500000)
print(emp1)








