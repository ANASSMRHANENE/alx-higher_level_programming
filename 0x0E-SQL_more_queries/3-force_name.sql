SET @db_name = ?;

-- Check if the table exists in the specified database
SELECT COUNT(*) INTO @table_exists
FROM information_schema.tables
WHERE table_schema = @db_name AND table_name = 'force_name';

-- Create the table only if it does not exist
SET @create_table_query = IF(@table_exists = 0,
    CONCAT('
        USE ', @db_name, ';
        CREATE TABLE force_name (
            id INT,
            name VARCHAR(256) NOT NULL
        );
    '),
    'SELECT ''Table force_name already exists.'';'
);

-- Execute the query to create the table
PREPARE create_table_stmt FROM @create_table_query;
EXECUTE create_table_stmt;
DEALLOCATE PREPARE create_table_stmt;
