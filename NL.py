__author__ = "Ilyahoo Proshel"
__copyright__ = "Copyright 2017, IP"
__license__ = "GPL"
__version__ = "1.0."
__email__ = "irens@live.nl"


import os
import random
print("NL script v1.0")
print("For making some kind of folders inside folder.")
print()
#os.chdir("G://")
len = int(input("N of Length? "))
dirs = int(input("N of Folders? "))
msg = input("Ur msg inside wrong folders? ")

x=range(1,dirs+1)

for i in range(len):
	for j in range(dirs):
		os.mkdir(str(x[j]))
	f = random.randrange(1,dirs+1)
	for j in range(dirs):
		if j+1 is not f:
			os.chdir(".//"+str(j+1))
			ok = open(msg,'w')
			ok.close()
			os.chdir(".//..")
	os.chdir(".//"+str(f))
print(os.getcwd())