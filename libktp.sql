-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 09, 2018 at 01:13 PM
-- Server version: 10.1.35-MariaDB
-- PHP Version: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `libktp`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(200) NOT NULL,
  `tgl_create` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`, `tgl_create`) VALUES
(1, 'admin', 'pbkdf2:sha256:50000$0sCHe8UK$498b09ee19d9b4ab8267d3f6f7203c928f6b8aee09fc98f391c4e524bcc9d762', '2018-12-08 07:29:45');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `nama` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `no_telp` varchar(20) NOT NULL,
  `isi` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ktp`
--

CREATE TABLE `ktp` (
  `id` int(11) NOT NULL,
  `nik` varchar(20) NOT NULL,
  `nama` varchar(150) NOT NULL,
  `tempat_lahir` varchar(50) NOT NULL,
  `tgl_lahir` date NOT NULL,
  `jk` enum('Perempuan','Laki-laki') NOT NULL,
  `gol_darah` varchar(15) NOT NULL,
  `agama` enum('Kristen Protestan','Islam','Hindu','Buddha','Khatolik','Konghucu') NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `rt_rw` varchar(50) NOT NULL,
  `kel_desa` varchar(50) NOT NULL,
  `kecamatan` varchar(50) NOT NULL,
  `status_perkawinan` varchar(50) NOT NULL,
  `pekerjaan` varchar(50) NOT NULL,
  `kewarganegaraan` varchar(15) NOT NULL,
  `berlaku_hingga` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ktp`
--

INSERT INTO `ktp` (`id`, `nik`, `nama`, `tempat_lahir`, `tgl_lahir`, `jk`, `gol_darah`, `agama`, `alamat`, `rt_rw`, `kel_desa`, `kecamatan`, `status_perkawinan`, `pekerjaan`, `kewarganegaraan`, `berlaku_hingga`) VALUES
(3, '89039303030', 'Jovan Rauan', 'Suluun Tareran', '1987-05-04', 'Laki-laki', '', 'Kristen Protestan', '', '', '', '', '', '', '', ''),
(4, '393023030330', 'Willy Widianto', 'Manado', '2000-01-09', 'Laki-laki', '', 'Kristen Protestan', '', '', '', '', '', '', '', ''),
(5, '043030330330', 'Altarichie', 'Manado', '2000-11-27', 'Laki-laki', '', 'Kristen Protestan', 'Lingkungan VII', '008/009', 'Bengkol', 'Mapanget', 'Belum Kawin', 'Mahasiswa', 'WNI', 'Seumur Hidup');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ktp`
--
ALTER TABLE `ktp`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `ktp`
--
ALTER TABLE `ktp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
