-- Lists all cities contained in the database hbtn_0d_usa.
-- LEFT JOIN: Table states is set to depend on table cities.
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
