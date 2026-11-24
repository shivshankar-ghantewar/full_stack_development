show databases;
use shiv;
describe employees;
select * from employees;
CREATE TABLE Employee (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    employee_designation VARCHAR(100),
    salary DECIMAL(10,2),
    city VARCHAR(100)
);

create database hospital;
use hospital;
CREATE TABLE Doctor (
    doctor_id int  ,
    doctor_name char(100) ,
    specialization char(100),
    experience int,
    salary int,
    city char(100)
);

drop table doctor;

INSERT INTO Doctor (doctor_id, doctor_name, specialization, experience, salary, city)
VALUES
(101, 'Amit Sharma', 'Cardiologist', 10, 120000.00, 'Mumbai'),
(102, 'Priya Patel', 'Dermatologist', 7, 90000.00, 'Pune'),
(103, 'Rahul Verma', 'Orthopedic', 12, 135000.00, 'Nagpur'),
(104, 'Sneha Joshi', 'Pediatrician', 5, 80000.00, 'Nashik'),
(105, 'Vikram Singh', 'Neurologist', 15, 180000.00, 'Delhi'),
(106, 'Neha Gupta', 'Gynecologist', 8, 95000.00, 'Hyderabad'),
(107, 'Rohan Mehta', 'ENT Specialist', 6, 85000.00, 'Ahmedabad'),
(108, 'Anjali Desai', 'Psychiatrist', 9, 110000.00, 'Bengaluru'),
(109, 'Karan Malhotra', 'General Physician', 4, 70000.00, 'Chennai'),
(110, 'Pooja Kulkarni', 'Ophthalmologist', 11, 125000.00, 'Kolhapur');

select * from doctor;

use shiv;

delete from employee;

use hospital;

delete from doctor where doctor_id=101;
SET SQL_SAFE_UPDATES = 0;

create database college;
use college;
create table student(id int primary key auto_increment not null,name varchar(20));
desc student;
insert into student(name)values
('shiv');

select * from student;

insert into student(name)values('pravin'),('gaurav'),('prajwal'),('arjun'),('gajanan');
delete from student;
select * from student;
-- truncate: reset to zero
truncate table  student;  

create table student2(id int,name varchar(20));
-- copy data to another table 
insert into student2 select * from student;
select * from student2;

use college;
create table employee(id int primary key auto_increment,first_name varchar(100) , last_name varchar (100), salary int , designation  varchar (100), dept varchar(100)); 
describe employee;
drop table employee;
INSERT INTO employee (first_name, last_name, salary, designation, dept) VALUES
('Rahul', 'Sharma', 45000, 'Software Engineer', 'IT');


alter table employee add column city varchar (100);
alter table employee modify column city varchar (200);
alter table employee drop column city;

alter table employee change id s_id int ;
select salary as sal from employee;
truncate table employee;

select * from employee;
alter table employee auto_increment=101;
INSERT INTO employee (first_name, last_name, salary, designation, dept) VALUES
('Rahul', 'Sharma', 45000, 'Software Engineer', 'IT'),
('Priya', 'Patil', 52000, 'HR Executive', 'HR'),
('Amit', 'Verma', 60000, 'Project Manager', 'Management'),
('Sneha', 'Kulkarni', 48000, 'Accountant', 'Finance'),
('Rohit', 'Singh', 55000, 'Data Analyst', 'IT'),
('Neha', 'Joshi', 40000, 'Sales Executive', 'Sales'),
('Vikram', 'Yadav', 70000, 'Team Lead', 'IT'),
('Pooja', 'Deshmukh', 38000, 'Customer Support', 'Support'),
('Karan', 'Mehta', 65000, 'Database Administrator', 'IT'),
('Anjali', 'Gupta', 50000, 'Marketing Executive', 'Marketing');

select distinct dept from employee; -- distinct: unique

show databases;
show tables;
select * from courses;
show databases;
use college;

create table courses(id int primary key auto_increment , name varchar (200),course varchar (100));
insert into courses (name , course) values('pravin','python'),('gaurav','java');
DESC courses;
alter table courses modify id int primary key auto_increment;
select *from courses c
right join student s 
on c.name = s.name;

select * from courses
cross join student ;

select * from courses union select * from student ;

create table employee(id int primary key auto_increment,name varchar (100),salary varchar (100));
select * from employee ;
select * from employee  limit 5  ;
 
