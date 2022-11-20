-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-11-20 03:04:44
-- 伺服器版本： 10.4.25-MariaDB
-- PHP 版本： 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `item`
--

-- --------------------------------------------------------

--
-- 資料表結構 `mitemlist`
--

CREATE TABLE `mitemlist` (
  `id` int(11) NOT NULL,
  `name` varchar(15) COLLATE utf8_unicode_520_nopad_ci NOT NULL,
  `price` int(11) NOT NULL,
  `inventory` int(11) NOT NULL,
  `pnum` int(11) NOT NULL,
  `pay` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_nopad_ci;

--
-- 傾印資料表的資料 `mitemlist`
--

INSERT INTO `mitemlist` (`id`, `name`, `price`, `inventory`, `pnum`, `pay`) VALUES
(10, '睡衣', 50, 999, 0, 50),
(12, '鞋子', 1, 68, 0, 15),
(15, '襪子', 39, 647, 0, 600),
(17, '安全帽', 899, 13, 0, 0);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `mitemlist`
--
ALTER TABLE `mitemlist`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `mitemlist`
--
ALTER TABLE `mitemlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
