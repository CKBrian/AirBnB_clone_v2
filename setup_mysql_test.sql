-- creates a database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbtn_test_db;

-- creates a new user hbnb_test (in localhost) with hbnb_test_pwd password
CREATE USER IF NOT EXISTS hbtn_test@localhost IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges all privileges on hbtn_test_db to hbtn_test
GRANT ALL PRIVILEGES ON hbtn_test_db.* TO hbnb_test@localhost;

-- Grant privileges all privileges on performance_schema to hbtn_test
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
