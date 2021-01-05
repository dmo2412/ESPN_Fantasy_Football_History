CREATE TABLE points
(
    id INTEGER,
    player VARCHAR(20),
    season INTEGER,
    week INTEGER,
    score DECIMAL(3,2)

 )
          
copy scores (id, player, season, week, score)
from 's3://espn-fantasy-football-stats/Scores.csv'
iam_role ''
csv 