Use indexCertificates;
drop table if exists certificates;
Create table certificates
(
    certificateID    int   NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name  varchar(200) NOT NULL,
    organizationID varchar(200) NOT NULL,
    description  text,
    logoPath varchar(200),
    applicationLength text,
    priority tinyint,
    difficulty tinyint,
    relevance tinyint,
    validity varchar(100),
    goal varchar(100),
    specificity text,
    pricing text,
    sdgEngagement text
);


drop table if exists certificate_region;
Create table certificate_region
(
    certificateID    int NOT NULL,
    regionID smallint not null

);

drop table if exists certificate_country;
Create table certificate_country
(
    certificateID    int NOT NULL,
    countryID int not null

);

drop table if exists certificate_industry;
Create table certificate_industry
(
    certificateID    int NOT NULL,
    industryID char(1) not null

);

drop table if exists certificate_sdg;
Create table certificate_sdg
(
    certificateID    int NOT NULL,
    sdgID tinyint not null

);


drop table if exists certificate_industrySector;
Create table certificate_industrySector
(
    certificateID    int NOT NULL,
    industrySectorID int not null

);

drop table if exists certificate_sdgTarget;
Create table certificate_sdgTarget
(
    certificateID    int NOT NULL,
    sdgTargetID char(5) not null

);


