CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INT AUTO_INCREMENT,
    nombre_usuario VARCHAR(155) NOT NULL,
    contrasenha VARCHAR(55) NOT NULL,
    correo VARCHAR(155) NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_usuario PRIMARY KEY (id_usuario)
);



CREATE TABLE IF NOT EXISTS amistad (
    id_amistad INT AUTO_INCREMENT,
    fecha_amistad DATETIME NOT NULL,
    id_primer_usuario INT NOT NULL,
    id_segundo_usuario INT NOT NULL,

    CONSTRAINT pk_amistad PRIMARY KEY (id_amistad),
    CONSTRAINT fk_primer_usuario FOREIGN KEY(id_primer_usuario)
    REFERENCES usuario(id_usuario),
    CONSTRAINT fk_segundo_usuario FOREIGN KEY(id_segundo_usuario)
    REFERENCES usuario(id_usuario)
);



CREATE TABLE IF NOT EXISTS publicacion(
    id_publicacion INT AUTO_INCREMENT,
    contenido_publicacion TEXT NOT NULL,
    fecha_publicacion DATETIME NOT NULL,
    id_usuario INT NOT NULL,

    CONSTRAINT pk_publicacion PRIMARY KEY (id_publicacion),
    CONSTRAINT fk_usuario FOREIGN KEY(id_usuario)
    REFERENCES usuario(id_usuario)
);



CREATE TABLE IF NOT EXISTS comentario (
    id_comentario INT AUTO_INCREMENT,
    comentario TEXT NOT NULL,
    id_publicacion INT NOT NULL,
    id_usuario INT NOT NULL,

    CONSTRAINT pk_comentario PRIMARY KEY (id_comentario),
    CONSTRAINT fk_publicacion FOREIGN KEY(id_publicacion)
    REFERENCES publicacion(id_publicacion),
    CONSTRAINT fk_usuario FOREIGN KEY(id_usuario)
    REFERENCES usuario(id_usuario)
);


CREATE TABLE IF NOT EXISTS mensaje (
    id_mensaje INT AUTO_INCREMENT,
    contenido_mensaje TEXT NOT NULL,
    fecha_mensaje DATETIME NOT NULL,
    id_primer_usuario INT NOT NULL,
    id_segundo_usuario INT NOT NULL,

    CONSTRAINT pk_mensaje PRIMARY KEY (id_mensaje),
    CONSTRAINT fk_primer_usuario FOREIGN KEY(id_primer_usuario)
    REFERENCES usuario(id_usuario),
    CONSTRAINT fk_segundo_usuario FOREIGN KEY(id_segundo_usuario)
    REFERENCES usuario(id_usuario)
);


CREATE TABLE IF NOT EXISTS me_gusta (
    id_megusta INT AUTO_INCREMENT,
    fecha_megusta DATETIME NOT NULL,
    id_publicacion INT NOT NUll,
    id_usuario INT NOT NULL,

    CONSTRAINT pk_megusta PRIMARY KEY (id_megusta),
    CONSTRAINT fk_publicacion FOREIGN KEY(id_publicacion)
    REFERENCES publicacion(id_publicacion),
    CONSTRAINT fk_usuario FOREIGN KEY(id_usuario)
    REFERENCES usuario(id_usuario)
);