create table schedule ( 
    id INTEGER,
    player varchar(20),
    season INTEGER,
    week INTEGER,
    opponent varchar(20)
)

copy schedule (id, player, season, week, opponent)
from 's3://espn-fantasy-football-stats/Schedule.csv'
iam_role ''
csv 