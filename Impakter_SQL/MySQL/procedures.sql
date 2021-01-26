use impakter_certificates;

CREATE PROCEDURE spAddCertificate(IN in_name  varchar(200),IN in_organizationID int,IN in_description text)
BEGIN
    insert into impakter_certificates.certificates (name, organizationID, description) values (in_name,in_organizationID,in_description);

end;



CREATE PROCEDURE spAddCertOrganization(IN in_name  varchar(200))
BEGIN
    insert into impakter_certificates.certificateOrganizations (name) values (in_name);

end

