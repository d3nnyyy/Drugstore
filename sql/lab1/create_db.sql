-- -----------------------------------------------------
-- Schema drugstore_fixed
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `drugstore_fixed` DEFAULT CHARACTER SET utf8 ;
USE `drugstore_fixed` ;
-- -----------------------------------------------------
-- Table `drugstore_fixed`.`category`
-- -----------------------------------------------------

-- Drop Table `drugstore_fixed`.`order_has_drug`
DROP TABLE IF EXISTS `drugstore_fixed`.`order_has_drug`;

-- Drop Table `drugstore_fixed`.`order`
DROP TABLE IF EXISTS `drugstore_fixed`.`order`;

-- Drop Table `drugstore_fixed`.`review`
DROP TABLE IF EXISTS `drugstore_fixed`.`review`;

-- Drop Table `drugstore_fixed`.`customer`
DROP TABLE IF EXISTS `drugstore_fixed`.`customer`;

-- Drop Table `drugstore_fixed`.`drug`
DROP TABLE IF EXISTS `drugstore_fixed`.`drug`;

-- Drop Table `drugstore_fixed`.`manufacturer`
DROP TABLE IF EXISTS `drugstore_fixed`.`manufacturer`;

-- Drop Table `drugstore_fixed`.`address`
DROP TABLE IF EXISTS `drugstore_fixed`.`address`;

-- Drop Table `drugstore_fixed`.`category`
DROP TABLE IF EXISTS `drugstore_fixed`.`category`;


CREATE TABLE IF NOT EXISTS `drugstore_fixed`.`category` (
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`name`))
;

-- -----------------------------------------------------
-- Table `drugstore_fixed`.`address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `drugstore_fixed`.`address` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `country_name` VARCHAR(45) NULL,
  `region_name` VARCHAR(45) NULL,
  `city_name` VARCHAR(45) NULL,
  `street_name` VARCHAR(45) NULL,
  `house_number` INT NULL,
  PRIMARY KEY (`id`))
;


-- -----------------------------------------------------
-- Table `drugstore_fixed`.`manufacturer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `drugstore_fixed`.`manufacturer` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `phone_number` VARCHAR(20) NULL,
  `email` VARCHAR(45) NULL,
  `address_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_manufacturer_address1_idx` (`address_id` ASC) ,
  CONSTRAINT `fk_manufacturer_address1`
    FOREIGN KEY (`address_id`)
    REFERENCES `drugstore_fixed`.`address` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `drugstore_fixed`.`drug`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `drugstore_fixed`.`drug` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `price` DECIMAL(4,2) NULL,
  `expire_date` DATE NULL,
  `category_name` VARCHAR(45) NOT NULL,
  `manufacturer_id` INT NOT NULL,
  PRIMARY KEY (`id`, `category_name`, `manufacturer_id`),
  INDEX `fk_drug_category1_idx` (`category_name` ASC) ,
  INDEX `fk_drug_manufacturer1_idx` (`manufacturer_id` ASC) ,
  CONSTRAINT `fk_drug_category1`
    FOREIGN KEY (`category_name`)
    REFERENCES `drugstore_fixed`.`category` (`name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_drug_manufacturer1`
    FOREIGN KEY (`manufacturer_id`)
    REFERENCES `drugstore_fixed`.`manufacturer` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `drugstore_fixed`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `drugstore_fixed`.`customer` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `phone_number` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `drugstore_fixed`.`review`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `drugstore_fixed`.`review` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment` VARCHAR(45) NULL,
  `rating` INT NOT NULL,
  `drug_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`id`, `drug_id`, `customer_id`),
  INDEX `fk_review_drug1_idx` (`drug_id` ASC) ,
  INDEX `fk_review_customer1_idx` (`customer_id` ASC) ,
  CONSTRAINT `fk_review_drug1`
    FOREIGN KEY (`drug_id`)
    REFERENCES `drugstore_fixed`.`drug` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_review_customer1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `drugstore_fixed`.`customer` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `drugstore_fixed`.`order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `drugstore_fixed`.`order` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `price` DECIMAL NOT NULL,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`id`, `customer_id`),
  INDEX `fk_order_customer1_idx` (`customer_id` ASC) ,
  CONSTRAINT `fk_order_customer1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `drugstore_fixed`.`customer` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;

-- -----------------------------------------------------
-- Table `drugstore_fixed`.`order_has_drug`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `drugstore_fixed`.`order_has_drug` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `drug_id` INT NOT NULL,
  PRIMARY KEY (`id`, `order_id`, `drug_id`),
  INDEX `fk_order_has_drug_drug1_idx` (`drug_id` ASC) ,
  INDEX `fk_order_has_drug_order1_idx` (`order_id` ASC) ,
  CONSTRAINT `fk_order_has_drug_order1`
    FOREIGN KEY (`order_id`)
    REFERENCES `drugstore_fixed`.`order` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_has_drug_drug1`
    FOREIGN KEY (`drug_id`)
    REFERENCES `drugstore_fixed`.`drug` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;