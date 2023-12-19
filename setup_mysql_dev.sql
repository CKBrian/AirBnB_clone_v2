-- creates a database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creates a new user hbnb_dev (in localhost) with password of hbnb_dev set to hbnb_dev_pwd
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

-- grants all privileges on the database hbnb_dev_db (and only this database) to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;

-- grants SELECT privilege on the database performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
