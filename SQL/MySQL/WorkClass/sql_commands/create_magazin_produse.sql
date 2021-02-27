CREATE TABLE IF NOT EXISTS `magazin`.`produse`(
    `idprodus` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
    `nume` VARCHAR(200) NOT NULL ,
    `cantitate` INT NOT NULL ,
    `model` VARCHAR(250) NOT NULL ,
    `stoc` SMALLINT NOT NULL ,
    `pret` DECIMAL(6,2) NOT NULL ,
    `idcategorie` INT NOT NULL ,
    `descriere` TEXT NOT NULL ,
    `data_add` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,
    PRIMARY KEY (`idprodus`)
    ) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_general_ci;
