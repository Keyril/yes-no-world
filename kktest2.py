#!/usr/local/bin/python

def getInput():
	inputtext = input("Would you like to run? (yes/no):  ")
	giveResponse(inputtext)

def giveResponse(inputtext):
	if (str(inputtext) == "y" or "yes"):
		print("Hello World")
	elif (str(inputtext) == "n" or "no"):
			print("Will not run")
	else: 
			print("Please use input of 'yes' or 'no' (y or n suffices as well)") 
			return getInput
def main():
	getInput()

if __name__=='__main__':
	main()