#########################################
####### Simulador de Gasto Diario #######
#########################################
''' 







'''

## Conexion a archivos JSON y modulos

# Modulo para formato de datos en terminal
from tabulate import tabulate

# Gastos nuevos JSON
import json
from todasFunciones.funciones import*
json.dumps([])  
dicFinal = []

listadegastos = []
listadegastos = abrirJSON()

# Modulo para convertir fechas a datetime
from datetime import datetime


# Reportes JSON
import json
from todasFunciones.funciones import abrirReportesJSON
json.dumps([])
repoFinal = []

listaReportes = []
listaReportes = abrirReportesJSON()

#####################################################################
booleano = True
while booleano :

# Menu principal
        from todasFunciones.todosMenus import menuPrincipalT
        menuPrincipalT()

        menuPrincipal = ( int ( input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))

#Registrar nuevo gasto
        if ( menuPrincipal == 1 ):        
                from todasFunciones.todosMenus import menuRegistroNuevo
                menuRegistroNuevo()

                monto = ( float ( input ("Ingrese el monto del gasto: ") ) )
                categoria = ( ( input ( "Ingrese la categoria para guardar el gasto: ")))
                descripcion = ( ( input ( "Agregue la descripcion deseada: ")))
                print ( "Ingrese una fecha: ")
                dia = ( int (input ("Dia")))
                mes = ( int (input ("Mes")))
                year = ( int (input ("Year")))
                fecha = f"{dia:02d}/{mes:02d}/{year}"
                diccionariogastos = {
                        "monto" : monto,
                        "categoria" : categoria,
                        "descripcion" : descripcion,
                        "fecha" : fecha
                }

                listadegastos["gastos"].append(diccionariogastos)   
                guardarCancelar = input ( " Ingrese 's' para guardar 'n' para cancelar\n" )
                if (guardarCancelar == "s" ):
                        guardarJSON(listadegastos)

