
CREATE DATABASE PUBG;
use pubg;
CREATE TABLE users(
   userID int primary key auto_increment,
   username varchar(50) not null,
   useremail varchar(100) unique not null,
   userpassword varchar(200) not null,
   age tinyint check(age >=18),
   userphone int
);

CREATE TABLE department(
     depID int primary key auto_increment,
     depNAME varchar(50) not null

);
# add new column in table 
ALTER TABLE department ADD depempl varchar(100);


-- modify column type size
ALTER TABLE users MODIFY useremail varchar(500) not null;

-- INSERT DATA

INSERT INTO  users (username,useremail,userpassword,age,userphone) VALUES ('Arun','arun@gmail.com','wow@123',22,930196625);
INSERT INTO  users (username,useremail,userpassword,age,userphone) VALUES ('AK','AK@gmail.com','www@123',42,930196625);


-- multiple data insert
INSERT INTO  users (username,useremail,userpassword,age,userphone) VALUES ('ANKIT','ANKIT@gmail.com','ANKIT@123',82,5426546),('EREN','EREN@gmail.com','EREN@123',25,4354625);

-- DELET DATA FROM ROW
DELETE FROM users WHERE userID = 2;

-- delete all data from taBLE
truncate table department;

-- delet entire table
drop table department;


UPDATE users SET 
username = 'eren yeager',
useremail='erenyeager@gmail.com' 
WHERE userID= 4;