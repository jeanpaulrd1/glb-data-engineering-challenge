from db.db_connection import MySQLConnection
import pandas as pd
import utils.utils as u

class GenericService():   
    def loadData(self, uploaded_file, col_names, table_name):
        try:
            util = u.Utils()
            engine = MySQLConnection.create_connection()
            fileName = uploaded_file.filename
            df = pd.read_csv(uploaded_file,names=col_names, header=None)
            
            df['upload_file_name'] = fileName
            df = util.clean_dataset(df)
            if table_name == 'hired_employees':
                df = util.apply_datetime_format(df, "hired_date")
            if fileName != '':
                df.to_sql(table_name, con=engine, if_exists='append', index=False, chunksize= 1000)
                response_object = {
                    'status':'sucess',
                    'message':f'{table_name} data loaded successfully.'
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