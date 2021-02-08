use indexCertificates;

DELIMITER //

CREATE PROCEDURE spAddCertificate(in_name  varchar(200),in_organizationID int,in_description text)
BEGIN
    insert into certificates (name, organizationID, description) values (in_name,in_organizationID,in_description);

end//

DELIMITER ;



DELIMITER //
CREATE PROCEDURE spAddCertOrganization(IN in_name  varchar(200))
BEGIN
    insert into impakter_certificates.certificateOrganizations (name) values (in_name);

end//

DELIMITER ;
