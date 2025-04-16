import json
import pyaudio
import os
import vosk
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
        print(answer)
        try:
            os.startfile(conf[answer])
        except:
            if answer!='':
                return answer