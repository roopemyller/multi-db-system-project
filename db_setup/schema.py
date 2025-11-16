
SCHEMA = """
CREATE TABLE IF NOT EXISTS brands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100),
    founded_year INTEGER
);

CREATE TABLE IF NOT EXISTS camera_types (
    id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS cameras (
    id SERIAL PRIMARY KEY,
    brand_id INTEGER REFERENCES brands(id),
    type_id INTEGER REFERENCES camera_types(id),
    model_name VARCHAR(200) NOT NULL,
    release_year INTEGER,
    price DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS lenses (
    id SERIAL PRIMARY KEY,
    brand_id INTEGER REFERENCES brands(id),
    focal_length VARCHAR(50),
    aperture VARCHAR(50),
    lens_type VARCHAR(100),
    price DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS accessories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10, 2),
    compatible_brands TEXT
);
"""