import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from result_data import *
from passwords import *


class ImportExcelToDF:
    def __init__(self):
        self.table_names = ['Schedule', 'Scores']
        self.redshift_names = ['opponent', 'points']
        
        convert = Result()
        self.schedule = convert.schedule
        self.scores = convert.scores

        self.path = '/Users/dannymorgan/Desktop/ESPN/Final/CSVs/'
        self.file_name = 'fantasy_football_history'
        self.result_dicts = [self.schedule, self.scores]

        password = Password()
        self.username = password.username
        self.password = password.password
        self.redshift_link = password.redshift_link
        
        self.import_2020()
        self.create_df()
        print('Complete Dataframe')


    def import_2020(self):
        i = 0
        while i < len(self.table_names):
            self.data_xls = pd.read_excel(self.path + '/' + self.file_name, self.table_names[i], index_col=None)
            print('Completed pandas read excel')
            self.data_xls.to_csv('CSV/' + self.table_names[i] + '.csv', encoding='utf-8')
            i += 1
        print('Completed import')
    
    def create_df(self):
        i = 0
        for table in self.result_dicts:        
            df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in table.items()]))
            self.to_redshift_test(df,i)
            i += 1
        print("Complete create_df")
            

    def to_redshift_test(self,df,i):
        conn = create_engine(
            'postgresql://' + self.username + ":" + self.password + self.redshift_link)
        print('Complete conn create engine')
        df.to_sql(self.redshift_names[i], conn, index=False, if_exists='replace')
        print('Complete redshift' + str(i))




if __name__ == '__main__':
    imp = ImportExcelToDF()



