-- MySQL dump 10.16  Distrib 10.1.29-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: RFID
-- ------------------------------------------------------
-- Server version	10.1.29-MariaDB-6

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Digital_Data`
--

DROP TABLE IF EXISTS `Digital_Data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Digital_Data` (
  `RFID_Key` char(100) NOT NULL,
  `RFID_Card` char(100) NOT NULL,
  `Laptop_Make` char(10) NOT NULL,
  `Reg_Number` char(16) NOT NULL,
<<<<<<< HEAD
  UNIQUE KEY `UC_Digital` (`RFID_Key`,`RFID_Card`),
  KEY `Reg_Number` (`Reg_Number`),
  CONSTRAINT `Digital_Data_ibfk_1` FOREIGN KEY (`Reg_Number`) REFERENCES `Personal_Data` (`Reg_Number`)
=======
  PRIMARY KEY (`RFID_Key`,`RFID_Card`)
>>>>>>> e0837f7488066df51a2e1ec53ffb678337ee4f3d
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Digital_Data`
--

LOCK TABLES `Digital_Data` WRITE;
/*!40000 ALTER TABLE `Digital_Data` DISABLE KEYS */;
/*!40000 ALTER TABLE `Digital_Data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Personal_Data`
--

DROP TABLE IF EXISTS `Personal_Data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Personal_Data` (
  `Name` char(20) NOT NULL,
  `Phone_Number` int(10) NOT NULL,
  `Reg_Number` char(16) NOT NULL,
<<<<<<< HEAD
  PRIMARY KEY (`Reg_Number`),
  UNIQUE KEY `Phone_Number` (`Phone_Number`)
=======
  PRIMARY KEY (`Phone_Number`,`Reg_Number`)
>>>>>>> e0837f7488066df51a2e1ec53ffb678337ee4f3d
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Personal_Data`
--

LOCK TABLES `Personal_Data` WRITE;
/*!40000 ALTER TABLE `Personal_Data` DISABLE KEYS */;
/*!40000 ALTER TABLE `Personal_Data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

<<<<<<< HEAD
-- Dump completed on 2020-03-28 12:28:53
=======
-- Dump completed on 2020-03-23 20:39:45
>>>>>>> e0837f7488066df51a2e1ec53ffb678337ee4f3d
