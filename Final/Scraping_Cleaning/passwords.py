class Password:
    def __init__(self):
        self.username = 'danny-morgan'
        self.password = 'Dmo06071993'
        self.redshift_link = '@fantasy-football.cclwwhkm0ay1.us-east-1.redshift.amazonaws.com:5439/dev'
        self.email = 'djmorgan@udel.edu'
        self.espn_password = 'Knicks12'
        self.league_id = '&leagueId=1016052'
        self.scoreboard_url = 'https://fantasy.espn.com/football/league/scoreboard?seasonId='
        self.season_id = '?seasonId='
        self.standings_url = 'https://fantasy.espn.com/football/league/standings?seasonId='
        self.weekly_url = '&mSPID='
        self.matchup_period = '&matchupPeriodId='
        self.weekly = 'https://fantasy.espn.com/football/league/scoreboard?seasonId=2019&leagueId=1016052&matchupPeriodId=7&mSPID=7'
        self.league_url = 'https://fantasy.espn.com/football/league?leagueId=1016052'

if __name__ == '__main__':
    password = Password()
