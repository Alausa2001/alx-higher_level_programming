-- creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows
-- second_table description:
--     id INT
--      name VARCHAR(256)
--      score INT
CREATE TABLE second_table (id int, name varchar(256), score int);
INSERT INTO second_table VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);
