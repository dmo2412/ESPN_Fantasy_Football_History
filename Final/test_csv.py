import pandas as pd
from sqlalchemy import create_engine
import psycopg2

class CreateCSV:
    def __init__(self, path='/Users/dannymorgan/Desktop/ESPN/Excel'):
        self.file_name = 'fantasy_football_history'
        self.path = path
        self.table_names = ['Schedule', 'Scores']
        self.names = ['sched', 'sco']
        self.convert_CSV()


    def convert_CSV(self,):
        i = 0
        while i < len(self.table_names):
            self.data_xls = pd.read_excel(self.path + '/' + self.file_name, self.table_names[i],index_col=None)
            self.data_xls.to_csv('CSV/' + self.names[i] + '.csv', encoding='utf-8')
            print(self.names[i])
            i += 1

if __name__ == '__main__':
    create = CreateCSV()