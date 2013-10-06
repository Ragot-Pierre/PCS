# -*- coding: utf-8 -*-

import os

os.chdir("C://Users//Elpollo973//Documents//GitHub//PythonCodeSnippets//Hello_World_!")

from Funcs import *

quit = 0
user = "you"

while quit != 1:
	user_message = str(input())
	if user_message == "Hi":
		say_hello(user)
	elif user_message == "Bye":
		say_goodbye(user)
		quit = 1
	else:
		say_what()
