select player, count(score) as under_100
from points
where score < 100
group by player
order by under_100 desc