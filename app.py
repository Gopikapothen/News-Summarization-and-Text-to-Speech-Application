import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import gradio as gr
import json
import os
from gtts import gTTS

# Function to scrape news articles
def get_news(company):
    search_url = f"https://news.google.com/search?q={company}&hl=en"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return "Error: Unable to fetch news articles."
    
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    
    for article in soup.select("article")[:10]:  # Limit to 10 articles
        title = article.select_one("h3").text if article.select_one("h3") else "No title"
        summary = article.select_one("p").text if article.select_one("p") else "No summary"
        link = article.find("a")["href"] if article.find("a") else "#"

        articles.append({"Title": title, "Summary": summary, "Link": f"https://news.google.com{link}"})

    return articles

# Function for sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Function to generate comparative sentiment analysis
def comparative_analysis(articles):
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    
    for article in articles:
        sentiment = analyze_sentiment(article["Summary"])
        article["Sentiment"] = sentiment
        sentiment_counts[sentiment] += 1

    return sentiment_counts, articles

# Function to generate Hindi TTS
def generate_tts(text, filename="output.mp3"):
    tts = gTTS(text=text, lang="hi")
    tts.save(filename)
    return filename

# Main function for the Gradio interface
def process_company(company):
    articles = get_news(company)
    if isinstance(articles, str):  # Error handling
        return articles, "", "", ""

    sentiment_counts, processed_articles = comparative_analysis(articles)

    # Prepare final analysis summary
    analysis_summary = f"Company: {company}\n"
    analysis_summary += f"Positive Articles: {sentiment_counts['Positive']}, Negative Articles: {sentiment_counts['Negative']}, Neutral Articles: {sentiment_counts['Neutral']}\n"

    # Convert summary to Hindi and generate speech
    hindi_summary = f"{company} के समाचार सारांश:\nसकारात्मक लेख: {sentiment_counts['Positive']}, नकारात्मक लेख: {sentiment_counts['Negative']}, तटस्थ लेख: {sentiment_counts['Neutral']}।"
    tts_filename = generate_tts(hindi_summary)

    return json.dumps(processed_articles, indent=4), sentiment_counts, analysis_summary, tts_filename

# Gradio UI
iface = gr.Interface(
    fn=process_company,
    inputs="text",
    outputs=["text", "label", "text", "audio"],
    title="News Sentiment Analysis and Hindi TTS",
    description="Enter a company name to analyze its latest news articles and generate sentiment-based audio in Hindi."
)

iface.launch()
