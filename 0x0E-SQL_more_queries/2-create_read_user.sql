-- Check if the database exists
SELECT COUNT(*) INTO @db_exists
FROM information_schema.schemata
WHERE schema_name = 'hbtn_0d_2';

-- Create database only if it does not exist
SET @create_db_query = IF(@db_exists = 0,
    'CREATE DATABASE hbtn_0d_2;',
    'SELECT ''Database hbtn_0d_2 already exists.'';'
);

-- Execute the query to create the database
PREPARE create_db_stmt FROM @create_db_query;
EXECUTE create_db_stmt;
DEALLOCATE PREPARE create_db_stmt;

-- Check if the user exists
SELECT COUNT(*) INTO @user_exists
FROM mysql.user
WHERE user = 'user_0d_2' AND host = 'localhost';

-- Create user
SET @create_user_query = IF(@user_exists = 0,
    'CREATE USER ''user_0d_2''@''localhost'' IDENTIFIED BY ''user_0d_2_pwd'';',
    'SELECT ''User user_0d_2 already exists.'';'
);

-- Execute query to create the user
PREPARE create_user_stmt FROM @create_user_query;
EXECUTE create_user_stmt;
DEALLOCATE PREPARE create_user_stmt;

-- Grant SELECT privilege on the database to user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
