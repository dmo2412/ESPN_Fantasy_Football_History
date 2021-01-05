with t as (
 select s.player, p.score, s.opponent, p.season, p.week
 from schedule s
  join points p on p.player = s.player and p.season = s.season and p.week = s.week
)
select s.player as home_player, s.opponent as away_player, (select case count(home_player)
                                                            when count(s.player) > 0 then count(s.player)
                                                            else 0
                                                            end
                                                                from schedule s
                                                                left outer join points p on p.player = s.player and p.season = s.season and p.week = s.week
                                                                left outer join t on t.player = s.opponent and t.season = p.season and t.week = p.week
                                                                where home_player = s.player and away_player = s.opponent and t.score < p.score
                                                                group by home_player, away_player
                                                                ) as wins,
                                                                    (select case count(s.player)
                                                                    when count(s.player) > 0 then count(s.player)
                                                                    else 0
                                                                    end
                                                                    from schedule s
                                                                    left outer join points p on p.player = s.player and p.season = s.season and p.week = s.week
                                                                    left outer join t on t.player = s.opponent and t.season = p.season and t.week = p.week
                                                                    where home_player = s.player and away_player = s.opponent and t.score > p.score
                                                                    group by home_player, away_player) as losses                           
from schedule s
join points p on p.player = s.player and p.season = s.season and p.week = s.week
join t on t.player = s.opponent and t.season = p.season and t.week = p.week
group by home_player, away_player
order by home_player asc, wins desc


