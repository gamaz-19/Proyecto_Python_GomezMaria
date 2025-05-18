import json


import json

def abrirJSON():
    dicFinal=[]
    with open("./todosDatos/gastosNuevos.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal



def guardarJSON(dic):
    with open("./todosDatos/gastosNuevos.json",'w') as outFile:
        json.dump(dic,outFile)