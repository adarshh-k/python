use MYDB1

--- 1.CREATE TABLE AND INSERT ---

create table Studentss(
StudentID int,
StudentName varchar(50),
Age int,
Gender char(10),
Course varchar(50),
Fees int,
city varchar(30)
);

insert into Studentss values
(1,'Adarsh',21,'Male','Bsc cs',17000,'calicut'),
(2,'Naveen',21,'Male','Bsc cs',17000,'calicut'),
(3,'Adheena',20,'Female','Bca',15000,'kochi'),
(4,'Anu',21,'Female','Bsc electronics',16000,'calicut'),
(5,'Akshay',22,'Male','Bsc cs',17000,'kannur'),
(6,'Akash',19,'Male','Bsc maths',13000,'kochi'),
(7,'Hari',23,'Male','Bca',15000,'kochi'),
(8,'Adith',21,'Male','Bca',15000,'malappuram'),
(9,'Swathy',25,'Female','Bsc maths',13000,'kochi'),
(10,'Aswathy',22,'Female','Bsc electronics',16000,'calicut');
 select * from Studentss

 
CREATE TABLE Employeee1(
    Employee_id INT,
    Employee_name VARCHAR(50),
    Department VARCHAR(30),
    Salary INT,
    Age INT,
    City VARCHAR(30),
    Experience int
);

INSERT INTO Employeee1 VALUES
(101, 'Rahul', 'IT', 45000, 25, 'Kochi',2),
(102, 'Anu', 'HR', 35000, 28, 'Calicut',3),
(103, 'Vishnu', 'IT', 55000, 30, 'Kochi',2),
(104, 'Neha', 'Finance', 40000, 26, 'Thrissur',3),
(105, 'Arjun', 'IT', 65000, 32, 'Bangalore',4),
(106, 'Meera', 'HR', 30000, 24, 'Kochi',4),
(107, 'Akhil', 'Finance', 50000, 29, 'Calicut',2),
(108, 'Sneha', 'IT', 60000, 27, 'Chennai',2),
(109, 'Aman', 'HR', 13000, 27, 'Chennai',3),
(110, 'Alan', 'IT', 26000, 27, 'kochi',4);

select * from Employeee1

--- 2.USING ARITHMETIC OPERATORS ---

-- name and salary after adding 5000 bonus --
select Employee_name,Salary+5000 as Salary_bonus from Employeee1;

-- name and salary after deducing 2000 --
select Employee_name,Salary-2000 as Salary_deduct from Employeee1;

-- name and annual salary --
select Employee_name,Salary*12 as Annual_salary from Employeee1;

-- name and 10% slary after increment --
select Employee_name,Salary*1.10 as salary_10 from Employeee1;

-- name and 15% salary after increment --
select Employee_name,Salary*1.15 as Salary_15 from Employeee1;

--- 3.COMPARISON OPERATORS ---

-- employees whose salary>30000 --
select * from Employeee1 where Salary>30000;

-- employees whose salary<25000 --
select * from Employeee1 where Salary<25000;

-- employees with salary=40000 --
select * from Employeee1 where Salary=40000;

--  employees with age>=30 --
select * from Employeee1 where age>=30;

-- employees with age <=25 --
select * from Employeee1 where age<=25;

-- employees with experience!=2years --
select * from Employeee1 where Experience<>2;

--- 4.LOGICAL OPERATORS ---

-- employee whose salary>30000 and exp>2yrs --
select * from Employeee1 where Salary>30000 and Experience>2;

-- employee who work in IT and salary>35000 --
select * from Employeee1 where Department='IT' and Salary>35000;

-- employeee who lives in kochi or trivandrum --
select * from Employeee1 where City='Kochi' or City='Trivandrum';

-- employee with age>25 and salary<40000 --
select * from Employeee1 where Age>25 and Salary>40000;

-- employee who work in dept=HR or have exp>5 --
select * from Employeee1 where Department='HR' or Experience>5;

-- employee whose salary>25000 and not from kochi --
select * from Employeee1 where Salary>25000 and City!='Kochi';

--- 5.BETWEEN,IN,NOT IN ---

-- employees whose salary in between 25000 and 50000 --
select * from Employeee1 where Salary Between 25000 and 50000;

-- employees whose age in between 25 and 35 --
select * from Employeee1 where Age between 25 and 35;

-- employees with experiece between 2 and 5 yrs --
select * from Employeee1 where Experience between 2 and 5;

-- employees belong to IT,HR or finance dept --
select * from Employeee1 where Department in('IT','HR','Finance');

-- employee from kochi,calicut or trivandrum --
select * from Employeee1 where City in('Kochi','Calicut','Trivandrum');

-- employees not belong to HR or finance dept --
select * from Employeee1 where Department not in('HR','Finance');