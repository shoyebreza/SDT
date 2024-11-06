select * from employees order by salary asc;

select first_name, last_name,salary from employees order by salary desc limit 2,1;

select first_name, last_name,salary from employees order by salary ASC limit 2,1;

select first_name, last_name,salary from employees where salary < (select max(salary) as max_salary from employees) limit 1,1;

select max(salary) as max_salary from employees;

with hire as (select hire_date from employees where first_name='steven' or last_name='steven') select * from hire;



