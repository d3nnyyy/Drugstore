DELIMITER //
CREATE FUNCTION max_price_drug()
    RETURNS DECIMAL(10,2)
    DETERMINISTIC
    NO SQL
BEGIN
    DECLARE max DECIMAL(10,2);
    SELECT max(price) INTO max FROM drug;
    RETURN max;
END;

DELIMITER ;

CREATE PROCEDURE display_max_price_drug()
BEGIN
    SELECT max_price_drug() AS 'Max Price of Drug';
END;

CALL display_max_price_drug();