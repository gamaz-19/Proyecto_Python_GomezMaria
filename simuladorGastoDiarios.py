#########################################
#########################################
####### Simulador de Gasto Diario #######
#########################################
#########################################

''' 






'''
from tabulate import tabulate

import json
from todasFunciones.funciones import*
json.dumps([])  
dicFinal = []

listadegastos = []
listadegastos = abrirJSON()


# convertir fechas a datetime
from datetime import datetime

booleano = True
while booleano :
    
    print ( '''

=============================================
         Simulador de Gasto Diario           
============================================= 
Seleccione una opción:   
                     
1. Registrar nuevo gasto                      
2. Listar gastos                              
3. Calcular total de gastos                   
4. Generar reporte de gastos               
5. Salir                                      
============================================= ''' )



    menuPrincipal = ( int ( input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
    if ( menuPrincipal == 1 ):
        print ( '''
====================================================
        Registrar Nuevo Gasto                
==================================================== 
Ingrese la información del gasto: 
                         
Monto del gasto                            
Categoria  (ej. comida, transporte, entretenimiento, otros)
Descripción (opcional)
Fecha
==================================================== ''' )
        print ()
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
             
    elif ( menuPrincipal == 2 ):
        print ( '''
==================================================== 
                Listar Gastos                
==================================================== 
Seleccione una opción para filtrar los gastos: 
               
1. Ver todos los gastos                     
2. Filtrar por categoría                    
3. Filtrar por rango de fechas               
4. Regresar al menú principal                   
====================================================''' )
        opcionGastos = ( int (input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))

        if ( opcionGastos == 1 ):
            print("\nTodos los gastos: ")
            for i in range (len(listadegastos)):
                print(tabulate(listadegastos))

        elif ( opcionGastos == 2 ):
                opcionCategorias = [gasto["categoria"] for gasto in listadegastos["gastos"]]
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
        print ( '''
==================================================== 
          Calcular Total de Gastos            
==================================================== 
Seleccione el periodo de cálculo:          
1. Calcular total diario                     
2. Calcular total semanal                    
3. Calcular total mensual                    
4. Regresar al menú principal               
==================================================== 

''' )

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
        elif ( calcularTgastos == 3 ):
                print(" Calcular total mensual")
        elif ( calcularTgastos == 4 ):
                print("")

    elif ( menuPrincipal == 4 ):
        print ( '''
====================================================
           Generar Reporte de Gastos          
==================================================== 
Seleccione el periodo de cálculo:          
1. Reporte diario                             
2. Reporte semanal                           
3. Reporte mensual                            
4. Regresar al menú principal                 
==================================================== ''' )

        reporteGastos = ( int (input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
        if ( reporteGastos == 1 ):
                print(" Reporte diario")
        elif ( reporteGastos == 2 ):
                print(" Reporte semanal")
        elif ( reporteGastos == 3 ):
                print(" Reporte mensual")
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



