# Create database with default characters set utf8-ci
create_database = "CREATE SCHEMA `bank` DEFAULT CHARACTER SET utf8 ;"

# InnoDB - for transactions - MYISAM for transactions.
create_table = """
    CREATE TABLE `bank`.`user` (
      `iduser` INT UNSIGNED NOT NULL AUTO_INCREMENT,
      `nume` VARCHAR(70) NOT NULL,
      `prenume` VARCHAR(70) NOT NULL,
      `email` VARCHAR(255) GENERATED ALWAYS AS (CONCAT(nume,'.', prenume, '@awesometest.com')),
      `phone` VARCHAR(10) NOT NULL,
      PRIMARY KEY (`iduser`));
"""