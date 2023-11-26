from sqlalchemy import create_engine
from db.config import connection_string

class MySQLConnection():
    def create_connection():
        try:
            engine = create_engine(connection_string)
            return engine
        except Exception as e:
             raise Exception("Database connection error:"+ str(e))
        