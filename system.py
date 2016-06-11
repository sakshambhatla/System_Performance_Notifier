import os
import re
import time
while True:
    df_out = os.popen("df .").readlines()
    #print dir[1]
    df_out = ''.join(df_out[1])
    temp=df_out.split(' ');
    temp2=temp[9].split('%')
    print temp2[0]
    time.sleep(2)
    #matchObj = re.match( r'.*\s+([0-9]+)\%.*', dir, re.M|re.I)
    #matchObj = re.match('.*(\d+)\%.*', dir, re.M|re.I)
    #print dir
    #print "object match is - ", matchObj.group()
