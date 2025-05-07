import json
import pyaudio
from time import sleep
import os
import vosk
import keyboard
from generate_ai_answers import create_answer_langdock
conf=json.load(open('config.json','r',encoding='utf-8'))
print(conf)

mod=vosk.Model('vosk')#-model-ru-0.42
rec=vosk.KaldiRecognizer(mod,16000)
#grammar = """
#    [
#        "позвони",[unk],
#        "найди",[unk]
#    ]
#"""
#rec.SetGrammar(grammar)
p=pyaudio.PyAudio()
op=p.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True)
print('работать')
op.start_stream()
def liten():
    data=op.read(2000,False)
    if rec.AcceptWaveform(data)==1:
        answer=json.loads(rec.Result())['text']
        answer=input('>>>')
        if 'найти в интернете' in answer or 'найди в интернете' in answer:
            find=answer.replace('найди в интернете','').replace('найти в интернете', '')
            keyboard.press_and_release('win')
            sleep(0.1)
            keyboard.write('yandex',0.1)
            keyboard.press_and_release('enter')
            sleep(0.1)
            keyboard.press_and_release('ctrl+n')
            sleep(0.1)
            keyboard.write(find,0.1)
            sleep(0.1)
            keyboard.press_and_release('enter')
        try:
            os.startfile(conf[answer])
        except:
            if answer!='':
                return create_answer_langdock(answer)