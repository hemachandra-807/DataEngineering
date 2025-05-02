CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    LastLogin DATETIME,
    Status ENUM('Active', 'Inactive', 'Suspended') DEFAULT 'Active',
    INDEX (Email)
);

       
       
INSERT INTO Users 
(Username, Email, PasswordHash, FirstName, LastName, DateOfBirth, CreatedAt, LastLogin, Status)
VALUES 
("hemachandra807", "hemachandra@gmail.com", "hema@123", "Meluvalasa", "Hemachandra", '2001-01-10', NOW(), NOW(), 'Active');

create table Students(
		student_id int primary key,
        name varchar(100),
        age int,
        check(age>18)
	);
    

create table Enrollments (
	enrollment_id int primary key,
    student_id int,
    course_id int,
    foreign key (student_id) references Students(student_id)
    );
    
Insert into students values(101, "Vijay", 20), (102, "Bhanu", 22), (103, "Pranu", 19);
insert into enrollments values(201, 101, 301);


create table OrderDetails(
		order_id int,
        product_id int,
        primary key (order_id, product_id)
);
    
drop table employees;

truncate table employees;
USE REVATURETABLE;
create TABLE PRODUCTS(PRODUCTID INT, PRODUCTNAME varchar(20), PRICE INT);
INSERT INTO PRODUCTS VALUES(1, 'BIKE', 200000), (2, 'BIKE1', 300000);


select min(price) as smallestPrice, productid
from products
group by productid;

select max(price) as smallestPrice, productid
from products
group by productid;

insert into products values(3,'BIKE3',300000);

select avg(price) as smallestPrice, productid
from products
group by productid;

select count(*) as numbercolumns
from products;

select count(productid)
from products
where price > 200000;

select count(distinct price)
from products;

insert into products values(4,"BIKE4",200000);

select count(distinct price)
from products;

select sum(price)
from products;

create table customers (
customer_id int primary key,
name varchar(100)
);

create table orders(
	order_id int primary key,
    customer_id int,
    product varchar(100),
    foreign key (customer_id) references customers(customer_id)
    on delete cascade
    );
    
insert into customers values(1, 'Aravindh'),(2,'Raja');

insert into orders values(101, 1, 'laptop'), (102, 1, 'phone'),(103, 2,'Tablet');

delete from customers where customer_id = 1;

CREATE TABLE Customerstable (

    CustomerID INT PRIMARY KEY,

    CustomerName VARCHAR(100),

    ContactName VARCHAR(100),

    Country VARCHAR(50)

);
 
CREATE TABLE Orderstable (

    OrderID INT PRIMARY KEY,

    OrderDate DATE,

    CustomerID INT,

    Amount DECIMAL(10, 2),

    FOREIGN KEY (CustomerID) REFERENCES Customerstable(CustomerID)

);
 
INSERT INTO Customerstable (CustomerID, CustomerName, ContactName, Country) VALUES

(1, 'John Doe', 'John D.', 'USA'),

(2, 'Jane Smith', 'Jane S.', 'UK'),

(3, 'Alice Brown', 'Alice B.', 'Canada'),

(4, 'Bob Johnson', 'Bob J.', 'Australia');
 
INSERT INTO Orderstable (OrderID, OrderDate, CustomerID, Amount) VALUES

(101, '2024-09-01', 1, 250.00),

(102, '2024-09-05', 2, 300.00),

(103, '2024-09-07', 1, 150.00),

(104, '2024-09-10', 3, 450.00);


select 
customerstable.customerid,
customerstable.customername,
orderstable.orderid,
orderstable.orderdate,
orderstable.amount
from customerstable
inner join 
orderstable on customerstable.customerid = orderstable.customerid;

select 
customerstable.customerid,
customerstable.customername,
orderstable.orderid,
orderstable.orderdate,
orderstable.amount
from customerstable
left join 
orderstable on customerstable.customerid = orderstable.customerid;

select 
customerstable.customerid,
customerstable.customername,
orderstable.orderid,
orderstable.orderdate,
orderstable.amount
from customerstable
right join 
orderstable on customerstable.customerid = orderstable.customerid;

create table Drinks(
	drinksid int primary key,
    drinksname varchar(100)
    );
create table Snacks(
	snacksid int primary key,
    drinks_id int,
    snacksname varchar(100)
);

insert into drinks values(1, 'tea'),(2,'coffee'),(3, 'Juice');
insert into snacks values(101, 1,'somasa'),(102,2,'apple'),(103,3,'papaya');

select *
from drinks
cross join
snacks on drinks.drinksid = snacks.drinks_id;

CREATE TABLE EMPLOYEE (EMP_ID INT, ENAME VARCHAR(20), JOB_DESC VARCHAR(25), SALARY INT, HIRE_DATE date);

