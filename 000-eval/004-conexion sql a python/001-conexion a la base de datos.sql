--Creamos la base de datos 'clientes' creamos una tabla clientes le damos los campos 'nombre, apellidos y edad' y le insertamos datos a la tabla. 

CREATE DATABASE clientes;

USE clientes;

CREATE TABLE clientes(
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  edad INT
);

INSERT INTO clientes VALUES ("Juan","Lopez",45);
INSERT INTO clientes VALUES ("Javier","Martinez",46);

--Creamos un usuario y le damos permisos.

CREATE USER 
'clientes'@'localhost' 
IDENTIFIED  BY 'Clientes123$';

GRANT USAGE ON *.* TO 'clientes'@'localhost';

ALTER USER 'clientes'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON clientes.* 
TO 'clientes'@'localhost';

FLUSH PRIVILEGES;

