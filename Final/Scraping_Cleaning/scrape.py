from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
import os
from xlsxwriter import Workbook
import xlsxwriter as xw
from selenium.webdriver.common.action_chains import ActionChains
from collections import defaultdict
from passwords import *

class AllData:
    def __init__(self, path='/Users/dannymorgan/Desktop/ESPN/Excel'):
        if not os.path.exists(path):
            os.mkdir(path)
        
        # self.scores = defaultdict(list)
        
        self.path = path
        self.years = [str(i) for i in range(2018, 2021)]
        self.weeks = [str(i) for i in range(1, 14)]
        self.driver = webdriver.Chrome('/Users/dannymorgan/Downloads/chromedriver')
        password = Password()
        self.league_id = password.league_id
        self.scoreboard_url = password.scoreboard_url
        self.season_id = password.season_id
        self.standings_url = password.standings_url
        self.weekly_url = password.weekly_url
        self.matchup_period = password.matchup_period
        self.weekly = password.weekly
        self.league_url = password.league_url
        self.espn_password = password.espn_password
        self.email = password.email




        # self.league_id = '&leagueId=1016052'
        # self.scoreboard_url = 'https://fantasy.espn.com/football/league/scoreboard?seasonId='
        # self.season_id = '?seasonId='
        # self.standings_url = 'https://fantasy.espn.com/football/league/standings?seasonId='
        # self.weekly_url = '&mSPID='
        # self.matchup_period = '&matchupPeriodId='
        self.schedule_url = self.scoreboard_url + '2019' + self.league_id + self.matchup_period + '2' + self.weekly_url + '2'
        # self.weekly = 'https://fantasy.espn.com/football/league/scoreboard?seasonId=2019&leagueId=1016052&matchupPeriodId=7&mSPID=7'
        self.driver.get(self.league_url)
        
        sleep(15)
        self.login()
        sleep(10)
        self.driver.refresh()
        self.names = defaultdict(list)
        self.teams = defaultdict(list)
        self.team_schedules = defaultdict(list)
        self.scores = defaultdict(list)
        for i in range(3):
            self.teams['Danny Morgan'].append('Last Dan Standing')
        
        self.get_years()

        print(self.names)
        print(" ")
        print(" ")
        print(self.team_schedules)
        
        
        print('Completed Data')
        # print(self.teams)

    def login(self,):
        self.driver.switch_to.frame("disneyid-iframe")
        self.driver.find_element_by_css_selector(
            "input[type = 'email']").send_keys(self.email)
        self.driver.find_element_by_css_selector(
            "input[type = 'password']").send_keys(self.espn_password)
        login = self.driver.find_element_by_xpath(
            "//button[@class='btn btn-primary btn-submit ng-isolate-scope']")
        login.click()
        sleep(10)
        self.driver.switch_to.default_content()
        sleep(3)


    def get_years(self,):
        for year in self.years:
            self.driver.get(self.standings_url + year + self.league_id)
            sleep(3)
            self.get_names(year)

        for year in self.years:
            self.get_schedule(year)

    def get_names(self, year):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        players = soup.find_all(class_="jsx-2810852873 table--cell team__column")

        if len(players) > 9:
            players = players[9:]

        for player in players:
            player = str(player)
            player_start = player.find(' (') + 2
            player_finish = player.find('><div class="jsx-2302882246') - 2
            team_start = player.find('team__column"') + 20
            team = player[team_start+1:player_start-2]

            if team[-1] == " ":
                team = team[0:-1]
            
            name = player[player_start:player_finish]
            
            self.teams[name].append(team)
        
        
    def get_schedule(self, year):
        for week in self.weeks:
            self.driver.get(self.scoreboard_url + year + self.league_id + self.matchup_period + week + self.weekly_url + week)
            sleep(2)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            members = soup.find_all(class_="ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db")
            scores = soup.find_all(class_="ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2")
            players = self.get_player()
            i = 0
            
            while i < len(players):
                if i % 2 == 0:
                    opp = players[i+1]
                else:
                    opp = players[i-1]
                
                score = str(scores[i])
                
                start = score.find('title="') + 7
                end = score.find(' points')
                score = float(score[start:end])
                person = players[i]
                for k,v in self.teams.items():
                    x = 0
                    if person[-1] == " ":
                        person = person[0:-1]
                    
                    for name in v:
                        if name[-1] == " ":
                            name == name[0:-1]

                    if person in v:
                        self.scores[k].append(score)
                    else:
                        x += 1
                    if x == 10:
                        print(k)

                self.team_schedules[person].append(opp)
                i += 1
            

    def get_player(self,):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        members = soup.find_all(
            class_="ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db")

        players = []

        for ele in members:
            ele = str(ele)
            start = ele.find('">') + 2
            finish = ele.find('</div>')
            player = ele[start:finish]
            players.append(player)

        return players
            




if __name__ == '__main__':
    data = AllData()


