select player, sum(score) as total_points
from points
group by player
order by total_points desc