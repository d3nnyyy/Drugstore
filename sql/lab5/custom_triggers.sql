DELIMITER //
CREATE TRIGGER before_insert_drug
    BEFORE INSERT
    ON `drugstore_fixed`.`drug`
    FOR EACH ROW
BEGIN
    DECLARE price_suffix VARCHAR(2);

    SET price_suffix = SUBSTRING(NEW.price, CHAR_LENGTH(NEW.price) - 1);

    IF price_suffix = '00' THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'The price cannot end with 00';
    END IF;
END;
//
DELIMITER ;

INSERT INTO `drugstore_fixed`.`drug` (name, description, price, expire_date, category_name, manufacturer_id)
VALUES ('Sample Drug', 'Description', '10.00', '2023-12-31', 'Painkillers', 1);

DELIMITER //
CREATE TRIGGER before_insert_update_customer
    BEFORE INSERT
    ON `drugstore_fixed`.`customer`
    FOR EACH ROW
BEGIN
    DECLARE valid_name BOOLEAN;

    SET valid_name = NEW.first_name IN ('Svitlana', 'Petro', 'Olha', 'Taras');

    IF NOT valid_name THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'The firstname must be one of the following: Svitlana, Petro, Olha, Taras';
    END IF;
END;
//
DELIMITER ;

INSERT INTO `drugstore_fixed`.`customer` (first_name, last_name, phone_number)
VALUES ('John', 'Doe', '1234567890');

DELIMITER //
CREATE TRIGGER before_update_category
BEFORE UPDATE ON `drugstore_fixed`.`category`
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'You cannot update the category table';
END;
//
DELIMITER ;

UPDATE `drugstore_fixed`.`category`
SET name = 'Not Painkillers'
WHERE name = 'Painkillers';