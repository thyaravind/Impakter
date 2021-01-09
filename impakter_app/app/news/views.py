from flask import render_template,request
from ...Services import News, CompanyProcessor

from . import news


kwargs = {}


@news.route('/search',methods = ['GET'])
def research_home():
    return render_template('search.html')


@news.route('/search_results',methods = ['GET','POST'])
def research_results():


    if request.method == 'POST':
        kwargs["company"] = request.form['company_name']
        try:
            company = CompanyProcessor.CompanyProcessor(company = request.form['company_name'], wiki_url = request.form['company_wiki_url'])
            is_forbes_2000 = company.is_forbes_2000()
            probable_sic = company.get_sic_code()
            kwargs["sic_tables"]=[probable_sic.to_html(classes='ProjectData',index=False)]
            kwargs["sic_titles"]=probable_sic.columns.values
            if request.form['company_wiki_url']:
                _, wiki_data = company.wiki_data()
        except Exception as e:
            kwargs["status"] = f"Error {e} occured while using CompanyRetriever"
        else:
            if request.form['company_wiki_url']:
                kwargs["wiki_data"] = wiki_data #todo - wiki ProjectData persistance
            kwargs["is_forbes_2000"] = is_forbes_2000

            try:
                news = News.News()
                latest_news = news.google(period='1d', keyword=request.form['company_name']+request.form['keywords']) #date filter
                latest_news.drop(columns=['img','datetime','link'],inplace=True)
            except Exception as e:
                kwargs["status"] = f"Error {e} occured while using NewsRetriever"
            else:
                kwargs["news_tables"]=[latest_news.to_html(classes='ProjectData',index=False)]
                kwargs["news_titles"]=latest_news.columns.values
                kwargs["status"] = "Fetched ProjectData successfully"

            
    return render_template('search_results.html',**kwargs)



