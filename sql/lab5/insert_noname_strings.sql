DELIMITER //
CREATE PROCEDURE `insert_10_nonames_into_receipt`(
    IN p_customer_id INT
)
BEGIN
    DECLARE counter INT DEFAULT 1;

    WHILE counter <= 10 DO
        INSERT INTO receipt (customer_id, name)
        VALUES (p_customer_id, CONCAT('Noname', counter));
        SET counter = counter + 1;
    END WHILE;

END //
DELIMITER ;

CALL insert_10_nonames_into_receipt(1);