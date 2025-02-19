-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 29, 2024 at 10:03 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_rec_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance_log`
--

CREATE TABLE `attendance_log` (
  `sl_no` int(254) NOT NULL,
  `usn` varchar(10) NOT NULL,
  `log_date` varchar(15) NOT NULL,
  `time` varchar(10) NOT NULL,
  `camera_id` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance_log`
--

INSERT INTO `attendance_log` (`sl_no`, `usn`, `log_date`, `time`, `camera_id`) VALUES
(54, '4HG20CS029', '2024-05-11', '14:14:35', '0'),
(55, '4HG20CS029', '2024-05-11', '14:14:35', '0'),
(56, '4HG20CS029', '2024-05-11', '14:14:35', '0'),
(57, '4HG20CS029', '2024-05-11', '14:14:35', '0'),
(58, '4HG20CS029', '2024-05-11', '14:14:35', '0'),
(59, '4HG20CS029', '2024-05-11', '14:15:16', '1'),
(60, '4HG20CS029', '2024-05-11', '14:15:16', '1'),
(61, '4HG20CS029', '2024-05-11', '15:43:20', '0'),
(62, '4HG20CS029', '2024-05-11', '15:43:20', '0'),
(63, '4HG20CS029', '2024-05-11', '15:43:23', '1'),
(64, '4HG20CS029', '2024-05-11', '15:43:23', '1'),
(65, '4HG20CS029', '2024-05-11', '15:44:44', '1'),
(66, '4HG20CS029', '2024-05-11', '17:07:04', '0'),
(67, '4HG20CS029', '2024-05-11', '17:07:04', '0'),
(68, '4HG20CS029', '2024-05-11', '17:07:04', '0'),
(69, '4HG20CS029', '2024-05-11', '17:40:29', '0'),
(70, '4HG20CS029', '2024-05-11', '17:40:29', '0'),
(71, '4HG20CS029', '2024-05-11', '22:47:40', '0'),
(72, '4HG20CS029', '2024-05-11', '22:51:24', '0'),
(73, '4HG20CS029', '2024-05-11', '22:51:24', '0'),
(74, '4HG20CS029', '2024-05-11', '22:51:24', '0'),
(75, '4HG20CS029', '2024-05-11', '22:56:27', '0'),
(76, '4HG20CS029', '2024-05-11', '22:56:27', '0'),
(77, '4HG20CS029', '2024-05-12', '07:48:54', '0'),
(78, '4HG20CS029', '2024-05-12', '07:48:54', '0'),
(79, '4HG20CS029', '2024-05-12', '07:48:54', '0'),
(80, '4HG20CS029', '2024-05-12', '11:58:22', '0'),
(81, '4HG20CS021', '2024-05-12', '11:58:22', '0'),
(82, '4HG20CS029', '2024-05-12', '11:58:22', '0'),
(83, '4HG20CS029', '2024-05-12', '11:58:22', '0'),
(84, '4HG20CS029', '2024-05-12', '11:58:22', '0'),
(85, '4HG20CS021', '2024-05-12', '11:58:22', '0'),
(86, '4HG20CS021', '2024-05-12', '11:58:52', '0'),
(87, '4HG20CS021', '2024-05-12', '11:58:52', '0'),
(88, '4HG20CS021', '2024-05-12', '13:31:49', '0'),
(89, '4HG20CS029', '2024-05-12', '13:31:49', '0'),
(90, '4HG20CS029', '2024-05-12', '13:31:49', '0'),
(91, '4HG20CS029', '2024-05-12', '13:57:31', '0'),
(92, '4HG20CS029', '2024-05-12', '14:18:21', '0'),
(93, '4HG20CS029', '2024-05-12', '14:18:21', '0'),
(94, '4HG20CS029', '2024-05-12', '14:18:21', '0'),
(95, '4HG20CS029', '2024-05-12', '14:25:11', '0'),
(96, '4HG20CS029', '2024-05-12', '14:34:44', '0'),
(97, '4HG20CS029', '2024-05-12', '14:34:44', '0'),
(98, '4HG20CS029', '2024-05-12', '15:07:41', '1'),
(99, '4HG20CS029', '2024-05-12', '15:07:41', '1'),
(100, '4HG20CS029', '2024-05-12', '15:07:44', '0'),
(101, '4HG20CS029', '2024-05-12', '15:07:44', '0'),
(102, '4HG20CS029', '2024-05-12', '15:07:44', '0'),
(103, '4HG20CS029', '2024-05-12', '15:07:44', '0'),
(104, '4HG20CS029', '2024-05-12', '18:33:41', '0'),
(105, '4hg20cs028', '2024-05-12', '18:33:41', '0'),
(106, '4HG20CS029', '2024-05-12', '18:33:41', '0'),
(107, '4HG20CS029', '2024-05-12', '18:34:02', '0'),
(108, '4HG20CS029', '2024-05-12', '18:34:02', '0'),
(109, '4HG20CS029', '2024-05-12', '19:30:30', '0'),
(110, '4HG20CS029', '2024-05-12', '19:30:30', '0'),
(111, '4HG20CS029', '2024-05-12', '19:32:36', '0'),
(112, '4HG20CS029', '2024-05-12', '19:32:36', '0'),
(113, '4HG20CS029', '2024-05-12', '19:41:21', '0'),
(116, '4HG20CS029', '2024-05-12', '20:21:06', '0'),
(117, '4HG20CS023', '2024-05-12', '20:21:06', '0'),
(118, '4HG20CS029', '2024-05-12', '20:22:25', '1'),
(119, '4HG20CS009', '2024-05-13', '09:30:50', '1'),
(120, '4hg20cs028', '2024-05-13', '09:30:52', '0'),
(121, '4HG20CS009', '2024-05-13', '09:30:52', '0'),
(122, '4HG20CS023', '2024-05-13', '09:30:52', '0'),
(123, '4HG20CS029', '2024-05-13', '09:30:52', '0'),
(124, '4HG20CS009', '2024-05-13', '09:33:05', '1'),
(125, '4HG20CS029', '2024-05-13', '09:33:05', '1'),
(126, '4HG20CS009', '2024-05-13', '12:50:38', '0'),
(127, '4HG20CS023', '2024-05-13', '12:50:39', '1'),
(128, '4HG20CS029', '2024-05-13', '12:50:39', '1'),
(129, '4HG20CS023', '2024-05-13', '12:50:39', '1'),
(130, '4HG20CS029', '2024-05-13', '13:59:33', '1'),
(131, '4HG20CS023', '2024-05-13', '13:59:33', '1'),
(132, '4HG20CS009', '2024-05-13', '13:59:34', '0'),
(133, '4HG20CS029', '2024-05-29', '09:17:13', '0'),
(134, '4HG20CS029', '2024-05-29', '09:17:13', '0');

