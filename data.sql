-- Table for Grocery items
CREATE TABLE grocery (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    stock INT NOT NULL,
    expiration_date DATE NOT NULL
);

-- Table for Meat items
CREATE TABLE meat (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    stock INT NOT NULL,
    cut_type VARCHAR(100) NOT NULL
);

-- Table for Produce items
CREATE TABLE produce (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    stock INT NOT NULL,
    in_season VARCHAR(100) NOT NULL
);


-- Table for Bakery items
CREATE TABLE bakery (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    stock INT NOT NULL,
    pastry_type VARCHAR(100) NOT NULL
);


-- SEED info

-- seed.sql

-- Seed data for Grocery items
INSERT INTO grocery (item_name, stock, expiration_date) VALUES 
('Milk', 50, '2024-12-31'),
('Bread', 100, '2024-11-15'),
('Eggs', 200, '2024-10-10');

-- Seed data for Meat items
INSERT INTO meat (item_name, stock, cut_type) VALUES 
('Chicken Breast', 50, 'Boneless'),
('Pork Chops', 75, 'Bone-in'),
('Ground Beef', 100, 'Lean');

-- Seed data for Produce items
INSERT INTO produce (item_name, stock, in_season) VALUES 
('Apples', 150, 'yes'),
('Bananas', 200, 'yes'),
('Carrots', 100, 'no');

-- Seed data for Bakery items
INSERT INTO bakery (item_name, stock, pastry_type) VALUES 
('Croissant', 100, 'Pastry'),
('Bagel', 120, 'Bread'),
('Muffin', 90, 'Pastry');
