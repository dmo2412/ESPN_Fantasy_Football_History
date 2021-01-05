from collections import defaultdict
from xlsxwriter import Workbook
import xlsxwriter as xw
import os
from result_data import *

class ToExcel:
    def __init__(self, path='/Users/dannymorgan/Desktop/ESPN/Excel'):
        if not os.path.exists(path):
            os.mkdir(path)
        self.path = path
        rez = Result()
        self.schedule = rez.final_schedule
        self.scores = rez.scores
        self.file_name = 'fantasy_football_history'
        self.seasons = [i for i in range(2018,2021)]

        self.write_schedule()
        

    def write_schedule(self,):
        workbook = xw.Workbook(os.path.join(self.path, self.file_name + '.xlsx'))
        worksheet = workbook.add_worksheet('Schedule')

        headers = ['Player', 'season', 'week', 'opponent']


        player = 0
        season = 1
        week = 2
        opponent = 3
        row = 0
        x = 0
        j = 0
        while x < len(self.seasons):
            for k,v in self.schedule.items():
                i = 0
                while i < len(v[0]):
                    worksheet.write(row, player, k)
                    worksheet.write_number(row, season, self.seasons[x])
                    worksheet.write_number(row,week,i+1)
                    worksheet.write(row, opponent, v[j][i])
                    i += 1
                    row += 1
            x += 1
            j += 1

        self.write_scores(workbook)
        workbook.close()

    def write_scores(self,workbook):
        headers = ['Player', 'season', 'week', 'score']
        worksheet = workbook.add_worksheet('Scores')

        player = 0
        season = 1
        week = 2
        score = 3
        
        row = 0
        x = 0
        j = 0

        while x < len(self.seasons):
            for k,v in self.scores.items():
                i = 0
                while i < len(v[0]):
                    worksheet.write(row,player, k)
                    worksheet.write_number(row, season, self.seasons[x])
                    worksheet.write_number(row, week, i+1)
                    worksheet.write_number(row, score,v[j][i])
                    i += 1
                    row += 1
            x += 1
            j += 1


        




if __name__ == '__main__':
    to_excel = ToExcel()

