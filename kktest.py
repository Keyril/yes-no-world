#!/usr/local/bin/python

def getInput():
	inputtext = input("Would you like to run? (y/n):  ")
	giveResponse(inputtext)

def giveResponse(inputtext):
	if (str(inputtext) == "y"):
		print("Hello World")
	elif (str(inputtext) == "n"):
			print("Bye World")
	else: 
			print("Not a correct input") 
			return getInput
def main():
	print("its working")
	getInput()

if __name__=='__main__':
	main()