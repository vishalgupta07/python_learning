# -*- coding: utf-8 -*-
# @Author: gvishal
# @Date:   2019-04-05 09:31:50
# @Last Modified by:   gvishal
# @Last Modified time: 2019-04-05 09:58:18
website = 'your\'s string'
web = "website's good"
multi_line_code = """its good to have a new 
life"""
# get the length of string
print(len(multi_line_code))
# printing the sliced part and using a upper method
print(website[:4].find('r'))
# replace method returns the string insted inplace replace
website = website.replace('string', 'mera')
print(website)
#operartor overloading works in python
print(website + '.,message')
#a better method to print placeholders in place 
message = "{}, {}, Welcome".format('yes', 'you are')
print(message)
#f strings
my_message = f'{website}, {web} Welcome'
print(my_message) 
#help function for python 
print(dir(message))
#to see more help on any data type
print(help(str))
#for a particular method
#dont execute the method instead only give out the instance 
print(help(str.lower)