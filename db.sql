-- Create captured_cars table
CREATE TABLE `captured_cars` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `carID` int(11) DEFAULT NULL,
  `speed` float DEFAULT NULL,
  `violation_status` tinyint(1) DEFAULT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Create users table
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Insert data into users table
INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES
(1, 'Riyaj Kaffar', 'riyajkafar@gmail.com', '$2b$12$xIqD4N1CP1yYUyFFp3tAmeg.ik.PqST64DyWHAV5hJnt0..mew9uy');

-- Set auto-increment values for captured_cars table
ALTER TABLE `captured_cars`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=836;

-- Set auto-increment values for users table
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
