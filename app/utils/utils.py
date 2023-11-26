import datetime
from datetime import date

class Utils():
    def clean_dataset(self,df):
        trim_strings = lambda x: x.strip() if isinstance(x, str) else x
        return df.applymap(trim_strings)
    def format_datetime(self, dt):
            if str(dt).__contains__('T'):
                 dt = dt.replace('T',' ')
            if str(dt).endswith('Z'):
                dt = dt[:-1]
            return dt
    def apply_datetime_format(self, df, column_name):
        df[column_name] = df[column_name].apply(self.format_datetime)
        return df