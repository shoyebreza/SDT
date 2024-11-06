
/* sub query */


SELECT username,
       (SELECT COUNT(*)
        FROM orders
        WHERE orders.user_id = users.id) AS total_orders
FROM users;


SELECT username
FROM users
WHERE id IN (SELECT user_id 
              FROM orders 
              GROUP BY user_id 
              HAVING COUNT(*) > 5);


SELECT user_id, AVG(total_amount) AS average_order_amount
FROM (SELECT user_id, SUM(amount) AS total_amount
      FROM orders
      GROUP BY user_id) AS user_totals
GROUP BY user_id;




SELECT username
FROM users u
WHERE (SELECT AVG(amount) 
       FROM orders 
       WHERE user_id = u.id) > 100;




SELECT username
FROM users u
WHERE EXISTS (SELECT 1 
              FROM orders 
              WHERE user_id = u.id);


select avg(salary)
from employees
where department_id = (
		select department_id
		from departments
                where department_name = 'MARKETING'
		);



select max(salary)
from employees
where salary<(
            select max(salary)
            from employees
);


select salary
from employees
where salary=(
            select distinct salary
            from employees
            order by salary desc
            limit 1
            offset 1
);


/* CTE */

with TempTable as(
select * from employees
where salary > 15000
)    select avg(salary)
     from TempTable; 



with MktMaxTbl as(
    select max(salary) as MktMax
    from employees
    where department_id=20
    ),
    ItAvgTbl as(
    select avg(salary) as ItAvg
    from employees
    where department_id=60
    )
select * from employees
where    salary > (select ItAvg from ItAvgTbl) 
            and 
        salary < ( select MktMax from MktMaxTbl );


