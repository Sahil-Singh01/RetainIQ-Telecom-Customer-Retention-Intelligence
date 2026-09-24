from getpass import getpass
import pandas as pd
import mysql.connector

def get_config(database="retainiq"):
    return {"host":"localhost","port":3306,"user":"retainiq_user","password":getpass("Enter MySQL password for retainiq_user: "),"database":database}

def get_connection(database="retainiq"):
    return mysql.connector.connect(**get_config(database))

def run_query(query, params=None):
    connection=cursor=None
    try:
        connection=get_connection(); cursor=connection.cursor(dictionary=True); cursor.execute(query,params or ()); return pd.DataFrame(cursor.fetchall())
    finally:
        if cursor: cursor.close()
        if connection and connection.is_connected(): connection.close()
