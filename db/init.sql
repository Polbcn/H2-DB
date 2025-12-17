-- =========================
-- Base de datos del laboratorio de H2 (UPC)
-- =========================
-- Tabla de locaciones
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    locacion VARCHAR(100) NOT NULL,
    description TEXT
);
-- Tabla de equipos
CREATE TABLE equipment (
    id SERIAL PRIMARY KEY,
    location_id INT REFERENCES locations(id) ON DELETE SET NULL,
    name VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(100),
    serial_number VARCHAR(100),
    installation_date DATE,
    lifetime_years FLOAT,
    description TEXT
);

-- Tabla de variables
CREATE TABLE variables (
    id SERIAL PRIMARY KEY,
    equipment_id INT REFERENCES equipment(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    unit VARCHAR(20),
    description TEXT
);

-- Tabla de medidas
CREATE TABLE measures (
    id BIGSERIAL PRIMARY KEY,
    variable_id INT REFERENCES variables(id) ON DELETE CASCADE,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    value_min FLOAT,
    value_mean FLOAT NOT NULL,
    value_max FLOAT
);

-- Tabla de costes
CREATE TABLE costs (
    id SERIAL PRIMARY KEY,
    equipment_id INT REFERENCES equipment(id) ON DELETE SET NULL,
    description TEXT,
    amount FLOAT NOT NULL,
    date DATE DEFAULT CURRENT_DATE
);



-- Tabla de relacion entre equipos y locaciones
CREATE TABLE equipment_locations (
    id SERIAL PRIMARY KEY,
    equipment_id INT REFERENCES equipment(id) ON DELETE CASCADE,
    location_id INT REFERENCES locations(id) ON DELETE CASCADE,
    installed_date DATE DEFAULT CURRENT_DATE,
    removed_date DATE,
    description TEXT
);

