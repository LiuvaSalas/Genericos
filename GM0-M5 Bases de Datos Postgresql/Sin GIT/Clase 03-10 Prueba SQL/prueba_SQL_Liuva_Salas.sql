PARTE I

--nombre de la base de datos para prueba prueba_peliculas

-- Creamos la base de datos
CREATE DATABASE prueba_sql_liuva;

-- Nos conectamos a la base de datos
\c prueba_sql_peliculas;

-- Creamos las tablas indicadas en el requerimiento
-- Tabla para Tags
CREATE TABLE Tags(
id INTEGER PRIMARY KEY,
tag VARCHAR(32));

-- Tabla Peliculas
CREATE TABLE Peliculas(
id INTEGER PRIMARY KEY,
nombre VARCHAR(255),
anno INTEGER);

-- Tabla para Referencias
CREATE TABLE referencias_peliculas(
pelicula INTEGER REFERENCES Peliculas(id),
tag INTEGER REFERENCES Tags(id));

-- Importamos los archivos CSV a las tablas correspondientes
-- Peliculas
COPY Peliculas FROM 'C:\Users\Liuva\Desktop\Desafio_Latam_G20\GM0-M5 Bases de Datos Postgresql\Clase 03-10 Prueba SQL\peliculas.csv' DELIMITER ',' CSV HEADER;

-- Tags
COPY Tags FROM 'C:\Users\Liuva\Desktop\Desafio_Latam_G20\GM0-M5 Bases de Datos Postgresql\Clase 03-10 Prueba SQL\tags.csv' DELIMITER ',' CSV HEADER;

-- Tags
COPY referencias_peliculas FROM 'C:\Users\Liuva\Desktop\Desafio_Latam_G20\GM0-M5 Bases de Datos Postgresql\Clase 03-10 Prueba SQL\relacion.csv' DELIMITER ',' CSV HEADER;

-- Consultas Requeridas
-- 1. Cuenta la cantidad de tags que tiene cada película. Si una película no tiene tags debe mostrar 0.

SELECT p.nombre, COUNT(rp.tag) AS "Cantidad de Tags"
FROM Peliculas p
LEFT JOIN referencias_peliculas rp ON p.id = rp.pelicula
GROUP BY p.nombre;

\q;

PARTE II

-- Creamos las tablas requeridas en la parte II
-- Tabla Preguntas
CREATE TABLE Preguntas(
id INTEGER PRIMARY KEY,
pregunta VARCHAR(255),
respuesta_correcta VARCHAR);

-- Tabla Usuarios
CREATE TABLE Usuarios(
id INTEGER PRIMARY KEY,
nombre VARCHAR(255),
edad INTEGER);

-- Tabla Respuestas
CREATE TABLE Preguntas(
id INTEGER PRIMARY KEY,
respuesta VARCHAR(255),
usuario_id INTEGER REFERENCES Usuarios(id),
pregunta_id INTEGER REFERENCES Preguntas(id));

--Insertamos datos a las tablas
-- Preguntas
COPY Preguntas FROM 'C:\Users\Liuva\Desktop\Desafio_Latam_G20\GM0-M5 Bases de Datos Postgresql\Clase 03-10 Prueba SQL\preguntas.csv' DELIMITER ',' CSV HEADER;

-- Usuarios
COPY Usuarios FROM 'C:\Users\Liuva\Desktop\Desafio_Latam_G20\GM0-M5 Bases de Datos Postgresql\Clase 03-10 Prueba SQL\usuarios.csv' DELIMITER ',' CSV HEADER;

-- Respuestas
COPY Respuestas FROM 'C:\Users\Liuva\Desktop\Desafio_Latam_G20\GM0-M5 Bases de Datos Postgresql\Clase 03-10 Prueba SQL\respuestas.csv' DELIMITER ',' CSV HEADER;

-- Consultas Requeridas
-- 1. Cuenta la cantidad de respuestas correctas totales por usuario (independiente de la
pregunta).

-- 2. Por cada pregunta, en la tabla preguntas, cuenta cuántos usuarios tuvieron la
respuesta correcta.


-- Otro requerimiento
-- 3. Implementa borrado en cascada de las respuestas al borrar un usuario y borrar el
primer usuario para probar la implementación.

-- Alteramos la composicion de la columna usuario_id
ALTER TABLE Respuestas
DROP CONSTRAINT respuestas_usuario_id_fkey,
ADD CONSTRAINT fk_respuestas_usuario FOREIGN KEY (usuario_id) REFERENCES Usuarios(id) ON DELETE CASCADE;

-- Eliminamos el primer usuario
DELETE FROM Usuarios WHERE id = 1;

-- 4. Crea una restricción que impida insertar usuarios menores de 18 años en la base de datos.
ALTER TABLE Usuarios
ADD CONSTRAINT check_edad CHECK (edad >= 18);

-- 5. Altera la tabla existente de usuarios agregando el campo email con la restricción de único.
ALTER TABLE Usuarios
ADD COLUMN email VARCHAR(255) UNIQUE;





