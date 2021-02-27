CREATE TABLE `magazin`.`produse`
( `idprodus` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
`numep` VARCHAR(200) NOT NULL ,
`cantitate` INT NOT NULL ,
`idfirma` INT UNSIGNED NOT NULL ,
`firma` VARCHAR(200) NOT NULL ,
`adresafirma` INT(250) NOT NULL ,
`modelp` VARCHAR(250) NOT NULL ,
`stocp` SMALLINT NOT NULL ,
`pret` DECIMAL(6,2) NOT NULL ,
`categoriep` VARCHAR(200) NOT NULL ,
`descrierep` TEXT NOT NULL ,
`data_addp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,
PRIMARY KEY (`idprodus`)
) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_general_ci;


