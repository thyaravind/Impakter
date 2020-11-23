USE impakter_index;
DROP TABLE IF EXISTS companies;
CREATE TABLE companies (
Company_ID VARCHAR(10) PRIMARY KEY NOT NULL UNIQUE,
Company VARCHAR(45),
Revenue INT,
Country VARCHAR(45) DEFAULT 'United States',
Stock_market VARCHAR(45) DEFAULT 'NASDAQ', 
Ticker VARCHAR(45),
Researched BOOL DEFAULT false,
Double_checked BOOL DEFAULT false,
Triple_checked BOOL DEFAULT false,
Published BOOL DEFAULT false,
Company_Url VARCHAR(250),
Outlook ENUM('Positive','Neutral','Negative'),
Analyst_Notes TEXT,
Company_address VARCHAR(250)
);

ALTER TABLE companies
ADD COLUMN Financial_year INT,
ADD COLUMN Company_description TEXT,
ADD COLUMN Desc_long TEXT,
ADD COLUMN Sustainability TEXT,
ADD COLUMN Sustainability_long TEXT,
ADD COLUMN Rating ENUM('A','B','C','D','E');


SELECT * FROM companies;