INSERT INTO EMPLOYEE VALUES (1, 'RAM', 'ADMIN', 100000, DATE '2024-02-02');

INSERT INTO EMPLOYEE VALUES (2, 'george', 'MANAGER', 200000, DATE '2024-02-02');

INSERT INTO EMPLOYEE VALUES (3, 'Aravind', 'SALES', 300000, DATE '2024-02-02');

INSERT INTO EMPLOYEE VALUES (4, 'Nivetha', 'SALES', 250000, DATE '2024-02-02');

INSERT INTO EMPLOYEE VALUES (5, 'Hussain', 'HR', 350000, DATE '2024-02-02');


select * from employee;

select * from employee order by job_desc;

select job_desc, avg(salary) from employee group by job_desc;

select job_desc, count(emp_id) from employee group by job_desc;

select job_desc, count(emp_id)
from employee
group by job_desc
having count(emp_id)>1
order by job_desc;

select job_desc, count(emp_id)
from employee where salary > 400000
group by job_desc
having count(emp_id)>1
order by job_desc;

INSERT INTO EMPLOYEE VALUES (6, 'Vijesh', 'Hr', 500000, DATE '2025-07-25');
INSERT INTO EMPLOYEE VALUES (7, 'Guru', 'Manager', 450000, DATE '2023-04-10');	
INSERT INTO employee VALUES (8, 'Kumar', 'hr', 600000, DATE '2024-05-01');

select upper(job_desc) as job_desc, count(emp_id)
from employee 
where salary > 400000
group by upper(job_desc)
having count(emp_id)>1
order by job_desc;


#10-April-2025 class

use revaturetable;

select * from employee;

select ename 
from employee
where salary < (select avg(salary) 
				from employee);
                

select ename, salary
from employee
where salary > (select avg(salary) 
				from employee);
                
CREATE TABLE departments (

    department_id INT PRIMARY KEY,

    department_name VARCHAR(50)

);
 
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO departments (department_id, department_name) VALUES
(1, 'Sales'),
(2, 'Marketing'),
(3, 'HR');

INSERT INTO employees (employee_id, employee_name, department_id) VALUES
(101, 'Alice', 1),
(102, 'Bob', 1),
(103, 'Charlie', 2),
(104, 'Diana', 3);

select *
from employees
where department_id = (select department_id
						from departments
                        where department_name = 'Sales');

select employee_name,
		(select department_name
		from departments
        where departments.department_id = employees.department_id) as department_name
from employees;

select *
from employees
where department_id IN (select department_id
        from employees
        group by department_id
        having count(*) > 1);
        
select department_name
from departments d
where exists (select 1
from employees e
where e.department_id = d.department_id);

select department_name
from departments d
where  not exists (select 1
from employees e
where e.department_id = d.department_id);


INSERT INTO departments (department_id, department_name) VALUES
(5, 'Training');

select department_name
from departments d
where  not exists (select 1
from employees e
where e.department_id = d.department_id);

select department_id, avg(employee_id) as avg_emp_id
from employees
group by department_id
having avg_emp_id > 102;

-- scalar functions operate on a single value and return a single value.alter

SELECT ucase('Hello World') as UperCase;
SELECT lcase('Hello World') as LowerCase;

SELECT mid('Hello World',4,8) as Subdtring;

SELECT length('Hello World') as Length_String;

SELECT round(1592.4540,2) as Round_value;

SELECT now() as CurrentDateTime;

SELECT format(12872834.1234,2) as Format_Vlaue;

select employee_name, length(employee_name) as name_length
from employees;

SELECT SUBSTRING('MySQL', 2, 3);

SELECT CONCAT('Rev', 'Stock');

SELECT MOD(10, 3);

SELECT POWER(2, 3);

SELECT SQRT(16);

SELECT CURDATE();

SELECT CURTIME();

SELECT IF(10 > 5, 'Yes', 'No');

use revaturetable;

CREATE TABLE Customer(
cust_id int auto_increment,
cust_name varchar(100),
coupon_code varchar(100),
primary key(cust_id)
);

ALTER TABLE customer auto_increment = 1001;
 select * from customer;
 
 insert into customer (cust_name, coupon_code) values('Raju','customer101'), ('Vijay','customer102');
 
 select * from products;
 
 start transaction;
 
 savepoint point;
 
 insert into products values(5, 'Bike5',8808788);
 
 select * from products;
 
 rollback to point;
 
 select * from products;
 
 commit;
 
 select * from products;
 
 start transaction;
 savepoint point;
insert into products values(5, 'Bike5',8808788);
insert into products values(6, 'Bike6',9729169);

select * from products;

rollback to point;
commit;

select * from products;

DELIMITER //
CREATE PROCEDURE getAllUSers()
BEGIN
	SELECT * FROM USERS;
END;
//

call getAllUsers()


select * from employees;
use revaturetable;

