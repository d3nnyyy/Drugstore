DELIMITER //
CREATE PROCEDURE receipt_insert(
    IN p_customer_id INT,
    IN p_name VARCHAR(255)
)
BEGIN
    INSERT INTO receipt(customer_id, name)
    VALUES(p_customer_id, p_name);
END //
DELIMITER ;

CALL receipt_insert(1, 'test');

CREATE PROCEDURE insert_order_drug(
    IN p_order_id INT,
    IN p_drug_id INT
)
BEGIN
    INSERT INTO order_has_drug(order_id, drug_id)
    VALUES(p_order_id, p_drug_id);
END;

CALL insert_order_drug(1, 1);