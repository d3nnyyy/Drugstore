
-- Insert Categories
INSERT INTO `drugstore_fixed`.`category` (`name`) VALUES
('Painkillers'),
('Antibiotics'),
('Vitamins'),
('Allergy Medications'),
('Cold and Flu Remedies');

-- Insert Addresses
INSERT INTO `drugstore_fixed`.`address` (`country_name`, `region_name`, `city_name`, `street_name`, `house_number`) VALUES
('United States', 'California', 'Los Angeles', 'Main Street', 123),
('Canada', 'Ontario', 'Toronto', 'Oak Avenue', 456),
('United Kingdom', 'London', 'London', 'Broadway', 789),
('Australia', 'New South Wales', 'Sydney', 'King Street', 101),
('Germany', 'Bavaria', 'Munich', 'Hauptstrasse', 246);

-- Insert Manufacturers
INSERT INTO `drugstore_fixed`.`manufacturer` (`name`, `phone_number`, `email`, `address_id`) VALUES
('ABC Pharmaceuticals', '+1-555-123-4567', 'info@abcpharma.com', 1),
('XYZ Drugs', '+1-555-987-6543', 'contact@xyzdrugs.com', 2),
('HealthCorp', '+44-20-1234-5678', 'info@healthcorp.co.uk', 3),
('AussieMeds', '+61-2-9876-5432', 'sales@aussiemeds.com', 4),
('Medico GmbH', '+49-89-555-1234', 'info@medico.de', 5);

-- Insert Drugs
INSERT INTO `drugstore_fixed`.`drug` (`name`, `description`, `price`, `expire_date`, `category_name`, `manufacturer_id`) VALUES
('Ibuprofen', 'Pain relief', 9.99, '2024-12-31', 'Painkillers', 1),
('Amoxicillin', 'Antibiotic', 15.99, '2024-11-30', 'Antibiotics', 2),
('Vitamin C', 'Immune support', 5.99, '2023-10-31', 'Vitamins', 3),
('Loratadine', 'Allergy relief', 12.99, '2024-09-30', 'Allergy Medications', 4),
('ColdEze', 'Cold remedy', 8.99, '2024-10-31', 'Cold and Flu Remedies', 5);

-- Insert Customers
INSERT INTO `drugstore_fixed`.`customer` (`first_name`, `last_name`, `phone_number`) VALUES
('John', 'Smith', '+1-555-111-1111'),
('Emily', 'Johnson', '+1-555-222-2222'),
('David', 'Williams', '+44-20-1111-1111'),
('Olivia', 'Jones', '+61-2-1111-1111'),
('Sophie', 'Müller', '+49-89-1111-1111');