DELIMITER //
CREATE PROCEDURE getEmployeeDetails(IN EMP_id int)
BEGIN
	SELECT EMPLOYEE_ID, EMPLOYEE_NAME
    FROM EMPLOYEES
    WHERE EMPLOYEE_ID = EMP_id;
END;
//

CALL getEmployeeDetails(101);

CALL getEmployeeDetails(102);

CALL getEmployeeDetails(103);

DELIMITER //
CREATE procedure getEmpDetails(IN Emp_id INT, OUT empName varchar(100))
BEGIN
		SELECT employee_name INTO empName
        FROM employees
        where employee_id = Emp_id;
END;
//

SET @emp_Name = '';

CALL getEmpDetails(101, @emp_Name);

SELECT @emp_Name;

-- 11-April-2025 class notes

use revaturetable;

select * from employees;

create view employees_name as 
select employee_id, employee_name, department_id
from employees
where department_id = 1;

select * from employees_name;

create or replace view names_of_employees as 
select employee_id, employee_name
from employees
where department_id = 1;

select * from names_of_employees;

-- drop the view
drop view names_of_employees;

-- you can use Insert, Delete, Update statments on views
-- and changes will reflect on the original table

update names_of_employees
set employee_name = 'BoB'
where employee_id = 102;

select * from employees;


-- trigger is a database object that automatically executes block os sql
-- code in response to certain events on table or view like insert, update, delete

CREATE TABLE items (
    id INT PRIMARY KEY, -- clustered index
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
 
INSERT INTO items(id, name, price) 
VALUES (1, 'Item', 50.00);

CREATE TABLE item_changes (
    change_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT,
    change_type VARCHAR(10),
    change_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES items(id)
);

delimiter //
create trigger update_items_trigger
after update
on items
for each row 
begin
	insert into item_changes (item_id, change_type)
    values(new.id, 'Update');
end;
//

select * from items;

select * from item_changes;

update items set name = 'Laptop' where id = 1;

select * from items;
select * from item_changes;


CREATE TABLE emp (

    employee_id INT PRIMARY KEY,

    name VARCHAR(50),

    department VARCHAR(50),

    salary INT

);
 
INSERT INTO emp (employee_id, name, department, salary) VALUES

(1, 'Alice',   'Sales', 50000),

(2, 'Bob',     'Sales', 60000),

(3, 'Charlie', 'Sales', 45000),

(4, 'David',   'IT',    70000),

(5, 'Eva',     'IT',    80000),

(6, 'Frank',   'IT',    75000);
 
 select 
	employee_id,
    name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary desc) as rank_in_dept
From emp;

-- running tool of salaries
select 
	employee_id,
    name,
    salary,
    sum(salary) over (order by salary) as running_tool
from emp;

-- compare each employee salary with previous and next
select 
	employee_id,
    name,
    salary,
    lag(salary) over (order by salary) as previous_salary,
    lead(salary) over (order by salary) as next_salary
from emp;

select 
	employee_id,
    name,
    salary,
    lag(salary,1,'No one is there to compare') over (order by salary) as previous_salary,
    lead(salary,1,'No one is there to compare') over (order by salary) as next_salary
from emp;

-- rank employee by salary within department

select employee_id, name, department, salary,
	rank() over (partition by department order by salary desc) as rank_in_dept
from emp;

-- dense rank employee by salary within department
select employee_id, name, department, salary,
	dense_rank() over (order by salary desc) as rank_in_dept
from emp;

-- salary quartile
select employee_id, name, department, salary,
	ntile(4) over (order by salary desc) as salary_quartile
from emp;

-- salary quartile
select employee_id, name, department, salary,
	ntile(3) over (order by salary desc) as salary_quartile
from emp;

 use revaturetable;
 
DELIMITER //
CREATE FUNCTION calculateRectangleArea(length FLOAT, width FLOAT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
	RETURN length * width;
END;
//

SELECT calculateRectangleArea(2.2, 3.5) AS Result;
--        or --
SET @Result = calculateRectangleArea(5.5,2.3);
SELECT @Result;

SELECT employee_id, salary,
	CASE
        WHEN salary > 100000 THEN 'High'
        WHEN salary BETWEEN 50000 AND 100000 THEN 'Medium'
        ELSE 'Low'
	END AS salary_grade
FROM emp;


SELECT * FROM orders
WHERE 
	status = CASE
				WHEN customer_type = 'VIP' THEN 'PRIORITY'
                ELSE 'STandard'
			END;
            
UPDATE Products
SET Price = 
		CASE 
			WHEN category = 'Electronics' THEN price * 0.9
            WHEN category = 'Clothing'THEN price * 0.8
            ELSE price
		END;
   

CREATE TABLE people(
	id int primary key,
    name varchar(100),
    age int
    );
INSERT INTO people values(1,'hemachandra',24), (2,'Aravindh',23),(3,'Raja',20);

SELECT 
	name,
    age,
    CASE 
		WHEN age < 18 THEN 'Minimum'
        WHEN age BETWEEN 18 AND 59 THEN 'Adult'
        ELSE 'Senior'
	END as age_group
FROM people;

CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT,
    grade CHAR(1)
);

