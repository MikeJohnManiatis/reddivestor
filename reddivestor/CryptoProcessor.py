from Processor import Processor
from bs4 import BeautifulSoup


class CryptoProcessor(Processor):
    
    def __init__(self):
        super(CryptoProcessor, self).__init__()
        self.test_coin_list = ["btc", "bitcoin", "eth", "ethereum", "bch", "bitcoin cash", "bitcoincash", "satoshi", "xrp", "cardano", "ada", "binancecoin", "binance coin", "bnb", "litecoin", "ltc", "chainlink", "link"]
        self.seen_post_titles = []

    def handle(self, message: BeautifulSoup):
        for message_item in message.findAll('h3'):
            post_title = message_item.text.lower()
            if(post_title not in self.seen_post_titles):
                for word in post_title.split(" "):
                    if (word in self.test_coin_list):
                        if(word not in self.processor_dict.keys()):
                            self.processor_dict[word] = 1
                        else:
                            self.processor_dict[word] = self.processor_dict[word] + 1
            self.seen_post_titles.append(post_title)