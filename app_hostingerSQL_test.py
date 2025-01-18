import mysql.connector
from flask import Flask

app = Flask(__name__)

# Configuration for Hostinger MySQL
HOSTINGER_DB_HOST = "193.203.184.165"
HOSTINGER_DB_NAME = "u854837124_mediminder_db"
HOSTINGER_DB_USER = "u854837124_mediminder"
HOSTINGER_DB_PASSWORD = "mediMinder457!"

# Connect to MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host=HOSTINGER_DB_HOST,
        database=HOSTINGER_DB_NAME,
        user=HOSTINGER_DB_USER,
        password=HOSTINGER_DB_PASSWORD
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    data = cursor.fetchall()
    conn.close()
    return str(data)


# if __name__ == "__main__":
#     app.run(debug=True)