CREATE TABLE receipt
(
    id   INT          NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    customer_id INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TRIGGER insert_receipt
    BEFORE INSERT
    ON receipt
    FOR EACH ROW
BEGIN
    IF NOT EXISTS(SELECT id FROM customer WHERE id = NEW.customer_id) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'customer_id does not exist';
    END IF;
END;

INSERT INTO `receipt` (name, customer_id)
VALUES ('Receipt 1', 999);

CREATE TRIGGER update_receipt
    BEFORE UPDATE
    ON receipt
    FOR EACH ROW
BEGIN
    IF NOT EXISTS(SELECT id FROM customer WHERE id = NEW.customer_id) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'customer_id does not exist';
    END IF;
END;

UPDATE `receipt`
SET customer_id = 999
WHERE id = 1;

CREATE TRIGGER delete_receipt
    BEFORE DELETE
    ON customer
    FOR EACH ROW
BEGIN
    DELETE FROM receipt WHERE customer_id = OLD.id;
END;

DELETE FROM `customer`
WHERE id = 1;