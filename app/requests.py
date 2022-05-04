import urllib.request,json
from .models import Articles,Sources


# getting the api key
api_key = None

# getting the articles and sources base url
base_url = None
articles_url = None
sources_url = None


def configure_request(app):
    '''funcion that takes in the application instance and replaces the values of the none variables to application configuration objects'''
    
    global api_key,base_url, articles_url,sources_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCE_ARTICLES_URL']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['NEWS_ARTICLES_APL_URL']

def get_sources(category):
    """
    function that gets response from the api call
    """
    sources_url = base_url.format(category,api_key)
    with urllib.request.urlopen(sources_url) as url:

        sources_data = url.read()
        response = json.loads(sources_data) 

        sources_outcome = None        
        if response['sources']:
            sources_outcome_items = response['sources']
            sources_outcome = process_new_sources(sources_outcome_items)
    return sources_outcome

def process_new_sources(sources_list):

    sources_outcome = []    
    for one_source in sources_list:
        id = one_source.get("id")
        name = one_source.get("name")
        description = one_source.get("description")
        url = one_source.get("url")
        category = one_source.get("category")
        language = one_source.get("language")
        country = one_source.get("country")        
        new_source = Sources(id,name,description,url,category,language,country)
        sources_outcome.append(new_source)    
    return sources_outcome