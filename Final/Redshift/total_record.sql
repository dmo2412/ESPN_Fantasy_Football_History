with t as (
 select *
 from points
)
select p.player, count(p.player) as wins, count(distinct p.season) * 13 - wins as losses
from schedule s
join points p on p.player = s.player and p.season = s.season and p.week = s.week
join t on t.player = s.opponent and t.season = p.season and t.week = p.week
where p.score > t.score
group by p.player
order by wins desc
       
