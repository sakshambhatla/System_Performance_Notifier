import os
import time
import sqlClass

sqlObj = sqlClass.sqlClass()
sqlObj.dropTable()
sqlObj.createTable()

def main():
    id_no=1;
    while True:
        df_out = os.popen("df .").readlines()
        df_out = ''.join(df_out[1])
        temp=df_out.split(' ');
        usage=temp[9].split('%')
        print usage[0]
        time.sleep(2)
        sqlObj.insertEntry(id_no, str(usage[0]));
        id_no = id_no +1;

if __name__ == '__main__':
    print "running systeminfo main"
    main()
