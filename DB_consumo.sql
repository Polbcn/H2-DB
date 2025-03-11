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
