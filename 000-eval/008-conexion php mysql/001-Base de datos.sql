--Iniciamos nuestro usuario en la terminal--
sudo mysql -u root -p

--Cramos la base de datos 'blogphp'--
CREATE DATABASE blogphp;

--Usamos la base de datos recien creada--
USE blogphp;

--Creamos la tabla blog y añadimos campos como: id, titulo, fecha, autor, contenido.--
CREATE TABLE blog(
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    fecha DATE,
    autor VARCHAR(200),
    contenido TEXT
);