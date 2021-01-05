with t as (
 select *
 from points
)
select s.player as person, s.season as seasons, count(s.player) as wins, 13 - wins as losses, (select sum(t.score)
                                                                                                from schedule s
                                                                                                join points p on p.player = s.player and p.season = s.season and p.week = s.week
                                                                                                join t on t.player = s.opponent and t.season = p.season and t.week = p.week
                                                                                                where t.season = seasons and t.player = person
                                                                                                group by t.player) as total_points
from schedule s
join points p on p.player = s.player and p.season = s.season and p.week = s.week
join t on t.player = s.opponent and t.season = p.season and t.week = p.week
where p.score > t.score
group by s.player, s.season
order by seasons desc, wins desc, total_points desc