# Fantasy Football History
Fantasy Football History goes through the history of an ESPN fantasy football league and scrapes all scores and standings and then cleans the data and organizes it into dictionaries. The dictionaries are then converted into CSV files which get uploaded to AWS S3, and ultimately into a redshift database. In redshift, several queries are done and the results are then uploaded to an excel file for readability.


### Table of Contents
- [Fantasy Football History](#fantasy-football-history)
    - [Table of Contents](#table-of-contents)
  - [Tech Stack](#tech-stack)
  - [Scraping](#scraping)
  - [Cleaning](#cleaning)
  - [Upload to S3](#upload-to-s3)
  - [Tables](#tables)
  - [Redshift](#redshift)
  - [Data Visualization](#data-visualization)
  - [Instructions To Run Fantasy Football History](#instructions-to-run-fantasy-football-history)



## Tech Stack
* Python (Pandas, Selenium, BeautifulSoup, OS, xlsxwriter, Boto3, time)
* AWS (S3, Redshift)

## Scraping
The scrape file uses Selenium webdriver to direct chrome to ESPN's fantasy football page. It starts by going to the standings page to collect the players real name, along with their team name from every year and pulls this data into a dictionary. It then iterates over every week within every season to collect the scores and opponent for each team and pulls this info into two seperate dictionaries. The schedule dictionary has a key of the players team name and a value of a list of all opponents. The scores dictionary has a key of the players team name and a value of a list of all of their scores throughout the season.

## Cleaning
The clean file calls scrape.py and sets variables equal to the resulting dictionaries from scrape.py. The clean file then iterates over the dictionaries to remove special characters and unwanted spaces, which is eventually called by the result_data file. The result_data file then creates a new dictionary, combining the names and opponents dictionary to replace all team names with the players real name: 
`teams = {"Danny": ["Last Dan Standing", "Last Dan Standing"...]...}, schedule = {Last Dan Standing: [["Cooked to perfection", "Dak to the future"....], [....], [....]]}`
These dictionaries are then merged to use real names because many users have different names every year: 
Result_schedule = {"Danny" :[[Andrew, Tim, Mark...],[..],[..]]}
The same thing is done with the scores dictionary to change the team name to real name.

## Upload to S3
The resulting dictionaries from above are then converted into a CSV file which is eventually uploaded to AWS S3 using boto3 and dotenv.


## Tables
schedule table:
id | player | season | week | opponent 
--- | --- | --- | --- |--- 
0 | Billy | 2020 | 1 | Danny 

points table:

id | player | season | week | score 
--- | --- | --- | --- |--- 
0 | Billy | 2020 | 1 | 107.34

## Redshift
A cluster is created in redshift, which is then used to convert the CSV file into tables that can then be queried. Several queries were run to compare both cumulative stats, as well as performing comparisons between each team. The results of these queries can be found in /Final/Excel/ff_results_2018_2020.xlsx. The queries can be found in /Final/Redshift. Sample query to compare each players record vs every other player over all seasons.
```sql
with t as (
 select s.player, p.score, s.opponent, p.season, p.week
 from schedule s
  join points p on p.player = s.player and p.season = s.season and p.week = s.week
)
select s.player as home_player, s.opponent as away_player, 
(select case count(home_player)
    when count(s.player) > 0 then count(s.player)
    else 0
    end
        from schedule s
        left outer join points p on p.player = s.player and p.season = s.season and p.week = s.week
        left outer join t on t.player = s.opponent and t.season = p.season and t.week = p.week
        where home_player = s.player and away_player = s.opponent and t.score < p.score
        group by home_player, away_player
        ) as wins,
 (select case count(s.player)
 when count(s.player) > 0 then count(s.player)
 else 0
 end
 from schedule s
 left outer join points p on p.player = s.player and p.season = s.season and p.week = s.week
 left outer join t on t.player = s.opponent and t.season = p.season and t.week = p.week
 where home_player = s.player and away_player = s.opponent and t.score > p.score
 group by home_player, away_player) as losses                           
from schedule s
join points p on p.player = s.player and p.season = s.season and p.week = s.week
join t on t.player = s.opponent and t.season = p.season and t.week = p.week
group by home_player, away_player
order by home_player asc, wins desc
```
Result: 

home_player | away_player | wins | losses 
--- | --- | --- | --- 
Billy | Danny | 2 | 4

## Data Visualization
*jahddhkj

## Instructions To Run Fantasy Football History
1. git clone https://github.com/dmo2412/Fantasy_Football_History
2. In `/Final/Scraping_Cleaning/scrape.py`: 
 * Change path
 * Path to webdriver
 * desired number of years and weeks
 * Input your league_id, and weekly_url
 * Append your name and team names for all years into self.teams
3. In `/Final/Scraping_Cleaning/clean.py`: 
 * Change path
4. Create S3 bucket and redshift cluster
5. In `/Final/Scraping_Cleaning/file_manager.py`:
 * Change names in csv_names to the names of your csv
6. Add a `passwords.py` file in `/Final/Scraping_Cleaning/`:
 * class Password: Add your aws username, password, and redshift link, and add to .gitignore
    ```py 
    def __init__(self):
        self.username = ''
        self.password = ''
        self.redshift_link = ''
   ```

* if __name__ == '__main__':
    password = Password()
7. Terminal:
 * python3 to_dataframe.py
 * python3 file_manger.py
 






