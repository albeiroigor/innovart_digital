CREATE TABLE IF NOT EXISTS roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid CHAR(36) NOT NULL UNIQUE,
    tipo VARCHAR(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid CHAR(36) NOT NULL UNIQUE,
    cedula VARCHAR(50),
    documento VARCHAR(50),
    primer_nombre VARCHAR(100),
    segundo_nombre VARCHAR(100),
    primer_apellido VARCHAR(100),
    segundo_apellido VARCHAR(100),
    correo VARCHAR(150),
    direccion VARCHAR(200),
    telefono VARCHAR(50),
    fecha_nacimiento DATE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid CHAR(36) NOT NULL UNIQUE,
    correo VARCHAR(150) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    personas_id INT,
    CONSTRAINT fk_usuarios_personas
        FOREIGN KEY (personas_id) REFERENCES personas(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS servicios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid CHAR(36) NOT NULL UNIQUE,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2),
    tipo VARCHAR(100),
    estado VARCHAR(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid CHAR(36) NOT NULL UNIQUE,
    roles_id INT,
    res_id INT,
    personas_id INT,
    servicios_id INT,
    CONSTRAINT fk_empleados_roles
        FOREIGN KEY (roles_id) REFERENCES roles(id),
    CONSTRAINT fk_empleados_personas
        FOREIGN KEY (personas_id) REFERENCES personas(id),
    CONSTRAINT fk_empleados_servicios
        FOREIGN KEY (servicios_id) REFERENCES servicios(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS pagos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid CHAR(36) NOT NULL UNIQUE,
    hora TIME,
    fecha DATE,
    monto DECIMAL(10,2),
    metodo_pago VARCHAR(50),
    servicios_id INT,
    usuarios_id INT,
    CONSTRAINT fk_pagos_servicios
        FOREIGN KEY (servicios_id) REFERENCES servicios(id),
    CONSTRAINT fk_pagos_usuarios
        FOREIGN KEY (usuarios_id) REFERENCES usuarios(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS agendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid CHAR(36) NOT NULL UNIQUE,
    fecha DATE,
    hora TIME,
    servicios_id INT,
    usuarios_id INT,
    pagos_id INT,
    CONSTRAINT fk_agendas_servicios
        FOREIGN KEY (servicios_id) REFERENCES servicios(id),
    CONSTRAINT fk_agendas_usuarios
        FOREIGN KEY (usuarios_id) REFERENCES usuarios(id),
    CONSTRAINT fk_agendas_pagos
        FOREIGN KEY (pagos_id) REFERENCES pagos(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS servicios_agenda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid CHAR(36) NOT NULL UNIQUE,
    servicios_id INT,
    agendas_id INT,
    CONSTRAINT fk_servicios_agenda_servicios
        FOREIGN KEY (servicios_id) REFERENCES servicios(id),
    CONSTRAINT fk_servicios_agenda_agendas
        FOREIGN KEY (agendas_id) REFERENCES agendas(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS consultas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid CHAR(36) NOT NULL UNIQUE,
    hora TIME,
    fecha DATE,
    mensaje TEXT,
    usuarios_id INT,
    CONSTRAINT fk_consultas_usuarios
        FOREIGN KEY (usuarios_id) REFERENCES usuarios(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS respuestas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid CHAR(36) NOT NULL UNIQUE,
    hora TIME,
    descripcion TEXT,
    fecha DATE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
