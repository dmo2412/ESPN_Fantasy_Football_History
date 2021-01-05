from collections import defaultdict
from scrape import *
from xlsxwriter import Workbook
import xlsxwriter as xw
import os

class Clean:
    def __init__(self, path='/Users/dannymorgan/Desktop/ESPN/Excel'):

        if not os.path.exists(path):
            os.mkdir(path)

        self.path = path
        
        data = AllData()
        
        self.teams = data.teams
        self.schedule = data.team_schedules
        self.real_scores = data.scores
        
        self.clean_schedule()
        self.yearly_schedule = defaultdict(list)
        self.team_set()
        self.check_schedule()
        
        self.updated_sch = defaultdict(list)
        self.result_sch = defaultdict(list)
        
        self.update()
        self.result()
        print('Completed Clean')
        # print(self.schedule)

    def team_set(self,):
        for k,v in self.teams.items():
            i = 0
            while i < len(v):
                if v[i] in v[0:i] or v[i] in v[i+1:]:
                    self.teams[k].pop(i)
                i += 1

            

    def result(self,):
        for k,v in self.updated_sch.items():
            for name, teams in self.teams.items():
                if k in teams:
                    self.result_sch[name].append(v)
                


    def update(self,):
        for k,v in self.schedule.items():
            if len(v) == 13:
                self.updated_sch[k].append(v)
            elif len(v) == 26:
                self.updated_sch[k].append(v[0:13])
                self.updated_sch[k].append(v[13:])
            elif len(v) == 39:
                self.updated_sch[k].append(v[0:13])
                self.updated_sch[k].append(v[13:26])
                self.updated_sch[k].append(v[26:])
        

    def clean_schedule(self,):
        arr = []
        for k,v in self.schedule.items():
            i = 0
            while i < len(v):
                if v[i][-1] == " ":
                    self.schedule[k][i] = v[i][0:-1]
                i += 1
            if k[-1] == " ":
                arr.append(k)

        for name in arr:
            self.schedule[name[0:-1]] = self.schedule.pop(name)
        
        
        


    def check_schedule(self,):
        temp = defaultdict(list)

        for real_name, team_name in self.teams.items():
            for team_sch, opp in self.schedule.items():
                if team_sch in team_name:
                    temp[real_name].append(opp)

        for real_name, team in temp.items():
            if len(team) == 1:
                first = team[0][0:13]
                second = team[0][13:26]
                third = team[0][26:]
                self.yearly_schedule[real_name].append(first)
                self.yearly_schedule[real_name].append(second)
                self.yearly_schedule[real_name].append(third)
            elif len(team) == 2:
                if len(team[0]) == 26:
                    first = team[0][0:13]
                    second = team[0][13:]
                    third = team[1]
                    self.yearly_schedule[real_name].append(first)
                    self.yearly_schedule[real_name].append(second)
                    self.yearly_schedule[real_name].append(third)
                elif len(team[1]) == 26:
                    first = team[0]
                    second = team[1][0:13]
                    third = team[1][13:]
                    self.yearly_schedule[real_name].append(first)
                    self.yearly_schedule[real_name].append(second)
                    self.yearly_schedule[real_name].append(third)
            else:
                self.yearly_schedule[real_name].append(team[0])
                self.yearly_schedule[real_name].append(team[1])
                self.yearly_schedule[real_name].append(team[2])
    
    def write_data(self,):
        workbook = xw.Workbook(os.path.join(self.path, self.file_name))
        worksheet = workbook.add_worksheet()
        years = ['2018', '2019', '2020']

        col = 0

        for name, teams in self.teams.items(): 
            worksheet.write(0, col, name)
            row = 1
            for team in teams:
                worksheet.write(row, col, team)
                row += 1
            col += 1
        
        # workbook.close()
        worksheet2 = workbook.add_worksheet()
        worksheet3 = workbook.add_worksheet()

        worksheet2.write(0,0,"Player")
        worksheet2.write(0,1, 'Year')
        worksheet3.write(0,0,"Player")
        worksheet3.write(0,1, 'Year')
        column = 2
        for week in range(1,14):
            worksheet2.write(0, column, 'Week_' + str(week))
            worksheet3.write(0, column, 'Week_' + str(week))
            column += 1
        # workbook.close()

        year_i = 0
        row = 1
        col = 0
        team_col = 2
        team_row = 1


        for name, schedule in self.yearly_schedule.items():
            i = 0
            for team in schedule:
                worksheet2.write(row, 0, name)
                worksheet2.write(row, 1, years[i])
                team_col = 2
                for opp in team:
                    worksheet2.write(team_row, team_col, opp)
                    team_col += 1
                row += 1
                i += 1
                team_row += 1
        
        # workbook.close()

        column = 2
        row = 1
        


        for name, score in self.real_scores.items():
            
            i = 0
            worksheet3.write(row,0, name)
            worksheet3.write(row+1,0, name)
            worksheet3.write(row+2,0, name)
            worksheet3.write_number(row,1, 2018)
            worksheet3.write_number(row+1,1, 2019)
            worksheet3.write_number(row+2,1, 2020)
            while i < 13:
                worksheet3.write_number(row,column, score[i])
                worksheet3.write_number(row+ 1,column, score[i+13])
                worksheet3.write_number(row+2,column, score[i+26])
                i += 1
                column += 1
            row += 3
            column = 2
        
        workbook.close()




        




if __name__ == '__main__':
    clean = Clean()
