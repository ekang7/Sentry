from nltk.stem import WordNetLemmatizer
import nltk
import json
from nltk.stem import PorterStemmer
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
import messager
    
hot = ['toxic', 'shoot', 'shot', 'blood', 'bleed', 'viru', 'kill', 'murder', 'injur', 'harm', 'attack', 'offend', 'arm', 'gun', 'steal', 'stole', 'robberi', 'punch', 'fire', 'infect', 'sti', 'sexual', 'rape', 'explos', 'explod', 'food-born', 'ill', 'salmonella', 'ebola', 'coli', 'gun', 'loos', 'stole', 'disast', 'tornado', 'hurrican', 'storm', 'sex', 'harrass', 'offend', 'killer', 'serial', 'bomb', 'threat', 'close', 'fled', 'flee', 'escap', 'flood', 'contamin', 'expos', 'danger', 'lose', 'fire', 'nake', 'broke', 'substanc', 'fight', 'fought']

stemmer = PorterStemmer()

# Go Back To Your Twitter App Tab For This Info 
client_key = "9xFso8bhX4sYKGP9GkRJG0JKY"
client_secret = "ZTAAa9BgwkwjFp8Fp4Jtu0FxjATRBUteo83RwWK1AviORSloxs"
token = "1101597753526886401-HH48H6szBLbDSJsB2IE8TfHeGs5cX7"
token_secret = "R81HuP9KK1N8mTHFABuyzTbldA9E5A9qSu2MwH19cyNnW"
# Send Notification to Slack

# Stream Listener Class
class TweetListener(StreamListener):
    
    def on_data(self, data):
        try:
            tweet = json.loads(data)
            # Send Tweet To Slack Notification
            print (tweet)
            text = tweet['text']
            text = text.split ('\n')
            if (len (text) == 4):
                address = text[1]
                text = text[2]
            elif (len(text)==3):
                address = ""
                text = text[1]
            else:
                address = ""
                text = text[0]
            stemmer.stem(text)
            num_matched = 0
            for keyword in hot:
                if (keyword in text.lower()):
                    num_matched += 1
            if (num_matched >= 1):
                messager.send ("New Alert Nearby: " + tweet['text'], carrier='att')
                messager.send ("New Alert Nearby: " + tweet['text'], carrier='tmobile')
                messager.send ("New Alert Nearby: " + tweet['text'], carrier='sprint')
                messager.send ("New Alert Nearby: " + tweet['text'], carrier='verizon')
            return True
        except:
            return True
    def on_error(self, status):
        print ("Error: %s" % status)

listener = TweetListener()
auth = OAuthHandler(client_key, client_secret)
auth.set_access_token(token, token_secret)
stream = Stream(auth, listener)
print ("Listening to twitter")
# stream.filter(follow=["522052782"])
stream.filter (follow=["720733640796336128"])