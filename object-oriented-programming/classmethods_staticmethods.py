# -*- coding: utf-8 -*-
# @Author: gvishal
# @Date:   2019-04-06 13:58:25
# @Last Modified by:   gvishal
# @Last Modified time: 2019-04-06 14:24:11
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

	def __str__(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	
	##class methods 

	#it accepts class as a first instance rather than using 
	#regular methods that take in self i.e instance as the 
	#the first argument
	#class : cls, *args : amt
	@classmethod
	def set_raise_amt(cls, amt):
		cls.raise_amt = amt

	@classmethod
	def from_str(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)


	#static methods: classmethods accept class as the first argument
	# 				 regular methods accept the instance of class/object 
	# 				 as the arguement
	# above has some logical connection to our class or not
	# where as static methods dont pass any of the above

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


#many people confuse between classmethod, regular method, static method
def main():
	emp1 = Employee('Vishal', 'Gupta', 4500000)
	emp2 = Employee('Sahil', 'Gupta', 4500000)
	emp3 = Employee('Vinay', 'Rathwa', 4500000)
	emp4 = Employee('Pranav', '', 4500000)
	emp5 = Employee.from_str('vishal-gupta-54000000')
	print(emp5 .fullname())




	#running the classmethod from instance also changes the functionality as 
	#the same as the using the class instance as the same


if __name__ == '__main__':
	main()
		
		