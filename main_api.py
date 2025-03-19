from fastapi import FastAPI
from news_scraper import get_news
from sentiment_analysis import get_sentiment
from comparative_analysis import analyze_sentiments
from tts_generator import generate_tts

app = FastAPI()

@app.get("/news/{company}")
def fetch_news(company: str):
    articles = get_news(company)
    for article in articles:
        article["Sentiment"] = get_sentiment(article["Summary"])
    
    sentiment_analysis = analyze_sentiments(articles)
    
    structured_report = {
        "Company": company,
        "Articles": articles,
        "Comparative Sentiment Score": sentiment_analysis,
        "Final Sentiment Analysis": f"{company}'s news has mixed reviews.",
        "Audio": generate_tts(f"{company} की समाचार रिपोर्ट तैयार है।")
    }

    return structured_report
