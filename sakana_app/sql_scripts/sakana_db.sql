-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sakana_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sakana_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sakana_db` DEFAULT CHARACTER SET utf8 ;
USE `sakana_db` ;

-- -----------------------------------------------------
-- Table `sakana_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakana_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `address` VARCHAR(255) NULL,
  `city` VARCHAR(100) NULL,
  `state` VARCHAR(100) NULL,
  `zipcode` INT NULL,
  `password` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakana_db`.`sushi`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakana_db`.`sushi` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `price` INT NULL,
  `description` VARCHAR(255) NULL,
  `rolls_number` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakana_db`.`beverages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakana_db`.`beverages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `price` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakana_db`.`sides`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakana_db`.`sides` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `price` INT NULL,
  `description` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakana_db`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakana_db`.`orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `side_id` INT NOT NULL,
  `beverage_id` INT NOT NULL,
  `sushi_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_orders_sides1_idx` (`side_id` ASC) VISIBLE,
  INDEX `fk_orders_beverages1_idx` (`beverage_id` ASC) VISIBLE,
  INDEX `fk_orders_sushi1_idx` (`sushi_id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_sides1`
    FOREIGN KEY (`side_id`)
    REFERENCES `sakana_db`.`sides` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_beverages1`
    FOREIGN KEY (`beverage_id`)
    REFERENCES `sakana_db`.`beverages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_sushi1`
    FOREIGN KEY (`sushi_id`)
    REFERENCES `sakana_db`.`sushi` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakana_db`.`past_orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakana_db`.`past_orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `order_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_past_orders_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_past_orders_orders1_idx` (`order_id` ASC) VISIBLE,
  CONSTRAINT `fk_past_orders_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `sakana_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_past_orders_orders1`
    FOREIGN KEY (`order_id`)
    REFERENCES `sakana_db`.`orders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakana_db`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakana_db`.`favorites` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `order_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_favorites_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_favorites_orders1_idx` (`order_id` ASC) VISIBLE,
  CONSTRAINT `fk_favorites_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `sakana_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorites_orders1`
    FOREIGN KEY (`order_id`)
    REFERENCES `sakana_db`.`orders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
