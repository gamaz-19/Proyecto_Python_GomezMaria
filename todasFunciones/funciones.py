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


##################################
# Reporte


def abrirReportesJSON():
    repoFinal=[]
    with open("./todosDatos/reportes.json",'r') as openFile:
        repoFinal=json.load(openFile)
    return repoFinal

def guardarReportesJSON (dic):
    with open("./todosDatos/reportes.json",'w') as outFile:
        json.dump(dic,outFile)
