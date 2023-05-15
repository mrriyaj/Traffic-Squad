-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 15, 2023 at 09:40 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `traffic_squad`
--

-- --------------------------------------------------------

--
-- Table structure for table `captured_cars`
--

CREATE TABLE `captured_cars` (
  `Id` int(11) NOT NULL,
  `carID` int(11) DEFAULT NULL,
  `speed` float DEFAULT NULL,
  `violation_status` tinyint(1) DEFAULT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `captured_cars`
--

INSERT INTO `captured_cars` (`Id`, `carID`, `speed`, `violation_status`, `image_path`, `timestamp`) VALUES
(900, 4, 138.972, 1, 'captured_cars/car4_speed138.97.jpg', '2023-05-15 19:16:23'),
(901, 5, 141.052, 1, 'captured_cars/car5_speed141.05.jpg', '2023-05-15 19:16:26'),
(902, 10, 66.4496, 1, 'captured_cars/car10_speed66.45.jpg', '2023-05-15 19:16:36'),
(903, 9, 50.2201, 0, 'captured_cars/car9_speed50.22.jpg', '2023-05-15 19:16:37'),
(904, 11, 105.233, 1, 'captured_cars/car11_speed105.23.jpg', '2023-05-15 19:16:39'),
(905, 13, 53.4178, 0, 'captured_cars/car13_speed53.42.jpg', '2023-05-15 19:16:54'),
(906, 15, 32.8852, 0, 'captured_cars/car15_speed32.89.jpg', '2023-05-15 19:17:01'),
(907, 16, 40.9191, 0, 'captured_cars/car16_speed40.92.jpg', '2023-05-15 19:17:05'),
(908, 18, 63.236, 1, 'captured_cars/car18_speed63.24.jpg', '2023-05-15 19:17:09'),
(909, 20, 23.9228, 0, 'captured_cars/car20_speed23.92.jpg', '2023-05-15 19:17:17'),
(910, 21, 45.9912, 0, 'captured_cars/car21_speed45.99.jpg', '2023-05-15 19:17:23'),
(911, 22, 29.5685, 0, 'captured_cars/car22_speed29.57.jpg', '2023-05-15 19:17:26'),
(912, 25, 33.5553, 0, 'captured_cars/car25_speed33.56.jpg', '2023-05-15 19:17:34'),
(913, 26, 30.2894, 0, 'captured_cars/car26_speed30.29.jpg', '2023-05-15 19:17:35'),
(914, 28, 17.8418, 0, 'captured_cars/car28_speed17.84.jpg', '2023-05-15 19:17:40'),
(915, 30, 22.8181, 0, 'captured_cars/car30_speed22.82.jpg', '2023-05-15 19:17:45'),
(916, 31, 18.305, 0, 'captured_cars/car31_speed18.30.jpg', '2023-05-15 19:18:03'),
(917, 32, 25.1603, 0, 'captured_cars/car32_speed25.16.jpg', '2023-05-15 19:18:09'),
(918, 33, 13.1122, 0, 'captured_cars/car33_speed13.11.jpg', '2023-05-15 19:18:11'),
(919, 34, 0, 0, 'captured_cars/car34_speed0.00.jpg', '2023-05-15 19:18:13'),
(920, 36, 0, 0, 'captured_cars/car36_speed0.00.jpg', '2023-05-15 19:18:16'),
(921, 37, 22.2585, 0, 'captured_cars/car37_speed22.26.jpg', '2023-05-15 19:18:30'),
(922, 39, 14.8456, 0, 'captured_cars/car39_speed14.85.jpg', '2023-05-15 19:18:39'),
(923, 41, 12.9725, 0, 'captured_cars/car41_speed12.97.jpg', '2023-05-15 19:18:49'),
(924, 42, 24.311, 0, 'captured_cars/car42_speed24.31.jpg', '2023-05-15 19:19:01'),
(925, 45, 20.0688, 0, 'captured_cars/car45_speed20.07.jpg', '2023-05-15 19:19:18'),
(926, 46, 12.0518, 0, 'captured_cars/car46_speed12.05.jpg', '2023-05-15 19:19:20'),
(927, 48, 15.7578, 0, 'captured_cars/car48_speed15.76.jpg', '2023-05-15 19:19:31'),
(928, 50, 11.8284, 0, 'captured_cars/car50_speed11.83.jpg', '2023-05-15 19:19:38'),
(929, 55, 12.5954, 0, 'captured_cars/car55_speed12.60.jpg', '2023-05-15 19:19:58'),
(930, 60, 22.4537, 0, 'captured_cars/car60_speed22.45.jpg', '2023-05-15 19:20:17'),
(931, 61, 18.4058, 0, 'captured_cars/car61_speed18.41.jpg', '2023-05-15 19:20:26');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES
(1, 'Riyaj Kaffar', 'riyajkafar@gmail.com', '$2b$12$xIqD4N1CP1yYUyFFp3tAmeg.ik.PqST64DyWHAV5hJnt0..mew9uy'),
(4, 'riyaj', 'itstarterorg@gmail.com', '$2b$12$jo4qFgM5o38AwqKSX1f3vOAj.1IcO.Ot7jYZVvTn4gh1c3PbT7NFy'),
(5, 'IT Starter', 'jerowit969@crtsec.com', '$2b$12$BMCCazBZ0FZgrMzBD2zbauxCUH4ukN3UB6Em2xp8naiJxOVI/imXG'),
(6, 'Joji', 'admin@example.com', '$2b$12$9kDbLdsdFJlh6vS0kKBd1O4e/1tt9eN1fo0O/TemWIFm.qGU03vmm'),
(7, 'Riyaj Kaffar', 'employee@example.com', '$2b$12$VeehtPXfyjyRsi4VOpaWzeYfqePH4ui6D/N3qHF.d60OaUBnqHk3G');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `captured_cars`
--
ALTER TABLE `captured_cars`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `captured_cars`
--
ALTER TABLE `captured_cars`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=932;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
