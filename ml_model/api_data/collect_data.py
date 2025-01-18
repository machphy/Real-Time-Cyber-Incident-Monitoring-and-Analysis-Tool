import tweepy
import requests
from bs4 import BeautifulSoup
import csv
import json
import os

# Directory to store collected data
DATA_DIR = "../data/"
os.makedirs(DATA_DIR, exist_ok=True)

# Load API credentials from environment variables
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")


def collect_twitter_data():
    """Fetch recent tweets related to cyber incidents."""
    try:
        # Authenticate with Twitter API
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)

        # Define search query
        query = "cyber attack OR data breach -filter:retweets"
        tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(100)

        # Collect tweet data
        data = []
        for tweet in tweets:
            data.append({
                "id": tweet.id_str,
                "text": tweet.full_text,
                "created_at": tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "user": tweet.user.screen_name,
                "location": tweet.user.location
            })

        # Save data to JSON file
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

        # Save data to JSON file
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
