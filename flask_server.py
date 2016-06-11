from flask import Flask, url_for
from flask import jsonify
import MySQLdb
import sqlClass

import time    

sqlReadObj = sqlClass.sqlClass()

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/timestamp')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/timestamp/<timestamp_id>')
def api_article(timestamp_id):
    return 'You are at timestamp ' + timestamp_id

@app.route('/diskspace', methods = ['GET'])
def api_hello():
    '''
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    '''
    data=sqlReadObj.readAll()
    resp = jsonify(data)
    resp.status_code = 200

    return resp


def main():
    app.run()

if __name__ == '__main__':
    main()
