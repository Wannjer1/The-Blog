class Articles:
    '''Artcle class to define class objects'''
    def __init__(self, source, author, title, description, url, urlToImage, publishedAt):        
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage= urlToImage
        self.publishedAt = publishedAt

class ArticleReview:
    articles_reviews = []

    def __init__(self,title,urlToImage,review):
        self.title = title
        self.urlToImage = urlToImage
        self.review = review 

    def save_artcles_review(self):
        ArticleReview.articles_reviews.append(self)

    @classmethod
    def clear_articles_reviews(cls):
        ArticleReview.articles_reviews.clear()

    @classmethod
    def get_articles_reviews(cls,title):        
        article_results = []        
        for review in cls.articles_reviews:
            if review.title == title:
                article_results.append(review)        
        return article_results