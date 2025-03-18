-- Выборка самых молодых жителей по странам в виде представления
--12337846534785
create view the_oldest_people_by_countries (fio, age,dob,country_name) as

with rn_cte as (select name, age, dob, country_id, row_number() over (partition by country_id order by dob) rn
				from people)

select rn.name, rn.age, rn.dob, ct.name
from rn_cte rn join countries ct on rn.country_id = ct.id 
where rn.rn = 1;