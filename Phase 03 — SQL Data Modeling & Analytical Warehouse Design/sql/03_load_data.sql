USE retainiq;
INSERT INTO fact_customer_status SELECT `Customer ID`,`Tenure in Months`,`Monthly Charge`,`Total Charges`,`Total Refunds`,`Total Revenue`,`Satisfaction Score`,`Churn Score`,`CLTV`,`Churn Label`,`Customer Status` FROM stg_telco_clean;
INSERT INTO dim_demographics SELECT `Customer ID`,`Gender`,`Age`,`Under 30`,`Senior Citizen`,`Married`,`Dependents`,`Number of Dependents` FROM stg_telco_clean;
INSERT INTO dim_location SELECT `Customer ID`,`Country`,`State`,`City`,`Zip Code`,`Latitude`,`Longitude`,`Population` FROM stg_telco_clean;
INSERT INTO dim_services SELECT `Customer ID`,`Phone Service`,`Multiple Lines`,`Internet Service`,`Internet Type`,`Online Security`,`Online Backup`,`Device Protection Plan`,`Premium Tech Support`,`Streaming TV`,`Streaming Movies`,`Streaming Music`,`Unlimited Data`,`Avg Monthly Long Distance Charges`,`Avg Monthly GB Download` FROM stg_telco_clean;
INSERT INTO dim_account SELECT `Customer ID`,`Quarter`,`Referred a Friend`,`Number of Referrals`,`Offer`,`Contract`,`Paperless Billing`,`Payment Method`,`Total Extra Data Charges`,`Total Long Distance Charges` FROM stg_telco_clean;
INSERT INTO dim_churn_detail SELECT `Customer ID`,`Churn Category`,`Churn Reason` FROM stg_telco_clean;
