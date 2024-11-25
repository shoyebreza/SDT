use dummydb;


CREATE TABLE Instructor ( 
InstructorID INT AUTO_INCREMENT PRIMARY KEY, 
Name VARCHAR(255) NOT NULL, 
Email VARCHAR(255) NOT NULL UNIQUE, 
Phone VARCHAR(15), 
Department VARCHAR(50) );

CREATE TABLE Course ( 
CourseID INT AUTO_INCREMENT PRIMARY KEY, 
Title VARCHAR(255) NOT NULL, 
Credits INT NOT NULL, 
InstructorID INT, 
FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID) );


CREATE TABLE Student ( 
StudentID INT AUTO_INCREMENT PRIMARY KEY, 
Name VARCHAR(255) NOT NULL, 
Email VARCHAR(255) NOT NULL UNIQUE, 
Phone VARCHAR(15) );


CREATE TABLE Enrollment ( 
EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, 
StudentID INT, CourseID INT, 
EnrollmentDate DATE NOT NULL, 
FOREIGN KEY (StudentID) REFERENCES Student(StudentID), 
FOREIGN KEY (CourseID) REFERENCES Course(CourseID) );


/*-----------------------------------*/ 


INSERT INTO Instructor (Name, Email, Phone, Department) VALUES
('Dr. John Smith', 'john.smith@example.com', '555-1234', 'Computer Science'),
('Dr. Emily Davis', 'emily.davis@example.com', '555-2345', 'Mathematics'),
('Dr. Michael Lee', 'michael.lee@example.com', '555-3456', 'Physics'),
('Prof. Sarah Johnson', 'sarah.johnson@example.com', '555-4567', 'History'),
('Dr. David Clark', 'david.clark@example.com', '555-5678', 'Engineering');


INSERT INTO Course (Title, Credits, InstructorID) VALUES
('Introduction to Programming', 3, 1), 
('Data Structures and Algorithms', 4, 1),
('Calculus I', 4, 2),
('Linear Algebra', 3, 2),
('Classical Mechanics', 3, 3),
('Modern Physics', 4, 3),
('World History', 3, 4),
('Modern European History', 3, 4),
('Introduction to Engineering', 4, 5),
('Thermodynamics', 3, 5);


INSERT INTO Student (Name, Email, Phone) VALUES
('Alice Walker', 'alice.walker@example.com', '555-6789'),
('Bob White', 'bob.white@example.com', '555-7890'),
('Charlie Brown', 'charlie.brown@example.com', '555-8901'),
('Diana Green', 'diana.green@example.com', '555-9012'),
('Eva Blue', 'eva.blue@example.com', '555-0123'),
('Frank Red', 'frank.red@example.com', '555-1235'),
('Grace Black', 'grace.black@example.com', '555-2346'),
('Hannah Gray', 'hannah.gray@example.com', '555-3457');



INSERT INTO Enrollment (StudentID, CourseID, EnrollmentDate) VALUES
(1, 1, '2024-09-01'),
(1, 3, '2024-09-01'),
(2, 2, '2024-09-02'),
(2, 4, '2024-09-02'),
(3, 1, '2024-09-03'),
(3, 5, '2024-09-03'),
(4, 6, '2024-09-04'),
(4, 3, '2024-09-04'),
(5, 7, '2024-09-05'),
(5, 8, '2024-09-05'),
(6, 1, '2024-09-06'),
(6, 2, '2024-09-06'),
(7, 10, '2024-09-07'),
(7, 9, '2024-09-07'),
(8, 4, '2024-09-08'),
(8, 6, '2024-09-08');
















