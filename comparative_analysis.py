from collections import Counter

def analyze_sentiments(articles):
    sentiment_counts = Counter(article['Sentiment'] for article in articles)
    
    total = len(articles)
    sentiment_distribution = {k: round(v / total, 2) for k, v in sentiment_counts.items()}

    return {"Sentiment Distribution": sentiment_distribution}

def topic_overlap(articles):
    common_topics = set.intersection(*[set(article['Topics']) for article in articles if 'Topics' in article])
    unique_topics = {f"Unique Topics in Article {i+1}": list(set(article['Topics']) - common_topics) for i, article in enumerate(articles)}
    
    return {"Common Topics": list(common_topics), **unique_topics}
