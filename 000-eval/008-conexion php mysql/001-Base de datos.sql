--Iniciamos nuestro usuario en la terminal--
sudo mysql -u root -p

--Cramos la base de datos 'blogphp'--
CREATE DATABASE IF NOT EXISTS blogphp
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_general_ci;

--Usamos la base de datos recien creada--
USE blogphp;

--Creamos la tabla blog y añadimos campos como: id, titulo, fecha, autor, contenido.--
CREATE TABLE IF NOT EXISTS blog(
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    autor VARCHAR(200) DEFAULT 'Administrador',
    contenido TEXT NOT NULL
);

--Ahora insertamos datos--
INSERT INTO blog (titulo, contenido, autor) VALUES
('Bienvenidos a mi nuevo blog',
    'Este es el primer artículo del blog. Aquí compartiré tutoriales, noticias y recursos útiles sobre programación y tecnología.',
    'Bryan Alejandro Avila Castro'),

('Cómo instalar PHP y Apache en Ubuntu',
    'En este artículo aprenderás a instalar un entorno AMP en Ubuntu utilizando los repositorios oficiales y configurando los módulos necesarios.',
    'Bryan Alejandro Avila Castro'),

('Introducción a SQL para principiantes',
    'SQL es un lenguaje fundamental para trabajar con bases de datos. En esta guía veremos las instrucciones básicas: SELECT, INSERT, UPDATE y DELETE.',
    'Administrador'),

('Consejos para mejorar tu productividad como programador',
    'Organizar el tiempo, dividir el trabajo en tareas pequeñas y mantener un entorno ordenado puede ayudarte a avanzar más rápidamente en tus proyectos.',
    'Administrador');