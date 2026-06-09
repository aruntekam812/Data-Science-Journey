CREATE database company;
use company;
create table department(
        depid int primary key auto_increment,
        depname varchar(100) not null,
        deploc varchar(100) not null,
        budget bigint not null
);

INSERT INTO department (depname,deploc,budget) values
('HR', 'Bhopal', 500000),
('Finance', 'Indore', 1200000),
('Marketing', 'Delhi', 900000),
('Sales', 'Mumbai', 1500000),
('IT', 'Bengaluru', 2500000),
('Research', 'Hyderabad', 3000000),
('Operations', 'Pune', 1800000),
('Legal', 'Chennai', 700000),
('Administration', 'Jaipur', 600000),
('Customer Support', 'Kolkata', 850000),
('Procurement', 'Ahmedabad', 950000),
('Training', 'Nagpur', 450000),
('Quality Assurance', 'Noida', 1100000),
('Logistics', 'Surat', 1300000),
('Security', 'Lucknow', 550000);


-- select function

SELECT * FROM department;

-- select spacific column
select depname,budget from department;


-- remove duplicate
select distinct depname  from  department;


-- FILTERNING
-- where function

select*from  department where  deploc = 'surat';
select*from  department where  depname = 'HR';
select*from  department where  budget > 2000000;
select*from  department where  depname != 'HR';

-- between or and

select*from department where budget between 450000 and 700000;


-- in 
select*from department  where depid in(1,8,5);
-- not in
select*from department where depid not in(1,8,5);


-- like
select*from department where depname like 'f%';
select*from department where depname like '%s';
select*from department where depname like '%o%';


-- and
select*from department where deploc ='bhopal' and budget < 600000;

-- or
select*from department where deploc ='indore' or budget = 100000;

-- not
select*from department where not deploc = 'indore';

-- change and update budget value
alter table department modify budget varchar(50);
UPDATE department SET budget = null where depid in (1,2);
select*from department;


-- is null
select*from department where budget is null;
-- not null
select*from department where budget is not null;


update department set budget= 1200000 where depid in (2);
select*from department;


-- ascending order sorting

select*from department order by budget ASC;
-- ascending order sorting
select*from department order by budget DESC;

-- limiting
select*from department limit  5;
select*from department limit  10,5;


-- string functions

select*, upper(deploc) as udeploc FROM department;

select *, lower(depname) as ldepname from department;

select concat(depname,'-',deploc) as nameloc from department;

select*,substring((depname),1,3) as depn from department;

select depname, length(depname) from department;


update department set depname = ' HR   ' WHERE depid =1;
select*from department;

select*, depname,trim(depname) from department;
select*from department;

select*from department;
-- aggregate function
select count(*) from department;
select avg(budget) from department;
select sum(budget) from department;
select max(budget) from department;
select  min(budget) from department;

-- group by

select deploc, sum(budget) as depsum from department group by deploc;

select deploc,min(budget) as depmin from department group by deploc;

select deploc, max(budget) as depmax from department group by deploc;

select deploc,count(*) as depcount from department group by deploc;

-- having
select*from department;
select depname,count(*) as contname from department group by depname having count(*) >1;

select deploc,sum(budget) as totalsum from department group by deploc;

use company;

-- primary and foreign key
create table employee(
    empID int primary key ,
    empname varchar(50) not null,
    salary int,
    depID int,
    foreign key(depID) references department(depid)

);

insert into  employee  (empID, empname, salary, depID) VALUES
(101, 'Arun', 45000, 1),
(102, 'Rohit', 52000, 2),
(103, 'Priya', 60000, 3),
(104, 'Anjali', 48000, 1),
(105, 'Vikas', 75000, 4),
(106, 'Neha', 55000, 2),
(107, 'Rahul', 67000, 3),
(108, 'Sneha', 43000, 5),
(109, 'Amit', 82000, 4),
(110, 'Pooja', 50000, 1),
(111, 'Karan', 72000, 2),
(112, 'Simran', 58000, 3),
(113, 'Deepak', 39000, 5),
(114, 'Ritika', 65000, 4),
(115, 'Manish', 47000, 1);


-- INNER JOIN

select e.empID,e.empname,e.salary ,d.depid,d.depname,d.deploc
from employee e INNER JOIN department d on e.depID = d.depid;

update employee set depid = null where empID = 101;
-- LEFT JOIN
select e.empID,e.empname,e.salary,d.depid,d.depname,d.deploc from employee e
left join department d on e.depID=d.depid;

