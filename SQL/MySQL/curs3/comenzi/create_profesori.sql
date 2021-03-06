CREATE TABLE  IF NOT EXISTS `profesor` (
  `cod_profesor` int(11) NOT NULL,
  `nume` varchar(45) DEFAULT NULL,
  `prenume` varchar(45) DEFAULT NULL,
  `adresa` varchar(45) DEFAULT NULL,
  `data_nastere` datetime DEFAULT NULL,
  `grad_didactic` int DEFAULT NULL,
  PRIMARY KEY (`cod_profesor`), -- This is a comment
  KEY `nume_prenume` (`nume`,`prenume`) COMMENT 'Nume prenume Unique'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
