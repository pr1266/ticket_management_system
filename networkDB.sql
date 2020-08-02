--data base created by the game
--1266
--users table for authentication;
create table user_(
    ID_ serial primary key ,
    username varchar(100) not null , 
    password_ varchar(100) not null ,
    api varchar(50) default null unique ,
    --zero for client and one for manager
    role_ int
);

--ticket tables;
create table ticket(
    ID serial primary key,
    sender varchar(50) references user_(api), 
    body varchar(300) ,
    subject_ varchar(100) ,
    response_ varchar(300) ,
    --zero for close and 1 for open and 2 for in queue
    status_ int
)