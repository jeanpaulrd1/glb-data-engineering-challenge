from db.db_connection import MySQLConnection
import pandas as pd
from json import loads, dumps
import json
class ReportService():   
    def readData(self, sql_path):
        try:
            engine = MySQLConnection.create_connection()
            conn = engine.connect()
            data = pd.read_sql(open(sql_path).read(), conn)
            json_data = data.to_json(orient="records")
            json_data = json.loads(json_data)
            response_object = response_object = {
                    'status':'sucess',
                    'data':json_data
                }
            return response_object,200
        except Exception as e:
            response_object = {
                'status':'fail',
                'message':'An error ocurred: ' + str(e) 
            }
            return response_object, 400
        finally:
            engine.dispose()