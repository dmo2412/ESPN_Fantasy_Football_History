select player, max(score) as high_score
from points
group by player
order by high_score desc