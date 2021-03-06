CREATE TABLE `studenti` (
  `cod_student` int NOT NULL,
  `nume` varchar(45) DEFAULT NULL,
  `prenume` varchar(45) DEFAULT NULL,
  `data_nastere` date DEFAULT NULL,
  PRIMARY KEY (`cod_student`),
  KEY `num_prenume` (`nume`,`prenume`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
