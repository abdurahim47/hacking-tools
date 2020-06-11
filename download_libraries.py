import os

def down(lib):
	lib = lib.strip(r"(,)\"\',[,],{,}")
	lib = lib.lower().split()
	os.system("pip install --upgrade pip")
	for i in lib:
		os.system("pip3 install " + str(i))

def question():
	lib = input("Which Library Do You Want to Download: ")
	down(lib)

question()
