select player, min(score) as low_score
from points
group by player
order by low_score 