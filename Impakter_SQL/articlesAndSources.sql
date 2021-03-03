USE impakter_index;
DROP TABLE IF EXISTS sources;


---old me and MySQL
CREATE TABLE sources
(
    Source_Name VARCHAR(45),
    Source_Type ENUM('Research Report',
    'News Publication'
) ,
Credibility ENUM('FirstHand','Tier 1','Tier 3','Tier 4'),
Period ENUM('Real-time','Daily','Weekly','Monthly','Annual','Occasional'),
Specificity ENUM('Specific','Generic'),
Source_Url VARCHAR(250)
);


SELECT *
FROM articles where sourceID = 25;


---SQLITE
drop table if exists sources;
create table sources
(
    sourceID    INTEGER primary key AUTOINCREMENT,
    name        varchar(100),
    country char(2),
    typeID      tinyint,
    credibility_score      tinyint,
    specificity tinyint,
    url         VARCHAR(1000),
    frequencyID tinyint,
    publishing_organization varchar(100)
);

drop table if exists source_types;
create table source_types
(
typeID tinyint primary key,
name varchar(100)
);


drop table if exists frequency;
create table frequency
(
frequencyID tinyint primary key,
name varchar(100)
);


drop table if exists source_industry;
create table source_industry
(
    sourceID   int,
    industryID int
);



drop table if exists articles;
create table articles
(
    articleID    varchar(25) PRIMARY KEY,
    url          varchar(1000),
    sourceID     integer,
    content_hash varchar(25),
    summary      text,
    datetime     text,
    FOREIGN KEY (sourceID) REFERENCES sources(sourceID)
);

alter table articles add column keywords text;
alter table articles add column content text;

drop table if exists article_category;
create table article_category
(
    articleID varchar(25) not null,
    categoryID  tinyint NOT null,
    FOREIGN KEY (articleID) REFERENCES articles(articleID),
    FOREIGN KEY (categoryID) REFERENCES category_types(categoryID)
);

drop table if exists category_types;
create table category_types
(
    categoryID  integer primary key autoincrement,
    name varchar(100)
);



drop table if exists article_company;
create table article_company
(
    articleID varchar(25) NOT NULL,
    companyID int NOT NULL,
    FOREIGN KEY (articleID) REFERENCES articles(articleID),
    FOREIGN KEY (companyID) REFERENCES companies_temp(companyID)
);




---Indexes

CREATE INDEX Index_articles
ON articles(articleID,content_hash);

alter table article_company add constraint fk_article_company foreign key (companyID) references companies_temp(companyID);