-- right join
select e.empID,e.empname,e.salary,d.depid,d.depname,d.deploc from employee e
right join department d on e.depID=d.depid;



-- union
select empID,empname,depID from employee where depId = 1
union
select empID,empname,depID from employee where depId = 2;


-- self join
-- ALTER TABLE employee
-- add managerID INT,
-- add constraint foreign key(managerID) references employee(empID);

-- update employee set managerID = 1 
-- where empID in (103,104)


-- cross join
select e.salary ,d.depname from employee e cross join department d ;


-- subquery 
select max(salary) from employee
where salary<(select max(salary)from employee);

select empname from employee
where depid = (select depid from department where depname='HR');

-- VIEWS
 create VIEW salaryviews AS
 select salary, empname from employee
 where salary>70000;
 SELECT*FROM salaryviews;
 
  create VIEW salaryviews1 AS
 select salary, empname from employee
 where salary>70000;
 select*from salaryviews1;
 
--  index

create index nameindex on employee(empname);
select*from employee where empname='Arun';


--  case statement
select salary,
empname,
case
when salary>75000 then 'high'
when salary between 70000 and 75000 then 'medium'
else 'low'
end as salary_category
from employee;



create view depview as
select d.depname ,count(*)  from employee e
inner join department d on e.depID= d.depid group by d.depname ;
 select*from depview;
 
 
 
--  function
DELIMITER $$
create function getAnnuallSalary(monthSalary INT)
returns int
deterministic
begin
     RETURN monthSalary*12;

end $$
DELIMITER ;

select empname,salary,getAnnuallSalary(salary) as AnnualSalary from employee;


 update employee set salary = 90000 where empID=101;
 
 select empname,salary  from employee;
  select*from salaryviews
  
  
  
--   STORED PROCEDURE

DELIMITER $$
CREATE procedure getempnydep(in depidd int)
begin
select empID,empname,salary from employee
where depID=depidd;

end $$

DELIMITER ;

call getempnydep(1);

-- example
DELIMITER $$
CREATE procedure increasesalary( depidd int,amount int)
begin
 update employee set salary = salary+amount
 where depID=depidd;
end $$
DELIMITER ;
call increasesalary(1,5000);

-- trigger
DELIMITER $$
CREATE TRIGGER beforeadd
before insert on employee
for each row
begin
IF new.salary<0 or new.salary is null then set new.salary =0;
end if;

end $$
DELIMITER ;
insert into  employee  (empID,empname, salary, depID) VALUES
( 151 ,'Attack', -5000, 1);





create table deletebackup(
 backid int auto_increment primary key,
 emp_id int,
 actiontype enum('INSERT','DELETE','UPDATE') NOT NULL,
 ACTIONTIME datetime default current_timestamp,
 remark varchar(255)
);

DELIMITER $$

CREATE TRIGGER deleteddata
after delete on employee
for each row
begin
 INSERT INTO deletebackup(emp_id,actiontype,remark)
 values(old.empID,'DELETE','empdata deleted');
end $$
DELIMITER ;

delete from employee where  empId = 10;


select*from deletebackup;




-- windows function
create table marks (
    student_id int primary key auto_increment,
    name varchar(50),
    branch varchar(50),
    marks int

);

insert  into marks(name,branch,marks)values('Aman', 'CSE', 85),
('Rohit', 'CSE', 92),
('Neha', 'CSE', 78),
('Priya', 'CSE', 88),

('Arjun', 'IT', 81),
('Kavya', 'IT', 95),
('Vikas', 'IT', 73),
('Sneha', 'IT', 87),

('Rahul', 'ECE', 90),
('Anjali', 'ECE', 76),
('Deepak', 'ECE', 84),
('Pooja', 'ECE', 91),

('Manish', 'ME', 69),
('Ritika', 'ME', 82),
('Saurabh', 'ME', 77),
('Nidhi', 'ME', 89);


select branch, avg(marks) from marks group by branch;



-- over()
select*,avg(marks) over(partition by branch )  as totalAVG from marks;

select*, min(marks) over(partition by branch),
max(marks) over(partition by branch) from marks order by student_id;


select*from (select*,
avg(marks)  over(partition by branch) as TAVG  from marks)t where t.marks > TAVG;


-- rank()

select name,branch,marks,
rank() over(partition by branch order by marks DESC) as  rnk from marks;

-- dens_rank()
select name, branch,marks, 
dense_rank() over(partition by branch order by marks DESC) as  drnk from marks;

-- ROW_NUMBER
SELECT name,branch,marks,
row_number() over(partition by branch order by marks DESC ) as RN from marks;







