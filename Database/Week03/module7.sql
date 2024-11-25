
/* join query without table join  */

SELECT employees.employee_name, departments.department_name
FROM employees, departments
WHERE employees.department_id = departments.department_id;

/* join query with table join  */

SELECT employees.employee_name, departments.department_name
FROM employees
JOIN departments ON employees.department_id = departments.department_id;



/* join query with table join alias name  */



SELECT e.employee_name, d.department_name
FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id;

/* join query with table  */

SELECT EMPLOYEES.FIRST_NAME, DEPARTMENT_NAME
FROM EMPLOYEES
JOIN DEPARTMENTS USING (DEPARTMENT_ID);

/* cross join  */

SELECT p.product_name, c.color_name
FROM products AS p
CROSS JOIN colors AS c;

SELECT p.product_name, c.color_name
FROM products AS p, colors AS c;



/* SQL Query for Self-Join: */



SELECT e1.employee_name AS Employee, e2.employee_name AS Manager
FROM employees AS e1
LEFT JOIN employees AS e2
ON e1.manager_id = e2.employee_id;




SELECT e1.employee_name AS Employee, e2.employee_name AS Manager
FROM employees AS e1
INNER JOIN employees AS e2
ON e1.manager_id = e2.employee_id;


SELECT e1.employee_name AS Employee, e2.employee_name AS Manager
FROM employees AS e1
LEFT JOIN employees AS e2
ON e1.manager_id = e2.employee_id
ORDER BY e1.manager_id;



/* more join query  */


SELECT DEPARTMENTS.DEPARTMENT_NAME
FROM DEPARTMENTS
    LEFT JOIN EMPLOYEES
        ON DEPARTMENTS.DEPARTMENT_ID = EMPLOYEES.DEPARTMENT_ID
WHERE EMPLOYEES.DEPARTMENT_ID IS NULL;



SELECT EMPLOYEES.FIRST_NAME, 
EMPLOYEES.SALARY, 
((SELECT AVG(SALARY) FROM EMPLOYEES WHERE DEPARTMENT_ID = EMPLOYEES.DEPARTMENT_ID) - EMPLOYEES.SALARY) AS LESS_SALARY
FROM EMPLOYEES
JOIN DEPARTMENTS
ON EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID;



SELECT DEPARTMENT_NAME, MIN(SALARY), AVG(SALARY)
FROM EMPLOYEES
	JOIN DEPARTMENTS
		ON  EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID
GROUP BY DEPARTMENT_NAME
HAVING MIN(SALARY) > 5000;



