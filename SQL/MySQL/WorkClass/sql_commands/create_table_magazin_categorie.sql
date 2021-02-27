CREATE TABLE IF NOT EXISTS 'magazin'.'categorie'(
    'idcategorie' INT UNSIGNED NOT NULL AUTO_INCREMENT ,
    'nume' VARCHAR(200) NOT NULL ,
    PRIMARY KEY ('idcategorie')
    ) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_general_ci;