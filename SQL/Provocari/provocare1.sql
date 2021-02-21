CREATE SCHEMA `provocare1` DEFAULT CHARACTER SET utf8;

CREATE TABLE `provocare1`.`student`
(
    `idstudent`      INT         NOT NULL AUTO_INCREMENT,
    `numar_matricol` CHAR(10)    NOT NULL,
    `cnp`            INT(13)     NOT NULL,
    `nume`           VARCHAR(70) NOT NULL,
    `prenume`        VARCHAR(70) NOT NULL,
    `data_nasterii`  DATE        NOT NULL,
    PRIMARY KEY (`idstudent`, `cnp`),
    UNIQUE INDEX `numar_matricol_UNIQUE` (`numar_matricol` ASC) VISIBLE,
    UNIQUE INDEX `idstudent_UNIQUE` (`idstudent` ASC) VISIBLE,
    UNIQUE INDEX `CNP_UNIQUE` (`cnp` ASC) VISIBLE
);

CREATE TABLE `provocare1`.`profesor`
(
    `idprofesor`     INT         NOT NULL AUTO_INCREMENT,
    `numar_matricol` CHAR(10)    NOT NULL,
    `nume`           VARCHAR(70) NULL,
    `prenume`        VARCHAR(70) NULL,
    `titularizare`   VARCHAR(10) NULL DEFAULT 'titular' COMMENT 'Can be titular or asistent',
    PRIMARY KEY (`idprofesor`),
    UNIQUE INDEX `numar_matricol_UNIQUE` (`numar_matricol` ASC) VISIBLE,
    UNIQUE INDEX `idprofesor_UNIQUE` (`idprofesor` ASC) VISIBLE
);

CREATE TABLE `provocare1`.`examen`
(
    `idexamen`        INT         NOT NULL AUTO_INCREMENT,
    `numar_examen`    INT(10)     NULL,
    `denumire_examen` VARCHAR(70) NULL,
    `sala_examen`     VARCHAR(45) NULL,
    `ora_examen`      DATETIME    NULL,
    PRIMARY KEY (`idexamen`),
    UNIQUE INDEX `idexamen_UNIQUE` (`idexamen` ASC) VISIBLE
);

CREATE TABLE `provocare1`.`note_student`
(
    `idexamen_student_note` INT           NOT NULL AUTO_INCREMENT,
    `idstudent`             INT           NULL,
    `idexamen`              INT           NULL,
    `idprofesor`            INT           NULL,
    `nota_student`          DECIMAL(4, 2) NULL,
    PRIMARY KEY (`idexamen_student_note`),
    UNIQUE INDEX `idexamen_student_note_UNIQUE` (`idexamen_student_note` ASC) VISIBLE,
    INDEX `idstudent_idx` (`idstudent` ASC) VISIBLE,
    INDEX `idprofesor_idx` (`idprofesor` ASC) VISIBLE,
    INDEX `idexamen_idx` (`idexamen` ASC) VISIBLE,
    CONSTRAINT `idstudent`
        FOREIGN KEY (`idstudent`)
            REFERENCES `provocare1`.`student` (`idstudent`)
            ON DELETE NO ACTION
            ON UPDATE CASCADE,
    CONSTRAINT `idprofesor`
        FOREIGN KEY (`idprofesor`)
            REFERENCES `provocare1`.`profesor` (`idprofesor`)
            ON DELETE NO ACTION
            ON UPDATE CASCADE,
    CONSTRAINT `idexamen`
        FOREIGN KEY (`idexamen`)
            REFERENCES `provocare1`.`examen` (`idexamen`)
            ON DELETE NO ACTION
            ON UPDATE CASCADE
);

