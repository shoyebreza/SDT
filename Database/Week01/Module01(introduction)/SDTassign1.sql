
// for question 1-2

USE phitron;

CREATE TABLE students(
id int auto_increment primary key,
name varchar(250) not null,
phone char(11) default null,
email varchar(250) default null,
created_at timestamp default current_timestamp,
updated_at timestamp default null on update current_timestamp);


INSERT INTO students (name, phone, email) VALUES
('hasan', '12345678901', 'hasan@example.com'),
('rakin', '12345678901', 'rakin@example.com');

CREATE TABLE library(
id int auto_increment primary key,
student_id int,
book varchar(250) not null,
reading timestamp default current_timestamp,
returned timestamp default null,
foreign key (student_id) references students(id));


CREATE TABLE fees (
    id int auto_increment primary key,
    student_id INT,
    amount decimal(10, 2) not null,
    payment_date timestamp default current_timestamp,
    status ENUM('Paid', 'Pending', 'Overdue') DEFAULT 'Pending',
    foreign key (student_id) references students(id)
);


// for question 3

Data : 
	data is unprocessed and unorganized mixing verious type of data thats not a meaningfull and not usable for decission making.

information : 
	information is processed and well organized data that have Provides context and meaning. Useful for decision-making and understanding.
presented in a structured format.


// for question 4

SET SQL_SAFE_UPDATES = 0;


//for question 5 



CREATE TABLE Employee (
    EmployeeID int primary key,
    FirstName varchar(50) not null,
    LastName varchar(50) not null,
    Age int not null,
    Department varchar(50) not null
);

INSERT INTO Employee (EmployeeID, FirstName, LastName, Age, Department) VALUES
(1, 'John', 'Doe', 28, 'Sales'),
(2, 'Jane', 'Smith', 32, 'Marketing'),
(3, 'Michael', 'Johnson', 35, 'Finance'),
(4, 'Sarah', 'Brown', 30, 'HR'),
(5, 'William', 'Davis', 25, 'Engineering'),
(6, 'Emily', 'Wilson', 28, 'Sales'),
(7, 'Robert', 'Lee', 33, 'Marketing'),
(8, 'Laura', 'Hall', 29, 'HR'),
(9, 'Thomas', 'White', 31, 'Finance'),
(10, 'Olivia', 'Clark', 27, 'Engineering');

SELECT DISTINCT Department FROM Employee;


// for question 6

SELECT lastName FROM Employee ORDER BY Age DESC;


// for question 7

SELECT lastName FROM Employee WHERE Department= 'Marketing' AND Age >30;



// for question 8 

SELECT * FROM Employee;

// for question 9

SELECT * FROM Employee WHERE LastName like '%son';


// for question 10

SELECT * FROM Employee WHERE Department like '%Engineering%';



