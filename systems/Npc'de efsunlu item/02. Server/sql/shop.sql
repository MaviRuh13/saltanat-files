/*
Navicat MySQL Data Transfer

Source Server         : Arkadia
Source Server Version : 50533
Source Host           : 25.85.95.100:3306
Source Database       : player

Target Server Type    : MYSQL
Target Server Version : 50533
File Encoding         : 65001

Date: 2017-03-23 22:36:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `shop`
-- ----------------------------
DROP TABLE IF EXISTS `shop`;
CREATE TABLE `shop` (
  `vnum` int(11) NOT NULL DEFAULT '0',
  `name` varchar(32) NOT NULL DEFAULT 'Noname',
  `npc_type` smallint(6) NOT NULL,
  `npc_vnum` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`vnum`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of shop
-- ----------------------------
INSERT INTO `shop` VALUES ('1', 'SHOPNAME_9001_0', '0', '9001');
INSERT INTO `shop` VALUES ('2', 'SHOPNAME_9001_1', '1', '9001');
INSERT INTO `shop` VALUES ('11', 'SHOPNAME_9002_0', '0', '9002');
INSERT INTO `shop` VALUES ('12', 'SHOPNAME_9002_1', '1', '9002');
INSERT INTO `shop` VALUES ('21', 'SHOPNAME_9003_0', '0', '9003');
INSERT INTO `shop` VALUES ('22', 'SHOPNAME_9003_1', '1', '9003');
INSERT INTO `shop` VALUES ('23', 'SHOPNAME_9003_1', '2', '9003');
INSERT INTO `shop` VALUES ('31', 'SHOPNAME_9005_0', '0', '9005');
INSERT INTO `shop` VALUES ('72', 'SHOPNAME_20094_1', '1', '20094');
INSERT INTO `shop` VALUES ('41', 'SHOPNAME_9009_0', '0', '9009');
INSERT INTO `shop` VALUES ('42', 'SHOPNAME_9009_1', '1', '9009');
INSERT INTO `shop` VALUES ('51', 'SHOPNAME_20001_0', '0', '20001');
INSERT INTO `shop` VALUES ('61', 'SHOPNAME_20084_0', '0', '20084');
INSERT INTO `shop` VALUES ('62', 'SHOPNAME_20084_1', '1', '20084');
INSERT INTO `shop` VALUES ('71', 'SHOPNAME_20094_0', '0', '20094');
INSERT INTO `shop` VALUES ('101', 'SHOPNAME_20300_0', '0', '20300');
INSERT INTO `shop` VALUES ('102', 'SHOPNAME_20300_1', '1', '20300');
INSERT INTO `shop` VALUES ('103', 'SHOPNAME_20301_0', '0', '20301');
INSERT INTO `shop` VALUES ('104', 'SHOPNAME_20301_1', '1', '20301');
INSERT INTO `shop` VALUES ('105', 'SHOPNAME_20302_0', '0', '20302');
INSERT INTO `shop` VALUES ('106', 'SHOPNAME_20302_1', '1', '20302');
INSERT INTO `shop` VALUES ('107', 'SHOPNAME_20303_0', '0', '20303');
INSERT INTO `shop` VALUES ('108', 'SHOPNAME_20303_1', '1', '20303');
INSERT INTO `shop` VALUES ('109', 'SHOPNAME_20304_0', '0', '20304');
INSERT INTO `shop` VALUES ('110', 'SHOPNAME_20304_1', '1', '20304');
INSERT INTO `shop` VALUES ('111', 'SHOPNAME_20305_0', '0', '20305');
INSERT INTO `shop` VALUES ('112', 'SHOPNAME_20305_1', '1', '20305');
INSERT INTO `shop` VALUES ('113', 'SHOPNAME_20306_0', '0', '20306');
INSERT INTO `shop` VALUES ('114', 'SHOPNAME_20306_1', '1', '20306');
INSERT INTO `shop` VALUES ('115', 'SHOPNAME_20307_0', '0', '20307');
INSERT INTO `shop` VALUES ('116', 'SHOPNAME_20307_1', '1', '20307');
INSERT INTO `shop` VALUES ('81', 'SHOPNAME_9006_0', '0', '9006');
INSERT INTO `shop` VALUES ('91', 'SHOPNAME_20015_0', '0', '20015');
INSERT INTO `shop` VALUES ('92', 'SHOPNAME_20015_1', '1', '20015');
INSERT INTO `shop` VALUES ('52', 'SHOPNAME_20001_1', '1', '20001');
