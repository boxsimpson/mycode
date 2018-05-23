#!/usr/bin/env python3

while(True):
	program = input("What program are you trying to run eth, fc, ifb, or otn ? ")
	if program == "eth":
		print("ethernet protocol allowed")
		break
	elif program == "fc":
		print("fiber channel NOT allowed")
	elif program == "ifb":
		print("ifiniband NOT ALLOWED")
	elif program == "otn":
		print("Optical Network allowed")
		break
	else :
		print("NO idea what that trechnology is")

		