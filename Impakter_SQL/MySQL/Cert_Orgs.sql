Use indexCertificates;
drop table if exists certificateOrganizations;
Create table certificateOrganizations
(
    organizationID varchar(200) PRIMARY KEY,
    name  varchar(200) NOT NULL,
    countryID int,
    website varchar(200)

)
