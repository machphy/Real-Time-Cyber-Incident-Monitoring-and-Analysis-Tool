from services.twitter_scraper import fetch_twitter_data
from services.news_scraper import fetch_news_data
from utils.database import save_to_database

def ingest_data():
    # data take from twit
    twitter_data = fetch_twitter_data()
    save_to_database(twitter_data, "incidents")

    # news data
    news_data = fetch_news_data()
    save_to_database(news_data, "incidents")

if __name__ == "__main__":
    ingest_data()
