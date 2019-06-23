import requests
import datetime
import json
import time
import messager

newskeys = ["disease","bacteria","danger","recall","sickness","sick","flu","measles","storm","weather","alert","advisory","illness","virus","coli","fungi","ebola","flood","hurricane","tornado","blackout","foodborne","food-borne","food","borne","germs","superbug","invasive","attack","bombing","bomb","fire","drought","cold"]

date = datetime.datetime.today ()
lastweek = date - datetime.timedelta (days=1)
lastweek = lastweek.strftime ('%Y-%m-%d')

start = time.time ()
url = ('https://newsapi.org/v2/everything?'
    'q=Chicago&'
    'from='+str(lastweek)+'&'
    'sortBy=relevancy&'
    'pageSize=50&'
    'apiKey=2fe38d1969c642b7a9c0db11b89b42f2&'
    'page=1')
response = requests.get(url)
news = json.loads (response.text)
for i in range (len (news['articles'])):   
    num_matched = 0
    desc = (news['articles'][i]['description'])
    for keyword in newskeys:
        try:
            if (keyword in desc.lower()):
                num_matched += 1
        except:
            num_matched = 0
    if (num_matched >= 1):
        messager.send ("The news article said: " + desc, carrier='att')
        messager.send ("The news article said: " + desc, carrier='tmobile')
        messager.send ("The news article said: " + desc, carrier='verizon')
        messager.send ("The news article said: " + desc, carrier='sprint')
        print ("Num matched: " + str(num_matched))

print (time.time() - start)