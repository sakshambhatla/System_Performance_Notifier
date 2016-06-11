import MySQLdb
import time


class sqlClass:
    '''Handles all DB communication.'''
    def __init__(self):
        '''Open DB connection.'''
        self.db = MySQLdb.connect("localhost","root","root","SYSTEM_MONITOR" )
        self.cur = self.db.cursor()
        print "connected to db"

    def dropTable(self):
        # Drop table if it already exist using execute() method.
        self.cur.execute("DROP TABLE IF EXISTS CPU")
        print "dropping table if existed"

    def __del__(self):
        print "shutting down db"
        self.db.close()

    def executeCmd(self, query):
        try:
            # Execute the SQL command
            self.cur.execute(query)
            # Commit your changes in the database
            self.db.commit()
        except:
            # Rollback in case there is any error
            print "rolling back. Error!"
            self.db.rollback()


    def createTable(self):
        '''Create table as per requirement'''
        query = """CREATE TABLE CPU (
        ID_NO  INT NOT NULL,
        TIME_DATA TIMESTAMP,
        USE_PERCENT FLOAT );"""
        self.executeCmd(query)

    def insertEntry(self,id_no, usage):
        self.time_stamp = time.strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO CPU (ID_NO, TIME_DATA, USE_PERCENT) VALUES ('%s', '%s', '%s');" \
                  %(int(id_no), self.time_stamp, int(usage))
        self.executeCmd(query)

    def readAll(self):
        query = "SELECT * FROM CPU";
        self.cur.execute(query)
        self.data=self.cur.fetchall()
        print self.data
        return self.data

