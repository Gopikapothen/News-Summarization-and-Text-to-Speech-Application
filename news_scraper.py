import requests
from bs4 import BeautifulSoup
from newspaper import Article

def get_news(company):
    search_url = f"https://www.bing.com/news/search?q={company}&FORM=HDRSC6"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for news in soup.find_all('a', class_='title')[:10]:
        title = news.text
        link = news['href']

        try:
            article = Article(link)
            article.download()
            article.parse()
            article.nlp()
            summary = article.summary
        except:
            summary = "Summary unavailable"

        articles.append({"Title": title, "Link": link, "Summary": summary})

    return articles
