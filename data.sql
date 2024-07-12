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
