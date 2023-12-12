DELIMITER //

CREATE PROCEDURE `create_random_dbs`()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE db_name VARCHAR(255);
    DECLARE num_tables INT;
    DECLARE i INT;
    DECLARE db_cursor CURSOR FOR
        SELECT TABLE_NAME
        FROM information_schema.tables
        WHERE TABLE_SCHEMA = 'drugstore_fixed';
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN db_cursor;

    my_loop: LOOP
        FETCH db_cursor INTO db_name;
        IF done THEN
            LEAVE my_loop;
        END IF;

        SET num_tables = FLOOR(RAND() * 9) + 1;

        SET @query = CONCAT('CREATE DATABASE IF NOT EXISTS `', db_name, '`');
        PREPARE stmt FROM @query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        SET i = 1;
        WHILE i <= num_tables DO
            SET @table_name = CONCAT(db_name, '_', i);
            SET @query = CONCAT(
                'CREATE TABLE IF NOT EXISTS `', db_name, '`.`', @table_name, '` (
                    `id` INT NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(45) NULL,
                    PRIMARY KEY (`id`)
                )'
            );
            PREPARE stmt FROM @query;
            EXECUTE stmt;
            DEALLOCATE PREPARE stmt;
            SET i = i + 1;
        END WHILE;

    END LOOP;

    CLOSE db_cursor;
END //

DELIMITER ;

CALL create_random_dbs();