# Listar Gastos
        elif ( menuPrincipal == 2 ):

                from todasFunciones.todosMenus import menuListarGastos
                menuListarGastos()

                opcionGastos = ( int (input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
                if ( opcionGastos == 1 ):
                        print("\nTodos los gastos: ")
                        for i in range (len(listadegastos)):
                                print(tabulate(listadegastos))

                elif ( opcionGastos == 2 ):
                        opcionCategorias = [gasto["categoria"] for gasto in listadegastos["gastos"]]
                        #Set se usa para quiter los duplicados
                        opcionCategorias = set(opcionCategorias)
                        print (opcionCategorias)
                        eleCategoria = (input(" Ingrese la categoria que quiere filtrar"))
                        for i in range (len(listadegastos["gastos"])):
                                if eleCategoria == listadegastos["gastos"][i]["categoria"]:
                                        print (listadegastos["gastos"][i])

                elif ( opcionGastos == 3 ):
                        rango = int(input(" Ingrese el rango que quiere saber\n1.Diario \n2.Semana \n3.Mes\n"))
                        if (rango == 1):
                                print (" Gasto diario")
                                print ( "Ingrese fecha del dia que quiere filtrar\n")
                                dia = ( int (input ("Dia= ")))
                                mes = ( int (input ("Mes= ")))
                                year = ( int (input ("Year= ")))
                                fechaC = f"{dia:02d}/{mes:02d}/{year}"


                                print("Para la fecha: ",fechaC)

                                for i in range (len(listadegastos["gastos"])):
                                        if fechaC == listadegastos["gastos"][i]["fecha"]:
                                                print (listadegastos["gastos"][i])  

                        elif (rango == 2):
                                print (" Gasto ultima semana")
                                print ( " Ingrese fecha inicio y fin de la semana que quiere filtrar\n")
                                print ( " Fecha de inicio: ")
                                dia = ( int (input ("Dia= ")))
                                mes = ( int (input ("Mes= ")))
                                year = ( int (input ("Year = ")))
                                fechaA = f"{dia:02d}/{mes:02d}/{year}"
                                print ( " Fecha final: ")
                                dia = ( int (input ("Dia")))
                                mes = ( int (input ("Mes")))
                                year = ( int (input ("Year\n")))
                                fechaB = f"{dia:02d}/{mes:02d}/{year}"
                                print("Para la semana del: ",fechaA, " hasta la fecha: ",fechaB)

                                # Fecha en formato

                                fechaA = datetime.strptime(fechaA, "%d/%m/%Y")
                                fechaB = datetime.strptime(fechaB, "%d/%m/%Y")

                                print(fechaA)
                                print(fechaB)

                                for i in range (len(listadegastos["gastos"])):

                                        # Fecha en formato datetime
                                        fechaFormatoDT= datetime.strptime(listadegastos["gastos"][i]["fecha"], "%d/%m/%Y")
                                        
                                        if fechaA <= fechaFormatoDT <= fechaB:
                                                print (listadegastos["gastos"][i])  

                        elif (rango == 3):
                                print (" Gasto mensual")
                                print ( " Ingrese fecha inicio y fin del mes que quiere filtrar\n")
                                print ( " Fecha de inicio: ")
                                dia = ( int (input ("Dia= ")))
                                mes = ( int (input ("Mes= ")))
                                year = ( int (input ("Year = ")))
                                fechaA = f"{dia:02d}/{mes:02d}/{year}"
                                print ( " Fecha final: ")
                                dia = ( int (input ("Dia")))
                                mes = ( int (input ("Mes")))
                                year = ( int (input ("Year\n")))
                                fechaB = f"{dia:02d}/{mes:02d}/{year}"
                                
                                print("Para la semana del: ",fechaA, " hasta la fecha: ",fechaB)

                                # Fecha en formato

                                fechaD = datetime.strptime(fechaA, "%d/%m/%Y")
                                fechaF = datetime.strptime(fechaB, "%d/%m/%Y")

                                print(fechaA)
                                print(fechaB)

                                for i in range (len(listadegastos["gastos"])):

                                        # Fecha en formato datetime
                                        fechaFormato= datetime.strptime(listadegastos["gastos"][i]["fecha"], "%d/%m/%Y")
                                        
                                        if fechaD <= fechaFormato <= fechaF:
                                                print (listadegastos["gastos"][i])    

                elif ( opcionGastos == 4 ):
                        print("")


        elif ( menuPrincipal == 3 ):

                from todasFunciones.todosMenus import menuCalcularTotalGastos
                menuCalcularTotalGastos()

                calcularTgastos = ( int (input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
                if ( calcularTgastos == 1 ):
                        print(" Calcular el total diario")
                        print ( "Ingrese fecha del dia que quiere calcular\n")
                        dia = ( int (input ("Dia= ")))
                        mes = ( int (input ("Mes= ")))
                        year = ( int (input ("Year= ")))
                        fechaE = f"{dia:02d}/{mes:02d}/{year}"


                        print("Para el dia: ",fechaE)
                        totalSumaMonto = 0
                        for i in range (len(listadegastos["gastos"])):
                                if fechaE == listadegastos["gastos"][i]["fecha"]:
                                        sumaMonto = (listadegastos["gastos"][i]["monto"])
                                        totalSumaMonto = totalSumaMonto+sumaMonto
                                        print (sumaMonto)
                                print ("Total= ",totalSumaMonto)

                elif ( calcularTgastos == 2 ):

                        print(" Calcular total semana")
                        print ( " Ingrese fecha inicio y fin del mes que quiere filtrar\n")
                        print ( " Fecha de inicio: ")
                        dia = ( int (input ("Dia= ")))
                        mes = ( int (input ("Mes= ")))
                        year = ( int (input ("Year = ")))
                        fechaA = f"{dia:02d}/{mes:02d}/{year}"
                        print ( " Fecha final: ")
                        dia = ( int (input ("Dia")))
                        mes = ( int (input ("Mes")))
                        year = ( int (input ("Year\n")))
                        fechaB = f"{dia:02d}/{mes:02d}/{year}"
                                
                        print("Para la semana del: ",fechaA, " hasta la fecha: ",fechaB)

                        # Fecha en formato
                        from datetime import datetime

                        fechaD = datetime.strptime(fechaA, "%d/%m/%Y")
                        fechaF = datetime.strptime(fechaB, "%d/%m/%Y")

                        print(fechaA)
                        print(fechaB)

                        totalSumaMonto1 = 0

                        for i in range (len(listadegastos["gastos"])):

                                # Fecha en formato datetime
                                fechaFormato= datetime.strptime(listadegastos["gastos"][i]["fecha"], "%d/%m/%Y")

                                if fechaD <= fechaFormato <= fechaF:
                                        sumaMonto1 = (listadegastos["gastos"][i]["monto"])
                                        print (sumaMonto1)
                                        totalSumaMonto1 = totalSumaMonto1+sumaMonto1
                        print ("Total= ",totalSumaMonto1)

                elif ( calcularTgastos == 3 ):

                        print(" Calcular total mensual")
                        print ( " Ingrese fecha inicio y fin del mes que quiere filtrar\n")
                        print ( " Fecha de inicio: ")
                        dia = ( int (input ("Dia= ")))
                        mes = ( int (input ("Mes= ")))
                        year = ( int (input ("Year = ")))
                        fechaA = f"{dia:02d}/{mes:02d}/{year}"
                        print ( " Fecha final: ")
                        dia = ( int (input ("Dia")))
                        mes = ( int (input ("Mes")))
                        year = ( int (input ("Year\n")))
                        fechaB = f"{dia:02d}/{mes:02d}/{year}"
                                
                        print("Para la semana del: ",fechaA, " hasta la fecha: ",fechaB)

                        # Fecha en formato
                        from datetime import datetime

                        fechaD = datetime.strptime(fechaA, "%d/%m/%Y")
                        fechaF = datetime.strptime(fechaB, "%d/%m/%Y")

                        print(fechaA)
                        print(fechaB)

                        totalSumaMonto1 = 0

                        for i in range (len(listadegastos["gastos"])):

                                # Fecha en formato datetime
                                fechaFormato= datetime.strptime(listadegastos["gastos"][i]["fecha"], "%d/%m/%Y")
                                        

                                if fechaD <= fechaFormato <= fechaF:
                                        sumaMonto1 = (listadegastos["gastos"][i]["monto"])
                                        print (sumaMonto1)
                                        totalSumaMonto1 = totalSumaMonto1+sumaMonto1

                                        
                        print ("Total= ",totalSumaMonto1)
                elif ( calcularTgastos == 4 ):
                        print("")

        elif ( menuPrincipal == 4 ):

                from todasFunciones.todosMenus import menuGenerarReportes
                menuGenerarReportes()

                reporteGastos = ( int (input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
                if ( reporteGastos == 1 ):

                        print(" Reporte de gastos diarios")
                        print ( "Ingrese fecha del dia que quiere calcular\n")
                        dia = ( int (input ("Dia= ")))
                        mes = ( int (input ("Mes= ")))
                        year = ( int (input ("Year= ")))
                        fechaE = f"{dia:02d}/{mes:02d}/{year}"

                        print("Para el dia: ",fechaE)
                        totalSumaMonto = 0
                        totalsumCat = 0

                        opcionCategorias = [gasto["categoria"] for gasto in listadegastos["gastos"]]
                        #Set se usa para quiter los duplicados
                        opcionCategorias = list(set(opcionCategorias))
                        for j in range (len(opcionCategorias)):
                                for i in range (len(listadegastos["gastos"])):
                                        if (opcionCategorias[j]== listadegastos["gastos"][i]["categoria"]) & (fechaE == listadegastos["gastos"][i]["fecha"]):
                                                print (listadegastos["gastos"][i])
                                                sumaMonto = (listadegastos["gastos"][i]["monto"])
                                                totalsumCat = totalsumCat + sumaMonto
                                                totalSumaMonto = totalSumaMonto+sumaMonto
                                if totalsumCat != 0:
                                        print ("El total de la categoria ",opcionCategorias[j]," es de: ",totalsumCat)
                                totalsumCat = 0
                        print ("Total= ",totalSumaMonto)



                elif ( reporteGastos == 2 ):
                        print(" Reporte semanal")

                        print(" Calcular total mensual")
                        print ( " Ingrese fecha inicio y fin del mes que quiere filtrar\n")
                        print ( " Fecha de inicio: ")
                        dia = ( int (input ("Dia= ")))
                        mes = ( int (input ("Mes= ")))
                        year = ( int (input ("Year = ")))
                        fechaA = f"{dia:02d}/{mes:02d}/{year}"
                        print ( " Fecha final: ")
                        dia = ( int (input ("Dia")))
                        mes = ( int (input ("Mes")))
                        year = ( int (input ("Year\n")))
                        fechaB = f"{dia:02d}/{mes:02d}/{year}"
                                
                        print("Para la semana del: ",fechaA, " hasta la fecha: ",fechaB)

                        # Fecha en formato
                        from datetime import datetime

                        fechaA = datetime.strptime(fechaA, "%d/%m/%Y")
                        fechaB = datetime.strptime(fechaB, "%d/%m/%Y")

                        print(fechaA)
                        print(fechaB)
                        totalsumCat = 0
                        totalSumaMonto = 0
                        opcionCategorias = [gasto["categoria"] for gasto in listadegastos["gastos"]]
                        #Set se usa para quiter los duplicados
                        opcionCategorias = list(set(opcionCategorias))
                        for j in range (len(opcionCategorias)):
                                for i in range (len(listadegastos["gastos"])):
                                        fechaFormatoDT= datetime.strptime(listadegastos["gastos"][i]["fecha"], "%d/%m/%Y")

                                        if (opcionCategorias[j]== listadegastos["gastos"][i]["categoria"]) & (fechaA <= fechaFormatoDT <= fechaB):
                                                print (listadegastos["gastos"][i])
                                                sumaMonto = (listadegastos["gastos"][i]["monto"])
                                                totalsumCat = totalsumCat + sumaMonto
                                                totalSumaMonto = totalSumaMonto+sumaMonto
                                if totalsumCat != 0:
                                        print ("El total de la categoria ",opcionCategorias[j]," es de: ",totalsumCat)
                                totalsumCat = 0

                        print ("Total= ",totalSumaMonto)

                elif ( reporteGastos == 3 ):
                        print(" Reporte mensual")
                        print(" Calcular total mensual")
                        print ( " Ingrese fecha inicio y fin del mes que quiere filtrar\n")
                        print ( " Fecha de inicio: ")
                        dia = ( int (input ("Dia= ")))
                        mes = ( int (input ("Mes= ")))
                        year = ( int (input ("Year = ")))
                        fechaA = f"{dia:02d}/{mes:02d}/{year}"
                        print ( " Fecha final: ")
                        dia = ( int (input ("Dia")))
                        mes = ( int (input ("Mes")))
                        year = ( int (input ("Year\n")))
                        fechaB = f"{dia:02d}/{mes:02d}/{year}"
                                
                        print("Para la semana del: ",fechaA, " hasta la fecha: ",fechaB)

                        # Fecha en formato
                        from datetime import datetime

                        fechaA = datetime.strptime(fechaA, "%d/%m/%Y")
                        fechaB = datetime.strptime(fechaB, "%d/%m/%Y")

                        print(fechaA)
                        print(fechaB)
                        totalsumCat = 0
                        totalSumaMonto = 0
                        opcionCategorias = [gasto["categoria"] for gasto in listadegastos["gastos"]]
                        #Set se usa para quiter los duplicados
                        opcionCategorias = list(set(opcionCategorias))
                        for j in range (len(opcionCategorias)):
                                for i in range (len(listadegastos["gastos"])):
                                        fechaFormatoDT= datetime.strptime(listadegastos["gastos"][i]["fecha"], "%d/%m/%Y")

                                        if (opcionCategorias[j]== listadegastos["gastos"][i]["categoria"]) & (fechaA <= fechaFormatoDT <= fechaB):
                                                print (listadegastos["gastos"][i])
                                                sumaMonto = (listadegastos["gastos"][i]["monto"])
                                                totalsumCat = totalsumCat + sumaMonto
                                                totalSumaMonto = totalSumaMonto+sumaMonto
                                if totalsumCat != 0:
                                        print ("El total de la categoria ",opcionCategorias[j]," es de: ",totalsumCat)
                                totalsumCat = 0

                        print ("Total= ",totalSumaMonto)
                elif ( reporteGastos == 4 ):
                        print("")
                

        elif ( menuPrincipal == 5 ):
                print ( '''
====================================================
¿Desea salir del programa? (S/N):               
==================================================== ''' )
                salirP = ( (input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
                if ( salirP == "s" ):
                        booleano = False
                elif ( salirP == "n" ):
                        print("")
# Desarrollado por: Maria Alejandra Gomez Archila - cc.1005234916