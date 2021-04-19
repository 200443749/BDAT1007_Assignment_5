from textblob import TextBlob
import requests
import os
import pandas as pd
import csv
import nltk
import re
import string
from nltk.sentiment import SentimentAnalyzer
from nltk.stem.porter import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from pymongo import MongoClient
pos_count = 0
pos_correct = 0
neg_correct = 0
neg_count = 0
positive_count=0
negative_count=0
netural_count=0
positive_list=[]
negative_list=[]
neutral_list=[]
polarity_list=[]
subjectivity_list=[]
word_list=[]
subject_list=[]
polar_list=[]
df = pd.read_csv ('hotel_ind_data.csv')
test = pd.DataFrame(df)
news_data=test["Reviews"].dropna()
hotel_data=test["Hotel Name"].dropna()
# # removing extra spaces

for data in news_data:
    new_doc=re.sub("s+"," ", data)

    # Removing punctuations
    punc_data=re.sub("[^-9A-Za-z ]", "" , new_doc)
    text_clean = "".join([i for i in punc_data if i not in string.punctuation])

    #case normalization
    text_norm = "".join([i.lower() for i in text_clean if i not in string.punctuation])
    # print("Normalization",text_clean)

    analysis_data = TextBlob(text_norm)
    polarity_value = analysis_data.sentiment.polarity
    polar_list.append(polarity_value)
    if polarity_value > 0:
        polarity_data = 'Positive'
        polarity_list.append(str(polarity_data))
    elif polarity_value < 0:
        polarity_data = 'Negative'
        polarity_list.append(polarity_data)
    else:
        polarity_data = 'Neutral'
        polarity_list.append(polarity_data)
    sentim_analyzer = SentimentIntensityAnalyzer()
    subjectivity_value = analysis_data.sentiment.subjectivity
    subject_list.append(str(subjectivity_value))
    if subjectivity_value > 0:
        subjectivity_data = 'Subjective'
        subjectivity_list.append(str(subjectivity_data))
    elif subjectivity_value == 0:
        subjectivity_data = 'Neutral'
        subjectivity_list.append(subjectivity_data)
    else:
        subjectivity_data = 'Objective'
        subjectivity_list.append(subjectivity_data)

percentile_list = pd.DataFrame(
    {'Hotel Name': hotel_data,
     'Reviews': news_data,
     'Polarity': polar_list,
     'Subjectivity': subject_list,
     'Results': polarity_list
    })
percentile_list.to_csv('sent_analysis.csv')