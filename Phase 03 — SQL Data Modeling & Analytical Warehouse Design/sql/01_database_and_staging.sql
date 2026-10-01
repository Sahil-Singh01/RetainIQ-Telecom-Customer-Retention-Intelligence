use retainiq;
CREATE DATABASE IF NOT EXISTS retainiq;
USE retainiq;
DROP TABLE IF EXISTS stg_telco_clean;
CREATE TABLE stg_telco_clean (`Customer ID` VARCHAR(20),
`Gender` VARCHAR(20),
`Age` SMALLINT,
`Under 30` VARCHAR(10),
`Senior Citizen` VARCHAR(10),
`Married` VARCHAR(10),
`Dependents` VARCHAR(10),
`Number of Dependents` SMALLINT,
`Country` VARCHAR(100),
`State` VARCHAR(100),
`City` VARCHAR(150),
`Zip Code` INT,
`Latitude` DECIMAL(9,6),
`Longitude` DECIMAL(9,6),`Population` INT,`Quarter` VARCHAR(20),`Referred a Friend` VARCHAR(10),`Number of Referrals` INT,`Tenure in Months` SMALLINT,`Offer` VARCHAR(100),`Phone Service` VARCHAR(20),`Avg Monthly Long Distance Charges` DECIMAL(12,2),`Multiple Lines` VARCHAR(30),`Internet Service` VARCHAR(20),`Internet Type` VARCHAR(40),`Avg Monthly GB Download` INT,`Online Security` VARCHAR(20),`Online Backup` VARCHAR(20),`Device Protection Plan` VARCHAR(30),`Premium Tech Support` VARCHAR(30),`Streaming TV` VARCHAR(20),`Streaming Movies` VARCHAR(20),`Streaming Music` VARCHAR(20),`Unlimited Data` VARCHAR(20),`Contract` VARCHAR(30),`Paperless Billing` VARCHAR(20),`Payment Method` VARCHAR(50),`Monthly Charge` DECIMAL(12,2),`Total Charges` DECIMAL(14,2),`Total Refunds` DECIMAL(14,2),`Total Extra Data Charges` DECIMAL(14,2),`Total Long Distance Charges` DECIMAL(14,2),`Total Revenue` DECIMAL(14,2),`Satisfaction Score` TINYINT,`Customer Status` VARCHAR(30),`Churn Label` VARCHAR(10),`Churn Score` TINYINT,`CLTV` INT,`Churn Category` VARCHAR(100),`Churn Reason` VARCHAR(200),`is_new_customer` BOOLEAN) ENGINE=InnoDB;
-- The Jupyter notebook loads telco_clean.csv into this table using mysql-connector-python.
