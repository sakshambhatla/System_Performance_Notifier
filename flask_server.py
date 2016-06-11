from flask import Flask, url_for
from flask import jsonify
import MySQLdb

import time    

time_string=time.strftime('%Y-%m-%d %H:%M:%S')

class sqlClass:
    '''Handles all DB communication.'''
    def __init__(self):
        '''Open DB connection.'''
        self.db = MySQLdb.connect("localhost","root","root","SYSTEM_MONITOR" )
        self.cur = self.db.cursor()
        print "connected to db"
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

    def insertEntry(self,usage):
	query = "INSERT INTO CPU (ID_NO, TIME_DATA, USE_PERCENT) VALUES (1, NOW(), '%s');" %usage
	self.executeCmd(query)
 
    def readAll(self):
	query = "SELECT * FROM CPU";
	self.cur.execute(query)
	data=self.cur.fetchall()
	print data
	return data

sqlObj = sqlClass()
sqlObj.createTable()
usage=10.5
sqlObj.insertEntry(usage)
data=sqlObj.readAll()

#TEST INPUT




app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

@app.route('/hello', methods = ['GET'])
def api_hello():
    '''
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    '''
    #js = json.dumps(data)

    #resp = Response(js, status=200, mimetype='application/json')
    resp = jsonify(data)
    resp.status_code = 200
    #resp.headers['Link'] = 'http://luisrei.com'

    return resp

#if __name__ == '__main__':
def main():
    app.run()
