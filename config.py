from distutils.debug import DEBUG
import os

from instance.config import NEWS_API_KEY 


class Config:
    '''General configuration parent class'''

    NEWS_API_BASE_URL =  'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_ARTICLES_APL_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}' 


class ProdConfig(Config):
    '''Production configuration child class
    Args:
        Config: The parent configuration  class with general configuration settings'''

    pass

class DevConfig(Config):
    '''Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings'''

    DEBUG=True


