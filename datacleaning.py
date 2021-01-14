from nltk.tokenize import WordPunctTokenizer
from bs4 import BeautifulSoup
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import re
from pprint import pprint

plt.style.use('fivethirtyeight')

# matplotlib inline
# config InlineBackend.figure_format = 'retina'

cols = ['namaakun', 'tweet', 'label']

df = pd.read_csv("datasettwitter.csv", header=None, names=cols)

tok = WordPunctTokenizer()

pat1 = r'@[A-Za-z0-9]+'
pat2 = r'https?://[A-Za-z0-9./]+'
combined_pat = r'|'.join((pat1, pat2))


def tweet_cleaner(tweet):
    soup = BeautifulSoup(tweet, 'lxml')
    souped = soup.get_text()
    stripped = re.sub(combined_pat, '', souped)
    try:
        clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        clean = stripped
    letters_only = re.sub("[^a-zA-Z]", " ", clean)
    lower_case = letters_only.lower()
    # During the letters_only process two lines above, it has created unnecessay white spaces,
    # I will tokenize and join together to remove unneccessary white spaces
    words = tok.tokenize(lower_case)
    return (" ".join(words)).strip()


testing = df.tweet
username = df.namaakun
i = 0
while i < len(testing):
    with open('dataset_twitter_clean.csv', 'a', encoding='utf-8') as f:
        try:
            username = df.namaakun[i]
            data_tweet = tweet_cleaner(testing[i]).replace("\n","")
            f.write(f'"{username}","{data_tweet}"')
            f.write('\n')
        except:
            print(testing[i])
        i += 1

