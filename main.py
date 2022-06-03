import requests
import json
from pymongo import MongoClient
import pandas as pd



url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"
countries=["India","Canada", "China", "Russia", "Nepal", "Germany","Afghanistan","Brazil","France","Japan"]
datalist=[]

for country in countries:
	querystring = {"country":country}

	headers = {
		"X-RapidAPI-Host": "covid-19-coronavirus-statistics.p.rapidapi.com",
		"X-RapidAPI-Key": "40b27a5d62mshead33450c6e50ccp159aeejsn1841eea50cff"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	datain = response.json()
	newdata={}
	newdata['confirmed'] =datain['data']['confirmed']

	newdata['deaths']=datain['data']['deaths']
	newdata['lastReported']=datain['data']['lastReported']
	newdata['location']=datain['data']['location']

	datalist.append(newdata)





#
#
#



# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["twitter_db"]

# Created or Switched to collection
Collection = db["cases_data"]




Collection.insert_many(datalist)