

/* 1. UPPER and LOWER
These functions are used to convert strings to uppercase or lowercase, respectively.

Example:

Assuming you have a table named users with a column username. */


SELECT username, 
       UPPER(username) AS username_upper, 
       LOWER(username) AS username_lower 
FROM users;

/* 2. COUNT
This function counts the number of rows that match a specified condition.

To count the total number of users:*/

SELECT COUNT(*) AS total_users 
FROM users;
To count users with a specific condition (e.g., users from a specific city):

SELECT COUNT(*) AS total_users_in_city 
FROM users 
WHERE city = 'New York';

/* 3. SUM
This function adds up numeric values in a specified column.

Assuming you have a table named orders with a column amount: */

SELECT SUM(amount) AS total_sales 
FROM orders;
To get the total sales for a specific product:


SELECT SUM(amount) AS total_sales_for_product 
FROM orders 
WHERE product_id = 123;

/* Combining Functions
You can also combine these functions in a single query: */


SELECT 
    COUNT(*) AS total_users, 
    SUM(amount) AS total_sales 
FROM users 
JOIN orders ON users.id = orders.user_id 
WHERE LOWER(city) = 'los angeles';




/* aggregate functions 

Aggregate functions in MySQL are used to perform calculations on multiple rows of a table and return a single value. Here are some common aggregate functions along with examples: */

/* 1. COUNT() 
Counts the number of rows that match a specified condition.
*/


SELECT COUNT(*) AS total_orders 
FROM orders;

/* 2. SUM()
Calculates the total sum of a numeric column. */


SELECT SUM(amount) AS total_sales 
FROM orders;

/* 3. AVG()
Calculates the average value of a numeric column. */

SELECT AVG(amount) AS average_order_value 
FROM orders;

/* 4. MIN()
Finds the minimum value in a column.
 */

SELECT MIN(amount) AS lowest_order_value 
FROM orders;


/* 5. MAX()
Finds the maximum value in a column.
 */
SELECT MAX(amount) AS highest_order_value 
FROM orders;


/* Using GROUP BY with Aggregate Functions
You can use aggregate functions with the GROUP BY clause to group results by one or more columns. */

SELECT product_id, SUM(amount) AS total_sales 
FROM orders 
GROUP BY product_id;


/* Combining Multiple Aggregate Functions
You can also combine multiple aggregate functions in a single query.
 */
SELECT 
    COUNT(*) AS total_orders, 
    SUM(amount) AS total_sales, 
    AVG(amount) AS average_order_value 
FROM orders;

/* Filtering with HAVING
When you want to filter results based on aggregate values, you can use the HAVING clause. */

SELECT product_id, SUM(amount) AS total_sales 
FROM orders 
GROUP BY product_id 
HAVING total_sales > 1000;



/* Scalar function 

In MySQL, scalar functions are functions that operate on a single value and return a single value. They can be used in SQL expressions, allowing for manipulation or transformation of data on a row-by-row basis. Here are some common types of scalar functions along with examples: */

/* 1. String Functions
LENGTH(): Returns the length of a string.
 */
SELECT username, LENGTH(username) AS username_length 
FROM users;

/* 
CONCAT(): Concatenates two or more strings. */

SELECT CONCAT(first_name, ' ', last_name) AS full_name 
FROM users;


/* SUBSTRING(): Extracts a substring from a string. */

SELECT SUBSTRING(username, 1, 3) AS username_prefix 
FROM users;


/* 2. Numeric Functions
ROUND(): Rounds a number to a specified number of decimal places.
 */


/* SELECT ROUND(price, 2) AS rounded_price 
FROM products;
ABS(): Returns the absolute value of a number. */


/* SELECT ABS(-10) AS absolute_value; -- Returns 10
3. Date and Time Functions
NOW(): Returns the current date and time.
 */


SELECT NOW() AS current_datetime;

/* DATE_FORMAT(): Formats a date according to a specified format. */