-- --------------------------------------------------------

--
-- Table structure for table `dept_login`
--

CREATE TABLE `dept_login` (
  `dept_id` varchar(10) NOT NULL,
  `dept_head_name` varchar(20) NOT NULL,
  `dept_branch` varchar(20) NOT NULL,
  `dept_passwd` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dept_login`
--

INSERT INTO `dept_login` (`dept_id`, `dept_head_name`, `dept_branch`, `dept_passwd`) VALUES
('CSE24', 'suprith', 'CSE', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `faculty_db`
--

CREATE TABLE `faculty_db` (
  `staff_id` varchar(10) NOT NULL,
  `staff_branch` varchar(20) NOT NULL,
  `staff_name` varchar(20) NOT NULL,
  `staff_passwd` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `faculty_db`
--

INSERT INTO `faculty_db` (`staff_id`, `staff_branch`, `staff_name`, `staff_passwd`) VALUES
('18cs22', 'CSE', 'prakash', 'Prakash@%143'),
('CSE23', 'CSE', 'manu', 'Prakash@%143');

-- --------------------------------------------------------

--
-- Table structure for table `student_db`
--

CREATE TABLE `student_db` (
  `usn` varchar(10) NOT NULL,
  `name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_db`
--

INSERT INTO `student_db` (`usn`, `name`) VALUES
('4HG20CS009', 'HEMALATHA N K'),
('4HG20CS029', 'SUPRITH M S');

-- --------------------------------------------------------

--
-- Table structure for table `subject_log`
--

CREATE TABLE `subject_log` (
  `subject_code` varchar(10) NOT NULL,
  `subject_faculty` varchar(20) NOT NULL,
  `branch_allot` varchar(20) NOT NULL,
  `sem_allot` varchar(20) NOT NULL,
  `start_time` varchar(10) NOT NULL,
  `end_time` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subject_log`
--

INSERT INTO `subject_log` (`subject_code`, `subject_faculty`, `branch_allot`, `sem_allot`, `start_time`, `end_time`) VALUES
('18CS71', 'Rakshita', 'cse', '8', '08:00:00', '23:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance_log`
--
ALTER TABLE `attendance_log`
  ADD PRIMARY KEY (`sl_no`);

--
-- Indexes for table `dept_login`
--
ALTER TABLE `dept_login`
  ADD PRIMARY KEY (`dept_id`);

--
-- Indexes for table `faculty_db`
--
ALTER TABLE `faculty_db`
  ADD PRIMARY KEY (`staff_id`);

--
-- Indexes for table `student_db`
--
ALTER TABLE `student_db`
  ADD PRIMARY KEY (`usn`);

--
-- Indexes for table `subject_log`
--
ALTER TABLE `subject_log`
  ADD PRIMARY KEY (`subject_code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendance_log`
--
ALTER TABLE `attendance_log`
  MODIFY `sl_no` int(254) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=135;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