select  count(distinct dept) from employee;  -- only unique values
select  count( dept) from employee;
select sum(salary) from employee;
select avg(salary) from employee;
select min(salary) from employee;
select max(salary) from employee;
select * from employee where dept in ('marketing','it');
select * from employee where dept not  in ('marketing','it');

select first_name from employee where salary is null;
select dept , sum(salary) from employee group by dept;
select dept , avg(salary) from employee group by dept;
select dept , min(salary) from employee group by dept;
select dept , max(salary) from employee group by dept;
select dept , count(*) from employee group by dept;

update employee set salary=null where first_name='rohit';
update employee set salary=null where first_name='amit';
SET SQL_SAFE_UPDATES = 0;


select dept , sum(salary) from employee  where salary> 30000 group by dept;

create database college_db;
create database hospital_db;
create database companies_db;
create database library_db;
create database bank_db;

show databases;
use library_db;

create table student (student_id int primary key auto_increment, name varchar (100), email varchar (100),
phone varchar (100), dob varchar (100), gender varchar (100));

create table course (course_id int primary key auto_increment, course_name varchar (100), duration int , fees int );

INSERT INTO student (name, email, phone, dob, gender)
VALUES
('Rahul Sharma', 'rahul@gmail.com', '9876543210', '2002-05-15', 'Male'),
('Priya Patil', 'priya@gmail.com', '9876543211', '2003-08-20', 'Female'),
('Amit Kumar', 'amit@gmail.com', '9876543212', '2001-12-10', 'Male'),
('Sneha Joshi', 'sneha@gmail.com', '9876543213', '2003-03-25', 'Female'),
('Rohit Singh', 'rohit@gmail.com', '9876543214', '2002-11-05', 'Male');


INSERT INTO course (course_name, duration, fees)
VALUES
('MCA', 2, 85000),
('MBA', 2, 90000),
('BCA', 3, 60000),
('BBA', 3, 55000),
('MTech', 2, 95000);

create table employee (student_id int primary key auto_increment, name varchar (100), email varchar (100),
phone varchar (100), dob varchar (100), gender varchar (100));

describe employee;
alter table employee modify employee_id int auto_increment;
describe employee;
select * from employee;
show tables;
 insert into employee select * from student;



USE hospital_db;

CREATE TABLE patient (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    phone VARCHAR(15),
    disease VARCHAR(100)
);

INSERT INTO patient (name, age, gender, phone, disease)
VALUES
('Rahul Sharma', 25, 'Male', '9876543210', 'Fever'),
('Priya Patil', 30, 'Female', '9876543211', 'Diabetes'),
('Amit Kumar', 45, 'Male', '9876543212', 'Blood Pressure'),
('Sneha Joshi', 28, 'Female', '9876543213', 'Migraine'),
('Rohit Singh', 35, 'Male', '9876543214', 'Asthma');

CREATE TABLE doctor (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    specialization VARCHAR(100),
    phone VARCHAR(15),
    experience INT
);

INSERT INTO doctor (name, specialization, phone, experience)
VALUES
('Dr. Raj Mehta', 'Cardiologist', '9876500011', 12),
('Dr. Neha Sharma', 'Dentist', '9876500012', 8),
('Dr. Amit Verma', 'Neurologist', '9876500013', 15),
('Dr. Pooja Patil', 'Dermatologist', '9876500014', 10),
('Dr. Rahul Joshi', 'Orthopedic', '9876500015', 7);


USE companies_db;

CREATE TABLE employee (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    department VARCHAR(50),
    salary INT
);

INSERT INTO employee (name, email, phone, department, salary)
VALUES
('Rahul Sharma', 'rahul@company.com', '9876543210', 'IT', 55000),
('Priya Patil', 'priya@company.com', '9876543211', 'HR', 48000),
('Amit Kumar', 'amit@company.com', '9876543212', 'Finance', 60000),
('Sneha Joshi', 'sneha@company.com', '9876543213', 'IT', 65000),
('Rohit Singh', 'rohit@company.com', '9876543214', 'Marketing', 45000);

CREATE TABLE department (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100),
    manager_name VARCHAR(100),
    location VARCHAR(100),
    budget INT
);

INSERT INTO department (department_name, manager_name, location, budget)
VALUES
('IT', 'Vikram Shah', 'Pune', 1000000),
('HR', 'Anjali Deshmukh', 'Mumbai', 500000),
('Finance', 'Raj Malhotra', 'Delhi', 800000),
('Marketing', 'Karan Mehta', 'Bangalore', 700000),
('Sales', 'Neeraj Patil', 'Hyderabad', 900000);


