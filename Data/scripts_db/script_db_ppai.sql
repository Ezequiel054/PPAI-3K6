-- ==========================================================
-- SCRIPT SQL Para MySQL
-- ==========================================================

CREATE SCHEMA PPAI;

USE PPAI;

CREATE TABLE AlcanceSismo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

CREATE TABLE ClasificacionSismo (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    kmProfundidadDesde DECIMAL(10, 2),
    kmProfundidadHasta DECIMAL(10, 2)
);

CREATE TABLE OrigenDeGeneracion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT
);

CREATE TABLE Estado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ambito VARCHAR(100),
    nombreEstado VARCHAR(100)
);

CREATE TABLE EventoSismico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fechaHoraOcurrencia DATETIME,
    fechaHoraFin DATETIME,
    latitudEpicentro DECIMAL(10,6),
    latitudHipocentro DECIMAL(10,6),
    longitudEpicentro DECIMAL(10,6),
    longitudHipocentro DECIMAL(10,6),
    valorMagnitud DECIMAL(4,2),
    clasificacion_id INT,
    origenGeneracion_id INT,
    alcanceSismo_id INT,
    estadoActual_id INT,
    FOREIGN KEY (clasificacion_id) REFERENCES ClasificacionSismo(id),
    FOREIGN KEY (origenGeneracion_id) REFERENCES OrigenDeGeneracion(id),
    FOREIGN KEY (alcanceSismo_id) REFERENCES AlcanceSismo(id),
    FOREIGN KEY (estadoActual_id) REFERENCES Estado(id)
);

CREATE TABLE EstacionSismologica (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigoEstacion VARCHAR(50) NOT NULL,
    nombre VARCHAR(100),
    latitud DECIMAL(10,6),
    longitud DECIMAL(10,6),
    nroCertificacionAdquisicion VARCHAR(50),
    documentoCertificacionAdq VARCHAR(255),
    fechaSolcitudCertificacion DATE
);

CREATE TABLE Sismografo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fechaAdquisicion DATE,
    identificadorSismografo VARCHAR(50) NOT NULL,
    nroSerie VARCHAR(50),
    estacionSismologica_id INT,
    FOREIGN KEY (estacionSismologica_id) REFERENCES EstacionSismologica(id)
);


CREATE TABLE SerieTemporal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    condicionAlarma BOOLEAN,
    fechaHoraInicioRegistroMuestras DATETIME,
    fechaHoraRegistro DATETIME,
    frecuenciaMuestreo DECIMAL(10,2),
    eventoSismico_id INT,
    sismografo_id INT,
    FOREIGN KEY (eventoSismico_id) REFERENCES EventoSismico(id),
    FOREIGN KEY (sismografo_id) REFERENCES Sismografo(id)
);

CREATE TABLE TipoDeDato (
    id INT AUTO_INCREMENT PRIMARY KEY,
    denominacion VARCHAR(100) NOT NULL,
    nombreUnidadMedida VARCHAR(50),
    valorUmbral DECIMAL(10,2)
);

CREATE TABLE MuestraSismica (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fechaHoraMuestra DATETIME NOT NULL,
    serieTemporal_id INT,
    FOREIGN KEY (serieTemporal_id) REFERENCES SerieTemporal(id)
);

CREATE TABLE DetalleMuestraSismica (
    id INT AUTO_INCREMENT PRIMARY KEY,
    valor DECIMAL(10,4),
    tipoDeDato_id INT,
    muestraSismica_id INT,
    FOREIGN KEY (tipoDeDato_id) REFERENCES TipoDeDato(id),
    FOREIGN KEY (muestraSismica_id) REFERENCES MuestraSismica(id)
);

CREATE TABLE Empleado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100)
);

CREATE TABLE CambioEstado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fechaHoraInicio DATETIME,
    fechaHoraFin DATETIME,
    estado_id INT,
    responsableInspeccion_id INT,
    eventoSismico_id INT,
    FOREIGN KEY (estado_id) REFERENCES Estado(id),
    FOREIGN KEY (responsableInspeccion_id) REFERENCES Empleado(id),
    FOREIGN KEY (eventoSismico_id) REFERENCES EventoSismico(id)
);

CREATE TABLE Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombreUsuario VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    empleado_id INT,
    FOREIGN KEY (empleado_id) REFERENCES Empleado(id)
);

CREATE TABLE Sesion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fechaHoraDesde DATETIME,
    fechaHoraHasta DATETIME,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
);