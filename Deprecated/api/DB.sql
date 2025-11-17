-- Tabla de sensores
CREATE TABLE sensores (
    id_sensor SERIAL PRIMARY KEY,  -- Usamos SERIAL en lugar de AUTO_INCREMENT
    nombre_sensor VARCHAR(50) NOT NULL,
    descripcion_sensor VARCHAR(100),
    tipo_sensor VARCHAR(50) NOT NULL,
    ubicacion VARCHAR(50) NOT NULL,
    coste FLOAT
);

-- Tabla de mediciones
CREATE TABLE mediciones (
    id_medicion SERIAL PRIMARY KEY,  -- Usamos SERIAL en lugar de AUTO_INCREMENT
    id_sensor INT REFERENCES sensores(id_sensor) ON DELETE CASCADE,
    fecha_hora TIMESTAMP NOT NULL,  -- Usamos TIMESTAMP en lugar de DATETIME
    valor FLOAT NOT NULL
);

-- Tabla usuarios
CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,  -- Usamos SERIAL en lugar de AUTO_INCREMENT
    nombre_usuario VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    rol VARCHAR(50) CHECK (rol IN ('admin', 'user')) NOT NULL
);
