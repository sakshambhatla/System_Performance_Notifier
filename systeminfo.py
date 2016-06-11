import os
import re
import time
import sqlClass

sqlObj = sqlClass.sqlClass()
sqlObj.createTable()
usage=10.5
sqlObj.insertEntry(usage)


def main():
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

if __name__ == '__main__':
    main()
