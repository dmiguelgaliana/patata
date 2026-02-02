DROP DATABASE IF EXISTS nom_mail;
DROP USER IF EXISTS 'nommail_user'@'localhost';

CREATE DATABASE nom_mail;
CREATE USER 'nommail_user'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON nom_mail.* TO 'nommail_user'@'localhost';

USE nom_mail;

CREATE TABLE usuarios (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Mail VARCHAR(100) NOT NULL
);

INSERT INTO usuarios (Nombre, Mail) VALUES
('Diego', 'diego@example.com'),
('Maria', 'maria@gmail.com'),
('Pau', 'pau@hotmail.com');
