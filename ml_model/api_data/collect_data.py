import tweepy
import requests
from bs4 import BeautifulSoup
import csv
import json
import os

DATA_DIR = "../data/"
os.makedirs(DATA_DIR, exist_ok=True)


API_KEY = "QewpIOX1bqQoGzABUDZWsbAWM"
API_SECRET_KEY = "XtPNn0Z2RXTwgY9H5vphZfOAk278ggc2vlRxtfaPpZ1WcCQGuQ"
ACCESS_TOKEN = "1479660185589141504-mQcCLzvREVsHoKnVLZdnVmBPMuPHMi"
ACCESS_SECRET = "hdzkkXZsqeeuN610gT4QY19OdgBOUnkt1UH6rQHgc7a2s"

def collect_twitter_data():
    """Fetch recent tweets related to cyber incidents."""
    try:
    
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)


        query = "cyber attack OR data breach -filter:retweets"
        tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(100)

        
        data = []
        for tweet in tweets:
            data.append({
                "id": tweet.id_str,
                "text": tweet.full_text,
                "created_at": tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "user": tweet.user.screen_name,
                "location": tweet.user.location
            })

       
        with open(os.path.join(DATA_DIR, "twitter_data.json"), "w") as file:
            json.dump(data, file, indent=4)

        print("✅ Twitter data collected successfully!")

    except Exception as e:
        print(f"❌ Error collecting Twitter data: {e}")


def collect_news_data():
    """Scrape cybersecurity news headlines."""
    url = "https://www.cybersecurity-insiders.com/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        articles = []
        for article in soup.find_all("article"):
            headline = article.find("h2").text.strip()
            link = article.find("a")["href"]
            articles.append({"headline": headline, "link": link})

        
        with open(os.path.join(DATA_DIR, "news_data.json"), "w") as file:
            json.dump(articles, file, indent=4)

        print("✅ News data collected successfully!")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching news data: {e}")


def load_predefined_dataset():
    """Create and save a sample predefined cybersecurity dataset."""
    predefined_data = [
        ["Date", "Incident", "Details"],
        ["2024-01-01", "Data Breach", "Breach in XYZ company affecting 1M users"],
        ["2024-02-15", "Ransomware", "Ransomware attack on ABC hospital system"]
    ]

    with open(os.path.join(DATA_DIR, "predefined_dataset.csv"), "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(predefined_data)

    print("✅ Predefined dataset saved successfully!")


if __name__ == "__main__":
    print("🚀 Starting data collection...")
    collect_twitter_data()
    collect_news_data()
    load_predefined_dataset()
    print("🎉 Data collection completed. All files saved in the data/ directory.")
