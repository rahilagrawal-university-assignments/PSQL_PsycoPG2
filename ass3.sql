-- COMP3311 19T3 Assignment 3
-- Helper views and functions (if needed)

create or replace view courseQuota(course, quota, enrolments) as
select s.code, c.quota, count(s.code) from courses c 
inner join subjects s on c.subject_id = s.id 
inner join terms t on t.id = c.term_id 
inner join course_enrolments ce on ce.course_id = c.id 
where t.name='19T3' and c.quota > 50 group by s.code, c.quota 
order by s.code;  

create or replace view courseDigits(subj, digits) as 
select SUBSTRING(code, 1,4), SUBSTRING(code, 5, 4) 
from subjects order by code;
