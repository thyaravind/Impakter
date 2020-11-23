USE impakter_index;
DROP TABLE IF EXISTS credentials;
CREATE TABLE credentials (
Credential_Name VARCHAR(45),
Credential_ID VARCHAR(10),
Credential_Type ENUM('Certificate','Index'),
Validity INT,
Availability_Type ENUM('Directory','API','Press_Release','More than 1','NA'),
Credential_Url VARCHAR(250),
Frequency ENUM('Real-time','Daily','Weekly','Monthly','Annual','Occasional'),
Specificity ENUM('Specific','Generic'),
Directory_Url VARCHAR(250),
Notes TINYTEXT
);


SELECT * FROM credentials;

