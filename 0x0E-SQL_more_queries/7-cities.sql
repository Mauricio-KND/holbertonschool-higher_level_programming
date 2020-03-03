-- Creates the database hbtn_0d_usa and the table cities.
-- CREATE DATABASE creates a database with the given name.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- CREATE DATABASE creates a database with the given name.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    -- The UNIQUE constraint ensures that all values in a column are different.
    -- Primary key for a table represents the column/set of columns used in your most vital queries.
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       state_id INT NOT NULL,
       FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states (id),
       name VARCHAR(256) NOT NULL
);
