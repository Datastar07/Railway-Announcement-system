#Railway Anoucement System

# pip install pyaudio
# pip install pydub
# pip install pandas
# pip install gTTS

from fileinput import filename
import pandas as pd
import os
from pydub import AudioSegment
from gtts import gTTS

def textTospeech(text,filename):
    mytext = str(text)
    language = "hi"
    myobj = gTTS(text=mytext,lang=language,slow=True)
    myobj.save(filename)
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined
def generateskeleton():
    audio=AudioSegment.from_mp3("railway.mp3")
    
    #1-kripiya dhyan dijiye
    start=0
    finish=2800
    audioprocessed=audio[start:finish]
    audioprocessed.export("1_hindi.mp3",format="mp3")
    
    #3-generate se chalkar
    start=8700
    finish=9300
    audioprocessed=audio[start:finish]
    audioprocessed.export("3_hindi.mp3",format="mp3")

    #5-ke raste
    start=10400
    finish=11200
    audioprocessed=audio[start:finish]
    audioprocessed.export("5_hindi.mp3",format="mp3")

    #7-generate ko jane vali gadi sakhya
    start=12000
    finish=13000
    audioprocessed=audio[start:finish]
    audioprocessed.export("7_hindi.mp3",format="mp3")
   
    #9-generate kuch hi samy mai platform sakhya
    start=15500
    finish=21000
    audioprocessed=audio[start:finish]
    audioprocessed.export("9_hindi.mp3",format="mp3")

    #11-se jayegi
    start=21500
    finish=22500
    audioprocessed=audio[start:finish]
    audioprocessed.export("11_hindi.mp3",format="mp3")
def generateanoucement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
         #2-generate from city
         textTospeech(item["from"],"2_hindi.mp3")

        #4-generate via city
         textTospeech(item["via"],"4_hindi.mp3")

        #6-generate to city
         textTospeech(item["to"],"6_hindi.mp3")

        #8-generate train no and name
         textTospeech(item["train_no"]+" "+item["train_name"],"8_hindi.mp3")

        #10-generate plateform number
         textTospeech(item[""],"10_hindi.mp3")

         audios=[f"{i}_hindi.mp3"for i in range(1,12)]
         annoucement = mergeAudios(audios)
         annoucement.export(f"annoucement_{index+1}.mp3",format="mp3")

if __name__=="__main__":
    print("Generating Skeleton....")
    generateskeleton()
    print("Now Generating Anoucement...")
    generateanoucement("annoucment.xlsx")
