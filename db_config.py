import psycopg2
import pgdb
class MedExDb(object):
    hostname = 'localhost'
    username = 'postgres'
    password = '1qazZAQ!'
    database = 'medexdb'
    def __init__(self, host, user, password, db_name):
        self.hostname = host
        self.username = user
        self.password = password
        self.database = db_name
    
    def db_query(conn):
        cur = conn.cursor()
        cur.execute( "SELECT name, price FROM drugs" )
        return cur

    def ps_connect():
        return pgdb.connect( host= hostname, user=username, password=password, database=database )
        
    def pg_connect():
        return pgdb.connect( host= hostname, user=username, password=password, database=database )

    def disconnect(conn):
        conn.close()
        
