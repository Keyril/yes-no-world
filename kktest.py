#!/usr/local/bin/python

def getInput():
	inputtext = input("Would you like to run? (yes/no):  ")
	giveResponse(inputtext)

def giveResponse(inputtext):
	if (str(inputtext) == "y" or "yes"):
		print("Hello World")
	elif (str(inputtext) == "n" or "no"):
			print("Bye World")
	else: 
			print("Not a correct input") 
			return getInput
def main():
	getInput()

if __name__=='__main__':
	main()