-- Creates the database hbtn_0d_usa and table states.
-- CREATE DATABASE creates a database with the given name.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- USE statement tells MySQL to use named database as the default (current) database.
USE hbtn_0d_usa;
-- AUTO_INCREMENT attribute can be used to generate an unique identity for new rows.
-- Primary key for a table represents the column/set of columns used in your most vital queries.
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256));
