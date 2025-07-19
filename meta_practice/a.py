/* Write your PL/SQL query statement below */
with cte as (
    select
        experience
        ,salary
        ,sum(salary) over ( partition by experience order by salary ) cum_sum
    from
        Candidates

)
select experience,count(1) accepted_candidates from cte
where experience = 'Senior' and cum_sum <=70000
group by experience
union
select experience,count(1) accepted_candidates from cte
where experience = 'Junior' and cum_sum <=( select 70000 - nvl(max(cum_sum),0) from cte where experience='Senior' and cum_sum <=70000  )
group by experience
