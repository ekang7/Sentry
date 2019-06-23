from ibm_watson import SpeechToTextV1
import time
import json
from os import listdir, remove
import messager
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import zone

# Use the application default credentials
cred = credentials.Certificate('./cred1.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

hot = ["intoxicated", "intoxicate", "toxic", "shooting","shoot","shot","blood","bleeding","virus","killed","kill","murder","murdering","murdered","injured","injury","harm","harmed","harming","attacker","offender","armed","arms","gun","steal","stole","robbery","punching","fired","fire","infected","STI","sexually","rape","raping","raped","explosion","explode","exploded","food-borne","illness","salmonella","ebola","coli","gunned","loose","disaster","tornado","hurricane","storm","sex","harrassment","harrasser","offender","killer","serial","bomb","bombing","threat","threatened","threatening","closed","close","fled","flee","escaped","flood","flooding","contaminated","contamination","contaminate","exposing","danger","lose","fire","naked","broke","substance","fight", "stolen"]

speech_to_text = SpeechToTextV1(
    iam_apikey='V_g8OgIsLNpHPQ9PBTF1i_0LnflSXmsiJiMQOZ6HOjTH',
    url='https://stream.watsonplatform.net/speech-to-text/api'
)

def getTextAndKeywords(json):
    text = ''
    keywords = []
    for result in json['results']:
        text += result['alternatives'][0]['transcript'].strip() + ' '
        if ('keywords_result' in result.keys()):
            keywords = keywords + (list(result['keywords_result'].keys()))
    
    return (text.strip(), keywords)

while(True):
    filenames = sorted([f for f in listdir('audio') if not f.startswith('.')], key= lambda x : int(x.split('.')[0]))
    if (len(filenames) > 1): # if there is only one file, it is probably being currently written to
        with open('audio/' + filenames[0], 'rb') as audio_file:
            seconds = time.time()
            try:
                speech_recognition_results = speech_to_text.recognize(
                    audio=audio_file,
                    content_type='audio/mp3',
                    keywords=hot,
                    keywords_threshold=0.01,
                    inactivity_timeout=300
                ).get_result()

                print('Recognized ' + filenames[0] + ' in ' + str(time.time() - seconds) + ' seconds')
                # print(json.dumps(speech_recognition_results, indent=2))
                text, keywords = getTextAndKeywords(speech_recognition_results)
                print(text)
                print(keywords)
                if (len(keywords) > 0):
                    messager.send("Police Radio Broadcast: "+text+"\nKeyword(s) Found: "+str(keywords))
                    # docs = db.collection('users').get()
                    # for doc in docs:
                    #     thing = doc.to_dict()
                    #     if (zone.which_zone(thing['longitude'], thing['latitude']) == 4):
                    #         messager.send("Police Radio Broadcast: "+text+"\nKeyword(s) Found: "+keywords, thing.phoneNumber)
            except Exception as e:
                print(e)
                pass

        try:
            remove('audio/' + filenames[0])
        except:
            time.sleep(30)
            remove('audio/' + filenames[0])

        
        