USE library_db;

CREATE TABLE book (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    book_name VARCHAR(150),
    author VARCHAR(100),
    category VARCHAR(50),
    price INT,
    quantity INT
);

INSERT INTO book (book_name, author, category, price, quantity)
VALUES
('Let Us C', 'Yashavant Kanetkar', 'Programming', 450, 10),
('Java Complete Reference', 'Herbert Schildt', 'Programming', 650, 8),
('SQL for Beginners', 'John Smith', 'Database', 500, 12),
('Python Basics', 'Mark Taylor', 'Programming', 550, 7),
('Data Science Handbook', 'Jake VanderPlas', 'Data Science', 800, 5);

CREATE TABLE member (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    membership_type VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO member (name, email, phone, membership_type, city)
VALUES
('Rahul Sharma', 'rahul@gmail.com', '9876543210', 'Premium', 'Pune'),
('Priya Patil', 'priya@gmail.com', '9876543211', 'Regular', 'Mumbai'),
('Amit Kumar', 'amit@gmail.com', '9876543212', 'Premium', 'Delhi'),
('Sneha Joshi', 'sneha@gmail.com', '9876543213', 'Regular', 'Nagpur'),
('Rohit Singh', 'rohit@gmail.com', '9876543214', 'Premium', 'Nashik');


USE bank_db;

CREATE TABLE customer (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    city VARCHAR(50),
    occupation VARCHAR(100)
);

INSERT INTO customer (name, email, phone, city, occupation)
VALUES
('Rahul Sharma', 'rahul@gmail.com', '9876543210', 'Pune', 'Engineer'),
('Priya Patil', 'priya@gmail.com', '9876543211', 'Mumbai', 'Teacher'),
('Amit Kumar', 'amit@gmail.com', '9876543212', 'Delhi', 'Businessman'),
('Sneha Joshi', 'sneha@gmail.com', '9876543213', 'Nagpur', 'Designer'),
('Rohit Singh', 'rohit@gmail.com', '9876543214', 'Nashik', 'Developer');

CREATE TABLE account (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    account_number VARCHAR(20),
    account_type VARCHAR(50),
    balance INT,
    branch VARCHAR(100)
);

INSERT INTO account (customer_id, account_number, account_type, balance, branch)
VALUES
(1, 'ACC10001', 'Savings', 50000, 'Pune'),
(2, 'ACC10002', 'Current', 85000, 'Mumbai'),
(3, 'ACC10003', 'Savings', 120000, 'Delhi'),
(4, 'ACC10004', 'Savings', 45000, 'Nagpur'),
(5, 'ACC10005', 'Current', 95000, 'Nashik');

select * from course;
alter table course add student_name varchar (100) after course_id;  
update course set student_name='gaurav' where course_id=2;
update course set student_name='gajanan' where course_id=3;
update course set student_name='pravin' where course_id=4;
update course set student_name='arjun' where course_id=5;

alter table course change fees amount int ;
describe course;
alter table course modify student_name varchar (50);
select * from course;

use hospital_db;
show  tables;

select * from patient;
-- aggregate function

-- count
select gender,count(phone) from patient group by gender;
select count(phone) from patient;
select count(patient_id ) from patient; 
select count(age) from patient;
select count(name) from patient;
select count(disease) from patient;

-- sum 
select sum(patient_id)  from patient;
select sum(age) from patient ;
select sum(age) from patient where age >30 ;


-- min
select min(patient_id) from patient;
select min(age) from patient;

-- max
select max(age) from patient where age<30 ;
select max(phone) from patient;

-- avg 
select avg(age) from patient;
select * from patient ;
use hospital_db;

-- clause 
select * from patient where patient_id =2 AND gender='female';
select * from patient where patient_id =2 or  patient_id=4;

-- order by clause
-- ascending and descending 
select * from doctor order by experience desc;
select * from doctor order by experience asc;

-- limit 
select * from doctor order by experience desc limit 2;
select * from doctor;
-- printing second largest number 
select * from doctor order by experience desc limit 1 offset 2;  -- offset = skip 
show tables;

select * from doctor order by rand() ;   -- random values


create table product (id int, product_name varchar (100), category varchar (100));
insert into product values (1,'laptop','gadjet'),(2,'shirt','clothes');
select* from product; 

update product set product_name='mobile' where id=1;

SET SQL_SAFE_UPDATES = 0;

use college_db;

-- JOINS IN SQL 
create table student2 (S_id int primary key auto_increment, s_name varchar (50), course_id varchar (50)); 
create table course2(course_id int primary key auto_increment, course_name varchar (50));

insert into student2 values(1,'shiv',101),(2,'gaurav',102),(3,'arjun',103),(4,'pravin',104);
insert into course2 values(101,'python'),(102,'java'),(103,'mern'),(104,'testing');

-- inner join
select s_id,course_name,course_id from student2 s
inner join course2 c 
on s.course_id=c.course_id;

-- left join
select * from student2 s
left join course2 c 
on s.course_id=c.course_id;

-- right join
select * from student2 s
right join course2 c 
on s.course_id=c.course_id;

-- cross join
select * from student2 
cross join course2 ;

-- union 
select * from student2 s
left join course2 c 
on s.course_id=c.course_id
union
select * from student2 s
right join course2 c 
on s.course_id=c.course_id;

-- keys 

-- primary key (unique and not null)

create table product(id int primary key , p_name varchar (50));
insert into product values(1,'mobile'),(2,'tv'),(3,'board'),(4,'laptop');
insert into product values(null,'mobile');  -- cannot be null value
insert into product values(1,'mobile');   -- cannot be duplicate value

describe product;
select * from product;

use college_db;

-- foreign key
create table fortune (s_id int primary key ,foreign key(s_id) references student2 (s_id)) ;

select * from student2;
describe fortune;

show  create  table fortune;

-- composite key : assigning primary key to more than 1 table column

create table fortune2 (s_id int , course_id int ,course_name varchar (50),primary key(s_id ,course_id));

select * from student2 ;
select * from fortune2;
insert into fortune values(1);

describe fortune2;
insert into fortune2 values(1,101,'python'),(1,102,'python'),(2,101,'python'),(2,102,'python'); 


create table student(id int primary key auto_increment, name varchar(50) , email varchar(100) unique, contact varchar (50) unique); 
describe student;

insert into student (name,email,contact)
values ('shiv','shiv@gmail.com','7776948887'),
('gaurav','gaurav@gmail.com','7776948876'),
('pravin','pravin@gmail.com','7776948675');

select id from student;

create index sortid on  student (id asc);
show index from student;


-- fulltext index
CREATE TABLE books (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    book_name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    FULLTEXT KEY ft_books (title, book_name, description)
) ENGINE=InnoDB;


INSERT INTO books (title, book_name, description) VALUES
('Database Management', 'DBMS Fundamentals', 'Introduction to databases, tables, keys, normalization, and SQL.'),
('Programming in C', 'C Programming Complete Guide', 'Learn C programming fundamentals, functions, arrays, pointers, and structures.'),
('Data Structures', 'Data Structures and Algorithms', 'Covers arrays, linked lists, stacks, queues, trees, graphs, and algorithms.'),
('Web Development', 'Modern Web Development', 'Learn HTML, CSS, JavaScript, responsive design, and web development concepts.'),
('Python Programming', 'Python for Beginners', 'A beginner-friendly guide to Python programming and problem solving.'),
('Artificial Intelligence', 'Introduction to AI', 'Learn the fundamentals of artificial intelligence and intelligent systems.'),
('Machine Learning', 'Machine Learning Basics', 'Introduction to machine learning algorithms, models, training, and evaluation.'),
('Computer Networks', 'Computer Networking Essentials', 'Learn networking concepts, protocols, IP addresses, TCP/IP, and network security.'),
('Operating Systems', 'Operating System Concepts', 'Covers processes, threads, memory management, file systems, and scheduling.'),
('Software Engineering', 'Software Engineering Principles', 'Introduction to software development life cycle, requirements, testing, and maintenance.');

SELECT *
FROM books
WHERE MATCH(title, book_name, description)
AGAINST('programming');


-- spatial index: to find particular location in geometry

create table booking(name varchar(50),contact varchar (50),
location geometry not null srid 4326 , spatial index(location));

insert into booking values('abc','7776948877',ST_GeomFromText('linestring(2 1,6 6)',4326));
SELECT
    name,
    contact,
    ST_AsText(location) AS location
FROM booking;


-- Normarlization

-- pl/sql

-- functions in pl/sql 

show databases;
use college;

delimiter $$
create function square(num int)
returns int
deterministic
begin 
 return num*num;
end $$
 delimiter ;
 select square(5);
 
 -- addition 
 delimiter $$
 create function addition(a int,b int)
 returns int
 deterministic
 begin
  return a+b;
 end $$;
  delimiter ;
  
 select addition(4,5); 
 
 
 delimiter $$
 create function even_odd(val int)
 returns varchar(10)
 deterministic
 begin
  if val%2=0 then
  return "even";
  else
  return "odd";
  end if;
 end $$ 
   delimiter ;
   select even_odd(5);
 


-- positive 
delimiter $$
create function p_n(a int )
returns varchar(25)
deterministic
begin
 if a>=0 then
 return "positive";
 else 
 return "negative";
 end if;
 end $$
 delimiter ;
 select p_n(-1);
 

-- greater 
delimiter $$
create function compare(a int , b int )
returns varchar(25)
deterministic
begin
if a>b then
return "a is greater";
else
return "b is greater";
end if;
end $$;
delimiter ;

select compare(6,5);

drop function compare;

-- eligible for vote 
delimiter $$ 
create function eligible(age int )
returns varchar(20)
deterministic
begin
if age>18 then
return "eligible";
else
return "not eligible";
end if ;
end $$;
delimiter ;

select eligible(9);

--  concat two strings
delimiter $$
create function add_string( str1 varchar(100), str2 varchar(100))
returns varchar(100)
deterministic
begin
  return concat(str1,str2);
  end $$
  delimiter ;
  
  select add_string("shiv ","ghantewar");

-- control statement

delimiter $$
create function check_if_else( val int)
returns varchar(100)
deterministic
begin
declare result varchar(20);
 if val=20 then
  set result="value is 20";
elseif val=10 then
  set result="value is 10";
else
  set result="enter 10 or 20";
end if;
return result;
end $$
delimiter ;
 select check_if_else(10);
  
--  grade system
delimiter $$
create function grade(marks int)
returns varchar (100)
deterministic
begin
 if marks<=100 AND marks>=90 then
  return "A+ Grade";
elseif marks<90 AND marks>=75 then
  return "B+ Grade";
elseif marks<75 AND marks>=50 then
  return "c+ Grade";
elseif marks<50 AND marks>=35 then
  return "D+ Grade";  
elseif marks<35 AND marks>=0 then
  return "fail";   
else
  return "enter valid number";
end if;
end $$
delimiter ;

select grade(76);

-- case 

delimiter $$
create function check_case(val int)
returns varchar (100)
deterministic
begin
declare level varchar (20);
case val
  when 10000  then 
    set level="low level";
  when 20000 then 
    set level="mid level";
  else
    set level="high income";
end case;
return level;
end $$
delimiter ;

select check_case(50000); 


-- loop
delimiter $$
create function cal_income(val int)
returns int 
deterministic
begin
  declare income int;
  set income=0;
  label:LOOP
   set income=income+val;
   if income<3000 then 
     iterate label;
     end if;
     leave label;
    end loop label;
    return income;
end $$
delimiter ;

select cal_income(567);

-- i increament 
delimiter $$
create function looping( )
returns int 
deterministic
begin
declare i int;
declare sum int default 0 ;

set i=5;
   label:LOOP
     set sum=sum+i;
     if sum<30 then
     iterate label;
     end if;
     leave label;
     end loop label;
     return sum;
end $$
delimiter ;

select looping();

drop function  looping;
     
  
  
  ------------------- procedure -------------------
show databases;
use hospital;

create table students (id int,name varchar (100));

-------------------- create -------------------
delimiter $$
create procedure registration (in i int,in n varchar(100))
begin
insert into students (id ,name) values(i,n);
end $$
delimiter ;

call registration(3,"Anil");
call registration(4,"ganesh");

------------------------- delete --------------------------
delimiter $$
create procedure delete_student(in student_id  int)
begin
delete from students
where id=student_id;
end $$
delimiter ;


SET SQL_SAFE_UPDATES = 0;
call delete_student(2);
select * from students;

drop procedure delete_student;

--------------------------- select ---------------------------

create table student(id int,name varchar(100),age int);
insert into student values(5,'gaju',23),(6,'ravi',23),(7,'pravin',23);
select * from student;


delimiter $$ 
create procedure getStudentage(
	IN student_id int,
    OUT student_age int
    )
    begin 
		select age
        into student_age
        from student
        where id = student_id;
	end $$
    delimiter ;
    
    call getStudentage(5, @age);
    select @age;
 
 drop procedure getstudentage;
 
 show databases;

SELECT * 
FROM student;
 
 
 






  





   
  

  

 






