from tweepy import StreamingClient, StreamRule
from os import getenv


class Streamer(StreamingClient):
    def on_tweet(self, tweet):
        print(f"Received tweet with id {tweet.id}")


class StreamManager:
    client: Streamer

    def __init__(self):
        self.client = Streamer(getenv('TWITTER_BEARER'))
        self.client.add_rules(StreamRule('from:itbfess'))

    def run(self):
        self.client.filter()

    def test(self):
        self.client.sample()
