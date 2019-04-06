# -*- coding: utf-8 -*-
# @Author: gvishal
# @Date:   2019-04-06 14:21:16
# @Last Modified by:   gvishal
# @Last Modified time: 2019-04-06 15:17:38
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

#inheriting from employee class
class Develper(Employee):
	raise_amt = 1.5
	
	def __init__(self, first, last, pay, lang):
		#base class handling things for you
		super().__init__(first, last, pay)
		self.lang = lang

	def __str__(self):
		return f'{self.first} {self.last} {self.pay} {self.lang}'

class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print(emp.fullname())


dev_1 = Develper('vishal', 'gupta', 45000000, 'c++')
print(dev_1)











