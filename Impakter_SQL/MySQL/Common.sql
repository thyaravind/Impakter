Use impakter_common;
drop table if exists industries;
Create table industries
(
    industryID char(1) primary key,
    name varchar(200),
    description text

);


drop table if exists sdgs;
Create table sdgs
(
    sdgID tinyint primary key,
    name varchar(200),
    description text

);


drop table if exists regions;
Create table regions
(
    regionID tinyint primary key,
    name varchar(200),
    description text

);


drop table if exists countries;
Create table countries
(
    countryID tinyint primary key,
    regionID tinyint,
    name varchar(200),
    description text

);



drop table if exists industrySectors;
Create table industrySectors
(
    industrySectorID int primary key,
    industryID int not null,
    name varchar(200),
    description text

);

drop table if exists sdgTargtes;
Create table sdgTargets
(
    sdgTargetID char(5) primary key,
    sdgID tinyint not null,
    name varchar(200),
    description text

);