-- MySQL dump 10.13  Distrib 5.7.28, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: pooii
-- ------------------------------------------------------
-- Server version	5.7.28-0ubuntu0.18.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Histórico`
--

DROP TABLE IF EXISTS `Histórico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Histórico` (
  `idHistórico` int(11) NOT NULL AUTO_INCREMENT,
  `problema` varchar(45) NOT NULL,
  `dataHora` varchar(45) NOT NULL,
  `resposta` varchar(45) DEFAULT NULL,
  `fk_id_time` int(11) NOT NULL,
  PRIMARY KEY (`idHistórico`,`fk_id_time`),
  KEY `fk_id_time_idx` (`fk_id_time`),
  CONSTRAINT `fk_id_time` FOREIGN KEY (`fk_id_time`) REFERENCES `times_coders` (`id_time`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Histórico`
--

LOCK TABLES `Histórico` WRITE;
/*!40000 ALTER TABLE `Histórico` DISABLE KEYS */;
INSERT INTO `Histórico` VALUES (1,'hanoio','hoje','eerro',3),(2,'caixeiro viajante','ontem','ACEPT',3);
/*!40000 ALTER TABLE `Histórico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercício`
--

DROP TABLE IF EXISTS `exercício`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exercício` (
  `idexercicio` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `arquivo_entrada` varchar(300) NOT NULL,
  `arquivo_saída` varchar(300) NOT NULL,
  `descrição` varchar(45) NOT NULL,
  `tempo` varchar(45) NOT NULL,
  `fk_id_professor` int(11) DEFAULT NULL,
  PRIMARY KEY (`idexercicio`),
  KEY `fk_id_professor_idx` (`fk_id_professor`),
  CONSTRAINT `fk_id_professor` FOREIGN KEY (`fk_id_professor`) REFERENCES `professor` (`idprofessor`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercício`
--

LOCK TABLES `exercício` WRITE;
/*!40000 ALTER TABLE `exercício` DISABLE KEYS */;
INSERT INTO `exercício` VALUES (19,'SamuelTEste','/home/samuel/TESTE_TEMPO/entradaPROF.txt','/home/samuel/TESTE_TEMPO/saidaPROF.txt','\\sdfadf','500',23);
/*!40000 ALTER TABLE `exercício` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `professor`
--

DROP TABLE IF EXISTS `professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `professor` (
  `idprofessor` int(11) NOT NULL AUTO_INCREMENT,
  `siape` int(11) DEFAULT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `senha` varchar(45) DEFAULT NULL,
  `exercicios` int(11) NOT NULL,
  PRIMARY KEY (`idprofessor`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professor`
--

LOCK TABLES `professor` WRITE;
/*!40000 ALTER TABLE `professor` DISABLE KEYS */;
INSERT INTO `professor` VALUES (23,2015,'samuel de oliveira ribeiro','kkk','kkk',0);
/*!40000 ALTER TABLE `professor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `times_coders`
--

DROP TABLE IF EXISTS `times_coders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `times_coders` (
  `id_time` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) NOT NULL,
  `senha` varchar(45) DEFAULT NULL,
  `nome_time` varchar(45) NOT NULL,
  `questoes_corretas` int(11) NOT NULL,
  `componentes_grupo` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id_time`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `times_coders`
--

LOCK TABLES `times_coders` WRITE;
/*!40000 ALTER TABLE `times_coders` DISABLE KEYS */;
INSERT INTO `times_coders` VALUES (1,'23','0','123',0,'123,123,12321,321'),(3,'23','0','sam',0,'sam,sam,sam,sam'),(5,'23',NULL,'',0,',,,');
/*!40000 ALTER TABLE `times_coders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-03  3:33:06
