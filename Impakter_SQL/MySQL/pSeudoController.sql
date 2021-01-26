select * from impakter_certificates.certificates;

select * from impakter_certificates.certificateOrganizations;

CALL impakter_certificates.spAddCertificate("Test Certificate",1,"Certificate Desc")