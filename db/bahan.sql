-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 23, 2018 at 01:09 PM
-- Server version: 10.1.24-MariaDB
-- PHP Version: 7.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `resep-app`
--

-- --------------------------------------------------------

--
-- Table structure for table `bahan`
--

CREATE TABLE `bahan` (
  `id_bahan` int(11) NOT NULL,
  `nama_bahan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bahan`
--

INSERT INTO `bahan` (`id_bahan`, `nama_bahan`) VALUES
(1, 'udang galah'),
(2, 'margarin'),
(3, 'daun bawang'),
(4, 'saus tiram'),
(5, 'kecap inggris'),
(6, 'kecap manis'),
(7, 'saus tomat'),
(8, 'merica'),
(9, 'gula'),
(10, 'garam'),
(11, 'air'),
(12, 'bawang bombai'),
(13, 'daging sapi'),
(14, 'maizena'),
(15, 'bawang putih'),
(16, 'kecap asin'),
(17, 'minyak wijen'),
(18, 'lada hitam'),
(19, 'paprika'),
(20, 'daging ayam'),
(21, 'minyak goreng'),
(22, 'ketumbar sangrai'),
(23, 'jahe'),
(24, 'kunyit'),
(25, 'kemiri goreng'),
(26, 'garam'),
(27, 'serai'),
(28, 'lengkuas'),
(29, 'telur ayam'),
(30, 'terigu'),
(31, 'tapioka'),
(32, 'baput'),
(33, 'saus sambah'),
(34, 'cabe merah'),
(35, 'kemiri'),
(36, 'bawang merah'),
(37, 'daun salam'),
(38, 'daun jeruk'),
(39, 'penyedap'),
(40, 'bawang putih bubuk');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bahan`
--
ALTER TABLE `bahan`
  ADD PRIMARY KEY (`id_bahan`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bahan`
--
ALTER TABLE `bahan`
  MODIFY `id_bahan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
