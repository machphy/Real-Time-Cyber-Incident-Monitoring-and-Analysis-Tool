def run_pipeline():
   
    twitter_data = fetch_twitter_data()
    news_data = fetch_news_data()

    processed_data = preprocess_data(twitter_data + news_data)
    save_to_database(processed_data)
