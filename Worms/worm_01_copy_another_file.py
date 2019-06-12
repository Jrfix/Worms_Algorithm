import os
import shutil
import time

#change the directory
os.chdir("/root/LAB/Worms/")

#limit of your worms
x = 1

#infinite loop
while(1):
	print("Total "+str(x)+" Worms created.")
	
	#copy sample.txt but you can perform any action
		
	shutil.copy("sample.txt","sample"+str(x)+".txt")
	x += 1

	#add delay 2s
	time.sleep(2)
