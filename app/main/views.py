# from email import message
from flask import render_template
from . import main
from ..requests import get_articles,get_sources,search_articles,articles_source
from app import app

# views 
@main.route('/')
def HomePage():
    '''View root page function that returns the index page and its data'''

    all_news = get_sources('general')
    sports = get_sources('sports')
    business = get_sources("business")
    return render_template('index.html', all_news=all_news,sports=sports,business=business)

@main.route('/articles/<id>')
def sourceArticles(id):
    all_articles = articles_source(id)
    print(all_articles)
    source = id

    return render_template('sourcearticles.html', articles = all_articles, source = source)

@main.route('/News-Articles')
def NewsArticles():
    """
    View that would return news articles    """
    health_articles = get_articles('health')
    education_articles = get_articles('technology')

    return render_template('articles.html',health=health_articles, tech =education_articles)
