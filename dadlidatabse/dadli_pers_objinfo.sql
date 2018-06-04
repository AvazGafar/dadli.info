CREATE DATABASE  IF NOT EXISTS `dadli` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `dadli`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win32 (AMD64)
--
-- Host: localhost    Database: dadli
-- ------------------------------------------------------
-- Server version	5.7.20-log

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
-- Table structure for table `pers_objinfo`
--

DROP TABLE IF EXISTS `pers_objinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pers_objinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `objt` varchar(250) NOT NULL,
  `adres` varchar(250) NOT NULL,
  `erazi` varchar(250) NOT NULL,
  `metro` varchar(250) NOT NULL,
  `city_reg` varchar(250) NOT NULL,
  `city` varchar(250) NOT NULL,
  `country` varchar(250) NOT NULL,
  `zip` varchar(10) NOT NULL,
  `fammeal` varchar(100) NOT NULL,
  `menu` varchar(5000) NOT NULL,
  `delivery` tinyint(1) NOT NULL,
  `tel1` varchar(14) NOT NULL,
  `tel2` varchar(14) NOT NULL,
  `tel3` varchar(14) NOT NULL,
  `mob1` varchar(14) NOT NULL,
  `mob2` varchar(14) NOT NULL,
  `mob3` varchar(14) NOT NULL,
  `mob4` varchar(14) NOT NULL,
  `mob5` varchar(14) NOT NULL,
  `info` longtext NOT NULL,
  `pic0` varchar(1000) NOT NULL,
  `pic1` varchar(1000) NOT NULL,
  `pic2` varchar(1000) NOT NULL,
  `pic3` varchar(1000) NOT NULL,
  `pic4` varchar(1000) NOT NULL,
  `pic5` varchar(1000) NOT NULL,
  `pic6` varchar(1000) NOT NULL,
  `pic7` varchar(1000) NOT NULL,
  `pic8` varchar(1000) NOT NULL,
  `pic9` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pers_objinfo`
--

LOCK TABLES `pers_objinfo` WRITE;
/*!40000 ALTER TABLE `pers_objinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `pers_objinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-11 17:39:24
