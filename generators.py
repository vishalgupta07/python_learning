# -*- coding: utf-8 -*-
# @Author: gvishal
# @Date:   2019-04-05 12:03:11
# @Last Modified by:   gvishal
# @Last Modified time: 2019-04-05 13:01:52
def square_numbers(nums):
	result = list()
	for i in nums:
		result.append(i**2)

	return res

def sq_num_generator(nums):
	for i in nums:
		yield(i**2)

def main():
	my_nums = [1,2,3,4,5]
	#gives out a generator obj
	# print(sq_num_generator(my_nums))
	my_nums = sq_num_generator(my_nums)
	for num in my_nums:
		print(num)

	

if __name__ == '__main__':
	main()