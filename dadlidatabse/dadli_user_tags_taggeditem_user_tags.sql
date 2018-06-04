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
-- Table structure for table `user_tags_taggeditem_user_tags`
--

DROP TABLE IF EXISTS `user_tags_taggeditem_user_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_tags_taggeditem_user_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `taggeditem_id` int(11) NOT NULL,
  `usertag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_tags_taggeditem_use_taggeditem_id_usertag_id_ba10e8ac_uniq` (`taggeditem_id`,`usertag_id`),
  KEY `user_tags_taggeditem_usertag_id_6c2e4069_fk_user_tags` (`usertag_id`),
  CONSTRAINT `user_tags_taggeditem_taggeditem_id_06f1c6de_fk_user_tags` FOREIGN KEY (`taggeditem_id`) REFERENCES `user_tags_taggeditem` (`id`),
  CONSTRAINT `user_tags_taggeditem_usertag_id_6c2e4069_fk_user_tags` FOREIGN KEY (`usertag_id`) REFERENCES `user_tags_usertag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_tags_taggeditem_user_tags`
--

LOCK TABLES `user_tags_taggeditem_user_tags` WRITE;
/*!40000 ALTER TABLE `user_tags_taggeditem_user_tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_tags_taggeditem_user_tags` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-11 17:39:29
