USE impakter_index;
DROP TABLE IF EXISTS sources;
CREATE TABLE sources (
Source_Name VARCHAR(45),
Source_Type ENUM('Research Report','News Publication'),
Credibility ENUM('FirstHand','Tier 1','Tier 3','Tier 4'),
Period ENUM('Real-time','Daily','Weekly','Monthly','Annual','Occasional'),
Specificity ENUM('Specific','Generic'),
Source_Url VARCHAR(250)
);