INSERT INTO student (id, name, marks, grade) VALUES
(1, 'Alice', 95, NULL),
(2, 'Bob', 82, NULL),
(3, 'Charlie', 67, NULL),
(4, 'Diana', 40, NULL),
(5, 'Ethan', 76, NULL);

UPDATE student
SET grade = 
		CASE
			WHEN marks >=90 THEN 'A'
            WHEN marks >=75 THEN 'B'
            WHEN marks >=6 THEN 'C'
            ELSE 'D'
		END;

-- works in MYSQL/Postgresql
EXPLAIN SELECT * FROM employees WHERE department_id = 1;

-- for Orcale
EXPLAIN PLAN FOR 


CREATE TABLE Datajson(
	id int,
    profile JSON
);
INSERT INTO datajson VALUES(1, '{"name" : "Alice", "skills" : ["SQL", "Python"]}');

SELECT JSON_EXTRACT(profile, '$.skills') FROM Datajson; -- to print all data

SELECT JSON_EXTRACT(profile, '$.skills[0]') FROM Datajson; -- to print based on index

-- Hierarchical Querying
-- Recursion

CREATE TABLE employeesNew (

    id INT PRIMARY KEY,

    name VARCHAR(100),

    manager_id INT

);
 
INSERT INTO employeesNew (id, name, manager_id) VALUES

(1, 'Alice (CEO)', NULL),

(2, 'Bob (CTO)', 1),

(3, 'Charlie (CFO)', 1),

(4, 'David (Dev Manager)', 2),

(5, 'Eve (Developer)', 4),

(6, 'Frank (Intern)', 5);
 
WITH RECURSIVE employee_hierarchy AS (
    SELECT 
        id,
        name,
        manager_id,
        1 AS level,
        CAST(name AS CHAR(1000)) AS path
    FROM employeesNew
    WHERE manager_id IS NULL  -- Root (e.g., CEO)

    UNION ALL

    SELECT 
        e.id,
        e.name,
        e.manager_id,
        eh.level + 1,
        CONCAT(eh.path, ' → ', e.name)
    FROM employeesNew e
    JOIN employee_hierarchy eh ON e.manager_id = eh.id
)

-- Final SELECT to fetch data from the CTE
SELECT * FROM employee_hierarchy;


-- Project Sql Operations

CREATE DATABASE stock_analysis;

USE stock_analysis;

CREATE TABLE stock_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10),
    date DATE,
    open_price DECIMAL(10, 2),
    high_price DECIMAL(10, 2),
    low_price DECIMAL(10, 2),
    close_price DECIMAL(10, 2),
    volume INT
);

CREATE TABLE company_metadata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10),
    company_name VARCHAR(100),
    exchange VARCHAR(50),
    industry VARCHAR(50),
    products JSON
);

select * from company_metadata;

USE REVATURETABLE;

WITH RECURSIVE EMPLOYEES_HIERARCHY AS
(
SELECT ID, NAME, MANAGER_ID, 1 AS LEVEL, CAST(NAME AS CHAR(1000)) AS PATH
FROM EMPLOYEESNEW
WHERE MANAGER_ID IS NULL
UNION ALL
SELECT E.ID, E.NAME, E.MANAGER_ID, EH.LEVEL + 1,
CONCAT(EH.PATH, '->', E.NAME)
FROM EMPLOYEESNEW E JOIN EMPLOYEES_HIERARCHY EH
ON E.MANAGER_ID = EH.ID
)
SELECT *
FROM EMPLOYEES_HIERARCHY;

-- Factorial Number using functions
DELIMITER $$
CREATE FUNCTION FACT(NUM INT)
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE RESULT INT DEFAULT 1;
    WHILE NUM > 1 DO
		SET RESULT = RESULT * NUM;
		SET NUM = NUM - 1;
	END WHILE;
    RETURN RESULT;
END $$

DELIMITER ;

SELECT FACT(5);

SHOW FUNCTION STATUS WHERE Db = 'revaturetable';

-- REVERSE A NUM
DELIMITER $$
CREATE FUNCTION REVERSE_NUM(NUM INT)
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE REV INT DEFAULT 0;
    DECLARE REM INT;
    
    WHILE NUM > 0 DO
		SET REM = NUM % 10;
        SET REV = REV * 10 + REM;
        SET NUM = NUM DIV 10;
        END WHILE;
        
        RETURN REV;
END $$
DELIMITER ;
	
SELECT REVERSE_NUM(123);
        