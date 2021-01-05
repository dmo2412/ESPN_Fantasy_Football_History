select player, count(score) as over_150
from points
where score >150
group by player
order by over_150 desc