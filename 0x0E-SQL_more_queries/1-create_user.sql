-- Creates the MySQL server user_0d_1.
-- CREATE USER statement creates new MySQL accounts.
-- GRANT statement assigns privileges and roles to MySQL user accounts and roles.
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY "user_0d_1_pwd";
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
