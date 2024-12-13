import tweepy
import requests
from bs4 import BeautifulSoup
import csv
import json
import os


DATA_DIR = "../data/"
os.makedirs(DATA_DIR, exist_ok=True)


def collect_twitter_data():
    # Twitter API credentials (replace with your own)
    API_KEY = "QewpIOX1bqQoGzABUDZWsbAWM"
    API_SECRET_KEY = "XtPNn0Z2RXTwgY9H5vphZfOAk278ggc2vlRxtfaPpZ1WcCQGuQ"
    ACCESS_TOKEN = "1479660185589141504-mQcCLzvREVsHoKnVLZdnVmBPMuPHMi"
    ACCESS_SECRET = "hdzkkXZsqeeuN610gT4QY19OdgBOUnkt1UH6rQHgc7a2s"

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    # Query tweets
    query = "cyber attack OR data breach -filter:retweets"
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(100)

    # Save collected data
    data = []
    for tweet in tweets:
        data.append({
            "id": tweet.id_str,
            "text": tweet.full_text,
            "created_at": tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "user": tweet.user.screen_name,
            "location": tweet.user.location
        })

    # Write to JSON file
    with open(os.path.join(DATA_DIR, "twitter_data.json"), "w") as file:
        json.dump(data, file, indent=4)

    print("Twitter data collected successfully!")


# -----------------------------
# News Website Scraping
# -----------------------------
def collect_news_data():
    # Define the URL of a cybersecurity news site
    url = "https://www.cybersecurity-insiders.com/"

    # Send an HTTP request
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract headlines and links
    articles = []
    for article in soup.find_all("article"):
        headline = article.find("h2").text.strip()
        link = article.find("a")["href"]
        articles.append({"headline": headline, "link": link})

    # Save to JSON file
    with open(os.path.join(DATA_DIR, "news_data.json"), "w") as file:
        json.dump(articles, file, indent=4)

    print("News data collected successfully!")


# -----------------------------
# Predefined Dataset Handling
# -----------------------------
def load_predefined_dataset():
    # Example predefined dataset
    predefined_data = [
        ["Date", "Incident", "Details"],
        ["2024-01-01", "Data Breach", "Breach in XYZ company affecting 1M users"],
        ["2024-02-15", "Ransomware", "Ransomware attack on ABC hospital system"]
    ]

    # Write to CSV file
    with open(os.path.join(DATA_DIR, "predefined_dataset.csv"), "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(predefined_data)

    print("Predefined dataset saved successfully!")


# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    print("Starting data collection...")
    collect_twitter_data()
    collect_news_data()
    load_predefined_dataset()
    print("Data collection completed. All files saved in the data/ directory.")
