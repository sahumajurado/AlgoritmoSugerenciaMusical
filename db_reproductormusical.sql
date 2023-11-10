-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: db_reproductormusical
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `album`
--

DROP TABLE IF EXISTS `album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album` (
  `id_album` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `fecha_creacion` date NOT NULL,
  `id_artista` int NOT NULL,
  PRIMARY KEY (`id_album`),
  KEY `fk_album_artista` (`id_artista`),
  CONSTRAINT `fk_album_artista` FOREIGN KEY (`id_artista`) REFERENCES `artista` (`id_artista`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album`
--

LOCK TABLES `album` WRITE;
/*!40000 ALTER TABLE `album` DISABLE KEYS */;
INSERT INTO `album` VALUES (1,'Made in A.M.','2015-11-23',1),(2,'Éxitos','2012-04-25',2);
/*!40000 ALTER TABLE `album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artista`
--

DROP TABLE IF EXISTS `artista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artista` (
  `id_artista` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `nacionalidad` varchar(45) NOT NULL,
  `id_generomusical` int NOT NULL,
  PRIMARY KEY (`id_artista`),
  KEY `fk_artista_genero` (`id_generomusical`),
  CONSTRAINT `fk_artista_genero` FOREIGN KEY (`id_generomusical`) REFERENCES `generomusical` (`id_generomusical`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artista`
--

LOCK TABLES `artista` WRITE;
/*!40000 ALTER TABLE `artista` DISABLE KEYS */;
INSERT INTO `artista` VALUES (1,'One Direction','Britanico',1),(2,'Makano','Panameño',2);
/*!40000 ALTER TABLE `artista` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cancion`
--

DROP TABLE IF EXISTS `cancion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cancion` (
  `id_cancion` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `archivo_letra` varchar(100) NOT NULL,
  `archivo_musica` varchar(100) NOT NULL,
  `id_artista` int NOT NULL,
  `id_album` int NOT NULL,
  `id_generomusical` int NOT NULL,
  PRIMARY KEY (`id_cancion`),
  KEY `fk_cancion_artista` (`id_artista`),
  KEY `fk_cancion_album` (`id_album`),
  KEY `fk_cancion_genero` (`id_generomusical`),
  CONSTRAINT `fk_cancion_album` FOREIGN KEY (`id_album`) REFERENCES `album` (`id_album`),
  CONSTRAINT `fk_cancion_artista` FOREIGN KEY (`id_artista`) REFERENCES `artista` (`id_artista`),
  CONSTRAINT `fk_cancion_genero` FOREIGN KEY (`id_generomusical`) REFERENCES `generomusical` (`id_generomusical`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cancion`
--

LOCK TABLES `cancion` WRITE;
/*!40000 ALTER TABLE `cancion` DISABLE KEYS */;
INSERT INTO `cancion` VALUES (1,'Perfect','C:\\Users\\Usuario\\Desktop\\TA_MICROPROCESADORES\\letra_cancion\\perfect.txt','C:\\Users\\Usuario\\Desktop\\TA_MICROPROCESADORES\\musica\\perfect.mp3',1,1,1),(2,'Dejame Entrar','\"C:\\Users\\Usuario\\Desktop\\TA_MICROPROCESADORES\\letra_cancion\\dejameentrar.txt\"','C:\\Users\\Usuario\\Desktop\\TA_MICROPROCESADORES\\musica\\dejameentrar.mp3',2,2,2);
/*!40000 ALTER TABLE `cancion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cancion_escuchada`
--

DROP TABLE IF EXISTS `cancion_escuchada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cancion_escuchada` (
  `id_cancion_escuchada` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `id_cancion` int NOT NULL,
  `id_usuario` int NOT NULL,
  PRIMARY KEY (`id_cancion_escuchada`),
  KEY `fk_cancion_escuchada_cancion` (`id_cancion`),
  KEY `fk_cancion_escuchada_usuario` (`id_usuario`),
  CONSTRAINT `fk_cancion_escuchada_cancion` FOREIGN KEY (`id_cancion`) REFERENCES `cancion` (`id_cancion`),
  CONSTRAINT `fk_cancion_escuchada_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cancion_escuchada`
--

LOCK TABLES `cancion_escuchada` WRITE;
/*!40000 ALTER TABLE `cancion_escuchada` DISABLE KEYS */;
/*!40000 ALTER TABLE `cancion_escuchada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generomusical`
--

DROP TABLE IF EXISTS `generomusical`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `generomusical` (
  `id_generomusical` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`id_generomusical`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generomusical`
--

LOCK TABLES `generomusical` WRITE;
/*!40000 ALTER TABLE `generomusical` DISABLE KEYS */;
INSERT INTO `generomusical` VALUES (1,'pop'),(2,'reggaeton');
/*!40000 ALTER TABLE `generomusical` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lista_favoritos`
--

DROP TABLE IF EXISTS `lista_favoritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lista_favoritos` (
  `id_lista_favoritos` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_cancion` int NOT NULL,
  PRIMARY KEY (`id_lista_favoritos`),
  KEY `fk_lista_favoritos_usuario` (`id_usuario`),
  KEY `fk_lista_favoritos_cancion` (`id_cancion`),
  CONSTRAINT `fk_lista_favoritos_cancion` FOREIGN KEY (`id_cancion`) REFERENCES `cancion` (`id_cancion`),
  CONSTRAINT `fk_lista_favoritos_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lista_favoritos`
--

LOCK TABLES `lista_favoritos` WRITE;
/*!40000 ALTER TABLE `lista_favoritos` DISABLE KEYS */;
INSERT INTO `lista_favoritos` VALUES (1,1,1);
/*!40000 ALTER TABLE `lista_favoritos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lista_recomendacion`
--

DROP TABLE IF EXISTS `lista_recomendacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lista_recomendacion` (
  `id_lista_recomendacion` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `id_cancion_escuchada` int NOT NULL,
  `id_usuario` int NOT NULL,
  `id_lista_favoritos` int NOT NULL,
  PRIMARY KEY (`id_lista_recomendacion`),
  KEY `fk_lista_recomendacion_cancion_escuchada` (`id_cancion_escuchada`),
  KEY `fk_lista_recomendacion_usuario` (`id_usuario`),
  KEY `fk_lista_recomendacion_lista_favoritos` (`id_lista_favoritos`),
  CONSTRAINT `fk_lista_recomendacion_cancion_escuchada` FOREIGN KEY (`id_cancion_escuchada`) REFERENCES `cancion_escuchada` (`id_cancion_escuchada`),
  CONSTRAINT `fk_lista_recomendacion_lista_favoritos` FOREIGN KEY (`id_lista_favoritos`) REFERENCES `lista_favoritos` (`id_lista_favoritos`),
  CONSTRAINT `fk_lista_recomendacion_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lista_recomendacion`
--

LOCK TABLES `lista_recomendacion` WRITE;
/*!40000 ALTER TABLE `lista_recomendacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `lista_recomendacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `sexo` varchar(45) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `nacionalidad` varchar(45) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `nombre_user` varchar(45) NOT NULL,
  `contraseña` varchar(45) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Gerson Daniel','Sahuma Jurado','Masculino','2002-08-27','Peruano','danielsahumajurado607@gmail.com','danielsjxd','123'),(2,'Jesus','Paye Juarez','Masculino','2001-05-07','Peruano','jesuspaye@gmail.com','jpaye','456'),(3,'Marcos','Lopez Diaz','Masculino','2000-06-04','Brasilero','mlopez@gmail.com','mlopezd','789'),(4,'Jose','Luna Pizarro','Masculino','2001-02-25','Colombiano','josesito@gmail.com','josepiza','573'),(5,'Martha','Ortiz Campos','Femenino','2002-06-30','Estadounidense','marthitaort@gmail.com','marthaortiz30','ortiz3006');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-10  7:20:09
