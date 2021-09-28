#!/usr/bin/python


# This is Hello World with Python multithreading.
# A user defined function is created and 
# the function is called when a thread is initialized. 


import threading


def MyFunction():
	"""This is a user defined function"""
	print "Hello World"
	fp = open("file.abc")
	return


def Main():
	"""This is where we create a thread. 
	Target means run this function when a thread is initiated."""
	myThread = threading.Thread(target=MyFunction) 	
	myThread.start() 	# Starting a thread
	fp = open("def.txt")
	print("File opened success")
	ilist = ['apple','cat','bat']
	ilist.append('dog')


if __name__ == '__main__':
	Main()
