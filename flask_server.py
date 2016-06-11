from flask import Flask, url_for
from flask import jsonify
import MySQLdb
import sqlClass

import time    

sqlReadObj = sqlClass.sqlClass()
data=sqlReadObj.readAll()


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

