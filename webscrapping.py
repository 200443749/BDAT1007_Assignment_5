from flask import Flask, render_template, session, request, redirect
from flask import Flask, jsonify, render_template, url_for
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import csv

urls=["https://www.expedia.ca/Toronto-Hotels.d178314.Travel-Guide-Hotels"]
name_list=[]
ratings_list=[]
price_match_list=[]
namee_list=[]
review_list=[]
rating=[]
revieww_list=[]
address_list=[]
post_price_list=[]
news_list=[]
for i in range(len(urls)):
    source=requests.get(urls[i])
    soup=BeautifulSoup(source.content,'html.parser')
    hotel_name = soup.find_all('div', class_ = 'uitk-cell')
    hotel_price = soup.find_all('div',class_='uitk-price-lockup')
    Address_name = soup.find_all('div',class_= 'uitk-type-300')
    Ratings = soup.find_all('div',class_='uitk-type-300 truncate')
    print(hotel_name)

    # Hotel Name list
    for hname in hotel_name:
        hlist=hname.find('a').find('h3')
        if hlist is not None:
            alist=hlist.find('h3',class_='uitk-type-heading-500')
            name_list.append(alist)

    # Price list
    for i in hotel_price:
        post_price=i.find('span',class_='uitk-lockup-price')
        if post_price is not None:
            post_price_list.append(post_price.text)

    # Address Name list
    for i in Address_name:
        if i is not None:
            address_list.append(i.text)

    # Ratings list
    for i in Ratings:
        hlist=hname.find('span',class_="hotelRating")
        if hlist is not None:
            ratings_list.append(hlist)

    # No of Reviews list
    for i in Address_name:
        nlist=Ratings.find('span',class_="uitk-type-300")
        if i is not None:
            review_list.append(i.text)
di1={'Hotel_Name': namee_list,'Price_Per_Night':news_list,'Address':post_price_list,'Ratings':ratings_list,'No_of_reviews':review_list}
df = pd.DataFrame.from_dict(di1,orient='index')
df.transpose()
df.to_csv('hotels_data.csv')