# app.py

# Import Flask and MySQL
from flask import Flask, render_template
from flask_mysqldb import MySQL
from config import DB_CONFIG

# Initialize Flask
app = Flask(__name__)
app.config['MYSQL_HOST'] = DB_CONFIG['host']
app.config['MYSQL_USER'] = DB_CONFIG['user']
app.config['MYSQL_PASSWORD'] = DB_CONFIG['password']
app.config['MYSQL_DB'] = DB_CONFIG['database']

# Initialize MySQL
mysql = MySQL(app)

# Get authors data
def get_authors_data() -> list :
    cur = mysql.connection.cursor()
    cur.execute('CALL get_authors()')
    data = cur.fetchall()
    cur.close()
    return data

# Get posts data
def get_posts_data() -> list :
    cur = mysql.connection.cursor()
    cur.execute('CALL get_posts()')
    data = cur.fetchall()
    cur.close()
    return data

# Routes
@app.route('/')
def index():
    return render_template('index.html', 
                           authors=get_authors_data(), 
                           posts=get_posts_data())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)