insert into sources (name) values ('The Verge'),('The New York Times'),('CNN'),('Forbes');

insert into category_types (name) values ('Sustainability'),('Business'),('Finance'),('Tehnology'),('Legal'),('Operations');

insert into companies_temp (name)  values ('Apple'),('Intel'),('Google'),('Microsoft');



insert into article_company (articleID, companyID) values ()

select * from source_types;

select * from sources;
select * from articles;
select * from articles_duplicate_2;
select * from article_category;
select * from category_types;
select * from article_company;
select * from companies_temp;




delete from sources;
delete from articles;
delete from article_company;
delete from article_category;
delete from companies_temp where companyID = 103;


select url from articles where sourceID = 1  limit 1;
update sources set url = "www.apple.com" where sourceID = 1

select sourceID,name,url from sources

alter table sources rename column url to source_url