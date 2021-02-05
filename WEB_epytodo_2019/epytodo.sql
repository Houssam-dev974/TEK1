CREATE DATABASE epytodo;
USE epytodo;

CREATE TABLE user
(
    user_id varchar(255) NOT NULL,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL
);

CREATE TABLE task
(
    task_id varchar(20) NOT NULL,
    title varchar(20) NOT NULL,
    begin varchar(10) NOT NULL,
    end varchar(10) NOT NULL,
    status varchar(255) NOT NULL
);

CREATE TABLE user_has_task
(
    fk_user_id int(11) NOT NULL,
    fk_task_id int(11) NOT NULL
);