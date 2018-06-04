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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add catobj',1,'add_catobj'),(2,'Can change catobj',1,'change_catobj'),(3,'Can delete catobj',1,'delete_catobj'),(4,'Can add cats',2,'add_cats'),(5,'Can change cats',2,'change_cats'),(6,'Can delete cats',2,'delete_cats'),(7,'Can add objinfo',3,'add_objinfo'),(8,'Can change objinfo',3,'change_objinfo'),(9,'Can delete objinfo',3,'delete_objinfo'),(10,'Can add tagobj',4,'add_tagobj'),(11,'Can change tagobj',4,'change_tagobj'),(12,'Can delete tagobj',4,'delete_tagobj'),(13,'Can add tags',5,'add_tags'),(14,'Can change tags',5,'change_tags'),(15,'Can delete tags',5,'delete_tags'),(16,'Can add ustags',6,'add_ustags'),(17,'Can change ustags',6,'change_ustags'),(18,'Can delete ustags',6,'delete_ustags'),(19,'Can add association',7,'add_association'),(20,'Can change association',7,'change_association'),(21,'Can delete association',7,'delete_association'),(22,'Can add code',8,'add_code'),(23,'Can change code',8,'change_code'),(24,'Can delete code',8,'delete_code'),(25,'Can add nonce',9,'add_nonce'),(26,'Can change nonce',9,'change_nonce'),(27,'Can delete nonce',9,'delete_nonce'),(28,'Can add user social auth',10,'add_usersocialauth'),(29,'Can change user social auth',10,'change_usersocialauth'),(30,'Can delete user social auth',10,'delete_usersocialauth'),(31,'Can add partial',11,'add_partial'),(32,'Can change partial',11,'change_partial'),(33,'Can delete partial',11,'delete_partial'),(34,'Can add tagged item',12,'add_taggeditem'),(35,'Can change tagged item',12,'change_taggeditem'),(36,'Can delete tagged item',12,'delete_taggeditem'),(37,'Can add user tag',13,'add_usertag'),(38,'Can change user tag',13,'change_usertag'),(39,'Can delete user tag',13,'delete_usertag'),(40,'Can add user tag group',14,'add_usertaggroup'),(41,'Can change user tag group',14,'change_usertaggroup'),(42,'Can delete user tag group',14,'delete_usertaggroup'),(43,'Can add log entry',15,'add_logentry'),(44,'Can change log entry',15,'change_logentry'),(45,'Can delete log entry',15,'delete_logentry'),(46,'Can add permission',16,'add_permission'),(47,'Can change permission',16,'change_permission'),(48,'Can delete permission',16,'delete_permission'),(49,'Can add group',17,'add_group'),(50,'Can change group',17,'change_group'),(51,'Can delete group',17,'delete_group'),(52,'Can add user',18,'add_user'),(53,'Can change user',18,'change_user'),(54,'Can delete user',18,'delete_user'),(55,'Can add content type',19,'add_contenttype'),(56,'Can change content type',19,'change_contenttype'),(57,'Can delete content type',19,'delete_contenttype'),(58,'Can add session',20,'add_session'),(59,'Can change session',20,'change_session'),(60,'Can delete session',20,'delete_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-11 17:39:23
