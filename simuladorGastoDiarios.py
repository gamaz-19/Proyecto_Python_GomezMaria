#########################################
#########################################
####### Simulador de Gasto Diario #######
#########################################
#########################################

''' 






'''
import json
from todasFunciones.funciones import*
json.dumps([])  
dicFinal = []
print(dicFinal)


listadegastos = []
listadegastos = abrirJSON()

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

booleano = True
while booleano :
    menuPrincipal = ( int ( input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
    if ( menuPrincipal == 1 ):
        print ( '''
=============================================
        Registrar Nuevo Gasto                
============================================= 
Ingrese la información del gasto: 
                         
Monto del gasto                            
Categoria  (ej. comida, transporte, entretenimiento, otros): 
Descripción (opcional):                 
        
Ingrese 'S' para guardar o 'C' para cancelar. 
============================================= ''' )
        print ()

        monto = ( float ( input (" Ingrese el monto del gasto: ") ) )
        categoria = ( ( input ( " Ingrese el numero de la categoria en la que quiere guardar el gasto: ")))
        descripcion = ( ( input ( " Agregue la descripcion deseada: ")))
        
        diccionariogastos = {
             "monto" : monto,
             "categoria" : categoria,
             "descripcion" : descripcion
        }

        listadegastos["gastos"].append(diccionariogastos)
        
        guardarCancelar = input ( " Ingrese 's' para guardar 'n' para cancelar\n" )
        if (guardarCancelar == "s" ):
                guardarJSON(listadegastos)
             



    elif ( menuPrincipal == 2 ):
        print ( '''
============================================= 
                Listar Gastos                
============================================= 
Seleccione una opción para filtrar los gastos: 
               
1. Ver todos los gastos                     
2. Filtrar por categoría                    
3. Filtrar por rango de fechas               
4. Regresar al menú principal                   
============================================= ''' )

        listarGastos = ( int (input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
        if ( listarGastos == 1 ):
            print("")
        elif ( listarGastos == 2 ):
            print("")
        elif ( listarGastos == 3 ):
            print("")
        elif ( listarGastos == 4 ):
            print("")



        
    elif ( menuPrincipal == 3 ):
        print ( '''
        ============================================= " )
                  Calcular Total de Gastos            " )
        ============================================= " )
        Seleccione el periodo de cálculo:          \n " )
        1. Calcular total diario                      " )
        2. Calcular total semanal                     " )
        3. Calcular total mensual                     " )
        4. Regresar al menú principal                 " )  
        ============================================= ''' )

        calcularTgastos = ( int (input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
        if ( calcularTgastos == 1 ):
            print("")
        elif ( calcularTgastos == 2 ):
                print("")
        elif ( calcularTgastos == 3 ):
                print("")
        elif ( calcularTgastos == 4 ):
                print("")

    elif ( menuPrincipal == 4 ):
        print ( '''
        =============================================
                   Generar Reporte de Gastos          
        ============================================= 
        Seleccione el periodo de cálculo:          
        1. Reporte diario                             
        2. Reporte semanal                           
        3. Reporte mensual                            
        4. Regresar al menú principal                 
        ============================================= ''' )

        reporteGastos = ( int (input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
        if ( reporteGastos == 1 ):
                print("")
        elif ( reporteGastos == 2 ):
                print("")
        elif ( reporteGastos == 3 ):
                print("")
        elif ( reporteGastos == 4 ):
                print("")
                

    elif ( menuPrincipal == 5 ):
        print ( '''
        =============================================
        ¿Desea salir del programa? (S/N):               
        ============================================= ''' )
        salirP = ( (input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
        if ( salirP == "s" ):
            print(" ")
        elif ( salirP == "n" ):
            print("")



