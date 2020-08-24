CREATE TABLE TestBank (
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
test_name VARCHAR(32) NOT NULL,
test_steps VARCHAR(512) NOT NULL,
test_description VARCHAR(64) NOT NULL,
creator INT UNSIGNED NOT NULL,
active BOOLEAN DEFAULT FALSE,
creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
update_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id),
FOREIGN KEY (creator) REFERENCES Testers(id) );