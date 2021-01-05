from collections import defaultdict
from clean import *




class Result:
    def __init__(self,):
        clean = Clean()
        self.teams = clean.teams
        self.schedule = clean.schedule
        self.real_scores = clean.real_scores
        

        self.named_schedule = defaultdict(list)
        self.updated_sch = defaultdict(list)
        self.final_schedule = defaultdict(list)
        self.scores = defaultdict(list)

        self.clean_teams()
        self.clean_sch_values()
        self.clean_sch_keys()
        self.replace_team()
        self.replace_name_key()
        self.set_final_schedule()
        self.set_scores()
        print('Completed Result')
        # print("self.named_schedule: ")
        # print(self.named_schedule)
        # print("  ")
        # print("  ")
        # print("self.final_schedule: ")
        # print(self.final_schedule)

        print(self.final_schedule == self.named_schedule)


    def set_scores(self,):
        for k,v in self.real_scores.items():
            self.scores[k].append(v[0:13])
            self.scores[k].append(v[13:26])
            self.scores[k].append(v[26:])

    def set_final_schedule(self,):
        for k,v in self.named_schedule.items():
            if len(v) == 1:
                self.final_schedule[k].append(v[0][0:13])
                self.final_schedule[k].append(v[0][13:26])
                self.final_schedule[k].append(v[0][26:])
            elif len(v) == 2:
                if len(v[0]) > len(v[1]):
                    self.final_schedule[k].append(v[0][0:13])
                    self.final_schedule[k].append(v[0][13:])
                    self.final_schedule[k].append(v[1])
                else:
                    self.final_schedule[k].append(v[0])
                    self.final_schedule[k].append(v[1][0:13])
                    self.final_schedule[k].append(v[1][13:])
            else:
                self.final_schedule[k] = v
        


    def replace_name_key(self,):
        for k,v in self.updated_sch.items():
            for name, teams in self.teams.items():
                if k in teams:
                    self.named_schedule[name].append(v)
        



    def replace_team(self,):
        for sch_team_name, sch_schedule in self.schedule.items():
            i = 0
            while i < len(sch_schedule):
                for real_name, team_names in self.teams.items():
                    if sch_schedule[i] in team_names:
                        self.updated_sch[sch_team_name].append(real_name)
                i += 1
        
        

    
    def clean_teams(self,):
        for k,v in self.teams.items():
            i = 0
            while i < len(v):
                if "(" in v[i]:
                    idx = v[i].find("(")
                    name = v[i][0:idx] + v[i][idx+1] + v[i][idx+3:]
                    self.teams[k][i] = name
                i += 1

    def clean_sch_values(self,):
        for k,v in self.schedule.items():
            i = 0
            while i < len(v):
                if "(" in v[i]:
                    idx = v[i].find("(")
                    name = v[i][0:idx] + v[i][idx+1] + v[i][idx+3:]
                    self.schedule[k][i] = name
                i += 1
    
    def clean_sch_keys(self,):
        arr = []
        for k,v in self.schedule.items():
            if "(" in k:
                idx = k.find("(")
                arr.append(k)
        
        for name in arr:
            idx = name.find("(")
            team = name[0:idx] + name[idx+1] + name[idx+3:]
            self.schedule[team] = self.schedule.pop(name)
        


if __name__ == '__main__':
    result = Result()
