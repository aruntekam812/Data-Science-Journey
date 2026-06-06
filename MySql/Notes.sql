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

select deploc,sum(budget) as totalsum from department group by deploc
