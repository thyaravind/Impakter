Use impakter_certificates;
Create table certificateOrganizations
(
    organizationID    int PRIMARY KEY AUTO_INCREMENT,
    name  varchar(200) NOT NULL,
    countryID int,
    website varchar(200)

)
