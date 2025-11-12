USE PPAI;

-- AlcanceSismo
INSERT INTO AlcanceSismo (nombre, descripcion) VALUES
('Local', 'Hasta 100 km del epicentro'),
('Regional', 'Entre 100 y 1000 km del epicentro'),
('Tele-sismo', 'Más de 1000 km del epicentro');

-- ClasificacionSismo
INSERT INTO ClasificacionSismo (kmProfundidadDesde, kmProfundidadHasta) VALUES
(0, 60),   -- Superficial
(61, 300), -- Intermedio
(301, 650);-- Profundo

-- OrigenDeGeneracion
INSERT INTO OrigenDeGeneracion (nombre, descripcion) VALUES
('Interplaca', 'Sismo entre placas tectónicas'),
('Volcánico', 'Sismo por actividad volcánica'),
('Explosiones', 'Sismo por explosiones humanas');

-- Estado (incluyendo los "Autodetectado")
INSERT INTO Estado (ambito, nombreEstado) VALUES
('Evento Sismico', 'Autodetectado'),
('Evento Sismico', 'En evaluación'),
('Evento Sismico', 'Confirmado'),
('Evento Sismico', 'Descartado');

-- EstacionSismologica
INSERT INTO EstacionSismologica (
    codigoEstacion, nombre, latitud, longitud,
    nroCertificacionAdquisicion, documentoCertificacionAdq, fechaSolcitudCertificacion
) VALUES
('001', 'Estación San Juan', -31.537500, -68.536389, 'CERT-001', 'cert_sanjuan.pdf', '2024-12-21'),
('002', 'Estación Mendoza', -32.889458, -68.845839, 'CERT-002', 'cert_mendoza.pdf', '2024-12-22');

-- Empleado
INSERT INTO Empleado (nombre, apellido) VALUES
('Lucía', 'González'),
('Pedro', 'Arreguez');

-- Usuario
INSERT INTO Usuario (nombreUsuario, password, empleado_id) VALUES
('LuciaGonz', '21Lucia', 1),
('PedroArr', '123Pedro', 2);

-- Sesion
INSERT INTO Sesion (fechaHoraDesde, fechaHoraHasta, usuario_id) VALUES
('2025-11-10 09:00:00', '2025-11-10 17:00:00', 1);

-- Sismografo
INSERT INTO Sismografo (fechaAdquisicion, identificadorSismografo, nroSerie, estacionSismologica_id) VALUES
('2024-12-22', 'SISMO-001', 'SN7156', 1),
('2024-12-22', 'SISMO-002', 'SN7157', 2);

-- EventoSismico
INSERT INTO EventoSismico (
    fechaHoraOcurrencia, fechaHoraFin, latitudEpicentro, latitudHipocentro,
    longitudEpicentro, longitudHipocentro, valorMagnitud,
    clasificacion_id, origenGeneracion_id, alcanceSismo_id, estadoActual_id
) VALUES
('2025-11-06 20:15:00', '2025-11-06 20:20:00', -31.5, -32.0, -68.5, -69.0, 6.0, 1, 1, 1, 1),
('2024-11-05 16:40:00', '2024-11-05 16:50:00', -32.9, -33.1, -68.8, -69.1, 4.2, 2, 2, 1, 1),
('2025-01-10 06:00:00', '2025-01-10 06:05:00', -10.1, -10.5, -74.3, -74.6, 6.1, 2, 3, 2, 1),
('2025-04-15 14:30:00', '2025-04-15 14:35:00', -33.7, -34.0, -70.7, -70.9, 8.0, 1, 3, 3, 1),
('2025-07-20 22:45:00', '2025-07-20 22:50:00', 35.1, 35.8, 139.6, 139.9, 4.5, 2, 3, 2, 1);

-- SerieTemporal
INSERT INTO SerieTemporal (
    condicionAlarma, fechaHoraInicioRegistroMuestras,
    fechaHoraRegistro, frecuenciaMuestreo,
    eventoSismico_id, sismografo_id
) VALUES
(FALSE, '2025-11-06 20:10:00', '2025-11-06 20:11:00', 5, 1, 1),
(FALSE, '2025-05-20 20:15:00', '2025-05-20 20:16:00', 5, 2, 2);

-- TipoDeDato
INSERT INTO TipoDeDato (denominacion, nombreUnidadMedida, valorUmbral) VALUES
('Velocidad de Onda', 'km/s', 100),
('Frecuencia de Onda', 'Hz', 50),
('Longitud de Onda', 'km', 200);

-- MuestraSismica
INSERT INTO MuestraSismica (fechaHoraMuestra, serieTemporal_id) VALUES
('2025-11-06 20:15:00', 1),
('2025-11-06 20:20:00', 1),
('2024-10-20 16:40:00', 2),
('2024-10-20 16:45:00', 2);

-- DetalleMuestraSismica
INSERT INTO DetalleMuestraSismica (valor, tipoDeDato_id, muestraSismica_id) VALUES
(50.0, 1, 1),
(20.0, 2, 1),
(180.0, 3, 1),

(55.0, 1, 2),
(22.0, 2, 2),
(175.0, 3, 2),

(48.0, 1, 3),
(19.0, 2, 3),
(190.0, 3, 3),

(52.0, 1, 4),
(21.0, 2, 4),
(185.0, 3, 4);
