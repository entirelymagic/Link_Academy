CREATE TABLE IF NOT EXISTS `magazin`.`firme`(
    `idfirma` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
    `firma` VARCHAR(200) NOT NULL ,
    `adresafirma` INT(250) NOT NULL ,
    PRIMARY KEY (`idfirma`)
    ) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_general_ci;