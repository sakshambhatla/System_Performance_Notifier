import threading
import time
import flask_server

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
            i=0
	    while (i <10):
	        systeminfo()
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


def systeminfo():
    i=0
    while i<100:
        print "222222222test threading!!!!!!!!!!!!!!!!!!!!!!!1"
        time.sleep(5)
        i=i+1

# Create new threads
thread1 = myThread(1, "System Information Thread", 1)
thread2 = myThread(2, "Flask Server", 2)
#t1=threading.Thread(target=flask_server.main)
#t2=threading.Thread(target=myfunc)
#t2.start()
#print "thread 1 started. thread 2 starting now."
#t1.start()


# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"
