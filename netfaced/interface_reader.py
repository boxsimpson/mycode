#!/usr/bin/env python3

import netifaces
print(netifaces.interfaces())

for i in netifaces.interfaces():
	print('\n**********Details of Interface - '+ i + ' **********')
	try:   #This is a line, you also need to indent the code below this line 
		print('MAC: ', end='')
		print(netifaces.ifaddresses(i))
		print('IP: ', end='')
		print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
	except:
		print('Could not collect adapter information') # print an error message