SELECT DATE_FORMAT(order_date, '%Y-%m-%d') AS formatted_date 
FROM orders;

/* 4. Control Flow Functions
IF(): Returns one value if a condition is true, and another value if its false. */

SELECT username, 
       IF(active = 1, 'Active', 'Inactive') AS status 
FROM users;


/* CASE: Similar to IF(), but can handle multiple conditions. */

SELECT username, 
       CASE 
           WHEN score >= 90 THEN 'A'
           WHEN score >= 80 THEN 'B'
           WHEN score >= 70 THEN 'C'
           ELSE 'F'
       END AS grade 
FROM students;


/* 5. Conversion Functions
CAST(): Converts one data type to another.
 */


SELECT CAST(price AS DECIMAL(10, 2)) AS formatted_price 
FROM products;


/* CONVERT(): Similar to CAST(), used for converting data types.
 */

SELECT CONVERT(username USING utf8) AS utf8_username 
FROM users;


/* Scalar functions are versatile and can greatly enhance the way you manipulate and display data in your queries. If you need further examples or have specific use cases in mind, just let me know! */




/* Date function 

MySQL provides several date functions that allow you to manipulate and retrieve date and time values. Here are some commonly used date functions along with examples: */

/* 1. Current Date and Time
NOW(): Returns the current date and time.
 */
SELECT NOW() AS current_datetime;

/* CURDATE(): Returns the current date. */

SELECT CURDATE() AS current_date;

/* CURTIME(): Returns the current time. */


SELECT CURTIME() AS current_time;

/* 2. Date Manipulation
DATE_ADD(): Adds a specified time interval to a date. */


SELECT DATE_ADD(NOW(), INTERVAL 7 DAY) AS date_plus_7_days;

/* DATE_SUB(): Subtracts a specified time interval from a date. */


SELECT DATE_SUB(NOW(), INTERVAL 1 MONTH) AS date_minus_1_month;

/* 3. Extracting Parts of a Date
YEAR(): Extracts the year from a date.
 */


SELECT YEAR(order_date) AS order_year 
FROM orders;

/* 
MONTH(): Extracts the month from a date. */


SELECT MONTH(order_date) AS order_month 
FROM orders;

/* DAY(): Extracts the day from a date. */

SELECT DAY(order_date) AS order_day 
FROM orders;


/* 4. Formatting Dates
DATE_FORMAT(): Formats a date according to a specified format. */

SELECT DATE_FORMAT(order_date, '%Y-%m-%d') AS formatted_date 
FROM orders;

/* Common format specifiers: */


/* 
DATEDIFF(): Returns the difference in days between two dates. */

SELECT DATEDIFF(NOW(), order_date) AS days_since_order 
FROM orders;


/* TIMEDIFF(): Returns the difference between two time values. */

SELECT TIMEDIFF(NOW(), start_time) AS time_difference 
FROM events;


/* 6. Getting the Last Day of the Month
LAST_DAY(): Returns the last day of the month for a given date.
 */


SELECT LAST_DAY(order_date) AS last_day_of_month 
FROM orders;


/* 7. Converting Strings to Dates
STR_TO_DATE(): Converts a string to a date based on a specified format.
 */


SELECT STR_TO_DATE('31-12-2023', '%d-%m-%Y') AS converted_date;




/* Mathmetical functions 

MySQL provides several mathematical functions that allow you to perform calculations on numeric data. Here are some commonly used mathematical functions along with examples: */

/* 1. Basic Mathematical Functions
ABS(): Returns the absolute value of a number.
 */
SELECT ABS(-15) AS absolute_value;  -- Returns 15
ROUND(): Rounds a number to a specified number of decimal places.


SELECT ROUND(123.4567, 2) AS rounded_value;  -- Returns 123.46

/* FLOOR(): Rounds a number down to the nearest integer. */

SELECT FLOOR(123.456) AS floored_value;  -- Returns 123


/* CEIL() or CEILING(): Rounds a number up to the nearest integer. */

