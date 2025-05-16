import json

def abrirJSON():
    dicFinal={}
    with open("./miArchivo.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./miArchivo.json",'w') as outFile:
        json.dump(dic,outFile)