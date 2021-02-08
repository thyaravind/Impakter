select * from certificates;
select * from certificate_sdg;
select * from certificate_sdgTarget;


select * from certificateOrganizations;

CALL spAddCertificate("Test Certificate",1,"Certificate Desc");

insert into certificateOrganizations (organizationID,name) Values ("YWIEMCAHGKDGKURSCE","Rain Forest Alliance");
insert into certificateOrganizations (organizationID,name) Values ("UYUOPEWRNYUWEOVASD","B CORP");




truncate table certificateOrganizations;