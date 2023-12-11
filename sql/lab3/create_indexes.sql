-- category
CREATE INDEX idx_category_name ON category (name);

-- address
CREATE INDEX idx_address_city_name ON address (city_name);
CREATE INDEX idx_address_country ON address (country_name);

-- manufacturer
CREATE INDEX idx_manufacturer_name ON manufacturer (name);
CREATE INDEX idx_manufacturer_email ON manufacturer (email);

-- customer
CREATE INDEX idx_customer_first_name ON customer (first_name);
CREATE INDEX idx_customer_last_name ON customer (last_name);

-- drug
CREATE INDEX idx_drug_description ON drug (description);
CREATE INDEX idx_drug_name ON drug (name);

-- order
CREATE INDEX idx_order_date ON `order` (date);
CREATE INDEX idx_order_price ON `order` (price);

-- review
CREATE INDEX idx_review_rating ON review (rating);
CREATE INDEX idx_review_comment ON review (comment);