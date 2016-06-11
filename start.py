import threading
import time
import flask_server
import systeminfo

exitFlag = 0
#flaskObj=flask_server.main()

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
	if (self.threadID == 1):
            #sysinfo()
	    while True:
	        systeminfo.main()
        else:
            flask_server.main()
	print "Exiting " + self.name

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


# Create new threads
thread1 = myThread(1, "System Information Thread", 1)
thread2 = myThread(2, "Flask Server", 2)

# Start new Threads
thread1.start()
time.sleep(2)
thread2.start()

print "Exiting Main Thread"