SELECT CEIL(123.456) AS ceiled_value;  -- Returns 124

/* 2. Trigonometric Functions
SIN(): Returns the sine of a value.
 */

SELECT SIN(PI()/2) AS sine_value;  -- Returns 1

/* 
COS(): Returns the cosine of a value. */


SELECT COS(0) AS cosine_value;  -- Returns 1

/* TAN(): Returns the tangent of a value. */


SELECT TAN(PI()/4) AS tangent_value;  -- Returns 1

/* 3. Exponential and Logarithmic Functions
EXP(): Returns e raised to the power of a number.
 */

SELECT EXP(1) AS e_to_the_power_of_1;  -- Returns approximately 2.71828


/* LOG(): Returns the natural logarithm (base e) of a number. */


SELECT LOG(2.71828) AS natural_log;  -- Returns 1
LOG10(): Returns the base-10 logarithm of a number.


SELECT LOG10(100) AS log_base_10;  -- Returns 2

/* 4. Power and Square Root Functions
POW() or POWER(): Raises a number to the power of another number.
 */



SELECT POWER(2, 3) AS two_to_the_power_of_three;  -- Returns 8


/* SQRT(): Returns the square root of a number.
 */

SELECT SQRT(16) AS square_root;  -- Returns 4

/* 5. Random Number Generation
RAND(): Generates a random floating-point value between 0 and 1. */


SELECT RAND() AS random_number;

/* 6. Miscellaneous Functions
GREATEST(): Returns the largest value from a list of values.
 */


SELECT GREATEST(10, 20, 30) AS max_value;  -- Returns 30

/* LEAST(): Returns the smallest value from a list of values.
 */


SELECT LEAST(10, 20, 30) AS min_value;  -- Returns 10



---------------------------------------------------------------------------------------------------------------------------------------

/* The ALTER TABLE statement in MySQL is used to modify an existing table structure. You can use it to add, drop, or modify columns, as well as to change table constraints. Here are some common operations you can perform with ALTER TABLE, along with examples:
 */
/* 1. Adding a Column
To add a new column to a table: */

/* ALTER TABLE table_name 
ADD column_name datatype [constraint]; */


ALTER TABLE users 
ADD age INT;


/* 2. Dropping a Column
To remove a column from a table: */

/* ALTER TABLE table_name 
DROP COLUMN column_name; */


ALTER TABLE users 
DROP COLUMN age;

/* 3. Modifying a Column
To change the data type or attributes of an existing column: */


/* ALTER TABLE table_name 
MODIFY COLUMN column_name new_datatype [constraint];
 */


ALTER TABLE users 
MODIFY COLUMN username VARCHAR(50) NOT NULL;


/* 4. Renaming a Column
To rename a column: */
/* 
ALTER TABLE table_name 
CHANGE old_column_name new_column_name datatype [constraint];
 */


ALTER TABLE users 
CHANGE username user_name VARCHAR(50);


/* 5. Renaming a Table
To rename an existing table: */



ALTER TABLE users 
RENAME TO customers;


/* 6. Adding a Primary Key
To add a primary key to a table:
 */


ALTER TABLE customers 
ADD PRIMARY KEY (customer_id);


/* 7. Dropping a Primary Key
To remove a primary key from a table:
 */

ALTER TABLE customers 
DROP PRIMARY KEY;


/* 8. Adding a Foreign Key
To add a foreign key constraint: */

ALTER TABLE orders 
ADD CONSTRAINT fk_customer 
FOREIGN KEY (customer_id) REFERENCES customers (customer_id);

/* 
9. Dropping a Foreign Key
To remove a foreign key constraint: */


ALTER TABLE orders 
DROP FOREIGN KEY fk_customer;


/* 10. Adding an Index
To create an index on a column: */


ALTER TABLE customers 
ADD INDEX idx_last_name (last_name);

/* 
11. Dropping an Index
To remove an index: */

ALTER TABLE customers 
DROP INDEX idx_last_name;
