import pandas as pd 
import xlsxwriter as xw
import os
import glob

class ResultsToExcel:
    def __init__(self, path='/Users/dannymorgan/Desktop/ESPN/Final/Excel'):
        self.path = path
        self.file_path = '/Users/dannymorgan/Desktop/ESPN/Final/CSVs/'

        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.files = os.listdir(self.file_path)
        self.over_150 = self.files[0]
        self.standings_by_year = self.files[1]
        self.total_points = self.files[2]
        self.low_score = self.files[3]
        self.points_allowed = self.files[4]
        self.record_vs_opponent = self.files[5]
        self.under_100 = self.files[6]
        self.total_record = self.files[7]
        self.high_score = self.files[8]
        self.listed = [self.over_150, self.standings_by_year, self.total_points, self.low_score, self.points_allowed, self.record_vs_opponent, self.under_100, self.total_record, self.high_score]
        self.csv_to_excel()  
        
    def csv_to_excel(self,):
        writer = pd.ExcelWriter('ff_results_2018_2020.xlsx')
        for item in self.listed:
            sheet_name = item[0:-4]
            new_path = self.file_path + item
            pd.read_csv(new_path).to_excel(writer, sheet_name, index=False)
        writer.save()
            



    

if __name__ == '__main__':
    excel = ResultsToExcel()
