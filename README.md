# News-Summarization-and-Text-to-Speech-Application
a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi.

Project Setup

Ensure you have Python 3.8+ installed.

Install dependencies: pip install -r requirements.txt
Run the application: python app.py
Access the interface at:http://127.0.0.1:7860


Summarization: Extracts key sentences from news articles.
Sentiment Analysis: TextBlob is used to determine sentiment polarity (Positive, negative, neutral).
Text-to-Speech (TTS): Uses gTTS (Google Text-to-Speech) to generate a Hindi summary.

Assumptions & Limitations

Assumptions

News articles are available for the company entered.Sentiment analysis is based on textual polarity, without deep contextual understanding.

Limitations

Google News blocking: If too many requests are made, the scraping might fail.
Accuracy: TextBlob provides a simple sentiment analysis and may not be as accurate as deep-learning models.
TTS Quality: Google’s TTS works well but might mispronounce certain words.



