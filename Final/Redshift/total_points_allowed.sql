with t as (
 select *
 from points
)
select p.player, sum(t.score) as points_allowed
from schedule s 
join points p on p.player = s.player and p.season = s.season and p.week = s.week
join t on t.player = s.opponent and t.season = p.season and t.week = p.week
group by p.player
order by points_allowed desc