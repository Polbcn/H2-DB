-- Tabla de sensores
CREATE TABLE consumo (
    id SERIAL PRIMARY KEY,  -- Usamos SERIAL en lugar de AUTO_INCREMENT
    produccion_total FLOAT NOT NULL,
    presion_baja FLOAT NOT NULL,
    presion_alta FLOAT NOT NULL,
    temperatura_exterior FLOAT NOT NULL,
    masa_baja FLOAT NOT NULL,
    masa_alta FLOAT NOT NULL,
    fecha TIMESTAMP NOT NULL
);
-- Tabla de Sensores LAB
CREATE TABLE Laboratorio (
    id SERIAL PRIMARY KEY,  -- Usamos SERIAL en lugar de AUTO_INCREMENT
    H2S FLOAT NOT NULL,
    NO2 FLOAT NOT NULL,
    O3 FLOAT NOT NULL,
    SO2 FLOAT NOT NULL,
    CO2 FLOAT NOT NULL,
    CO FLOAT NOT NULL,
    TVOC FLOAT NOT NULL,
    fecha TIMESTAMP NOT NULL
);
