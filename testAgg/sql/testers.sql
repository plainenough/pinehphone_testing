CREATE TABLE Testers (
id int UNSIGNED AUTO_INCREMENT,
email VARCHAR(32) NOT NULL,
first_name VARCHAR(32) NOT NULL,
last_name VARCHAR(32) NOT NULL,
user_passwd CHAR(64) NOT NULL,
creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id) );
