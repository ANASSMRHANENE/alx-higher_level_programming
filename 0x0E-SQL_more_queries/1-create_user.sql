-- Check if the user exists
SELECT COUNT(*) INTO @user_exists
FROM mysql.user
WHERE user = 'user_0d_1' AND host = 'localhost';

-- Create user only if it does not exist
SET @create_user_query = IF(@user_exists = 0,
    'CREATE USER ''user_0d_1''@''localhost'' IDENTIFIED BY ''user_0d_1_pwd'';',
    'SELECT ''User user_0d_1 already exists.'';'
);

-- Execute query to create the user
PREPARE create_user_stmt FROM @create_user_query;
EXECUTE create_user_stmt;
DEALLOCATE PREPARE create_user_stmt;

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges
FLUSH PRIVILEGES;
