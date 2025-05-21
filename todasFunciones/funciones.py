


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


def cargarLogs():
    dicFinal=[]
    with open("./todosDatos/reportes.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def logsJSON(dic):
    dicTemporal = []
    
    
    diccTemporal=cargarLogs()
    
    dicTemporal.append(dic)
    with open("./todosDatos/reportes.json",'w') as outFile:
        json.dump(dicTemporal,outFile)