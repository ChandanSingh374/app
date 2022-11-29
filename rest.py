import pymysql
from app import app
from db import mysql
from flask import jsonify

@app.route('/')
def users():
    conn = mysql.connect()
    
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "CREATE TABLE user (id INT NOT NULL PRIMARY KEY, name  VARCHAR(40), email VARCHAR(40))"
    cursor.execute(query)
    query = "INSERT INTO user (id, name, email) VALUES ('2222', 'Maria',  'mariaz@activestate.com')"
    cursor.execute(query)
    cursor.execute("SELECT * FROM user")
    
    rows = cursor.fetchall()
    
    resp = jsonify(rows)
    resp.status_code = 200
    
    return resp

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
