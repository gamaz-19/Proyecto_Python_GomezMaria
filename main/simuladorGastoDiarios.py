#########################################
####### Simulador de Gasto Diario #######
#########################################










print ( " ============================================= " )
print ( "          Simulador de Gasto Diario            " )
print ( " ============================================= " )
print ( " Seleccione una opción:   \n                   " )
print ( " 1. Registrar nuevo gasto                      " )
print ( " 2. Listar gastos                              " )
print ( " 3. Calcular total de gastos                   " )
print ( " 4. Generar reporte de gastos                  " )
print ( " 5. Salir                                      " )
print ( " ============================================= " )

booleanito = True
while booleanito :
    menuPrincipal = ( int ( input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
    if ( menuPrincipal == 1 ):
        print ( " ============================================= " )
        print ( "          Registrar Nuevo Gasto                " )
        print ( " ============================================= " )
        print ( " Ingrese la información del gasto:   \n        " )
        print ( " 1. Monto del gasto                            " )
        print ( " 2. Categoria  (ej. comida, transporte, entretenimiento, otros): " )
        print ( " 3. Descripción (opcional):   \n               " )
        print ( " Ingrese 'S' para guardar o 'C' para cancelar. " )
        print ( " ============================================= " )
        

    elif ( menuPrincipal == 2 ):
        print ( " ============================================= " )
        print ( "                 Listar Gastos                 " )
        print ( " ============================================= " )
        print ( " Seleccione una opción para filtrar los gastos: \n " )
        print ( " 1. Ver todos los gastos                       " )
        print ( " 2. Filtrar por categoría                      " )
        print ( " 3. Filtrar por rango de fechas                " )
        print ( " 4. Regresar al menú principal                 " )  
        print ( " ============================================= " )

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
        print ( " ============================================= " )
        print ( "           Calcular Total de Gastos            " )
        print ( " ============================================= " )
        print ( " Seleccione el periodo de cálculo:          \n " )
        print ( " 1. Calcular total diario                      " )
        print ( " 2. Calcular total semanal                     " )
        print ( " 3. Calcular total mensual                     " )
        print ( " 4. Regresar al menú principal                 " )  
        print ( " ============================================= " )
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
        print ( " ============================================= " )
        print ( "            Generar Reporte de Gastos          " )
        print ( " ============================================= " )
        print ( " Seleccione el periodo de cálculo:          \n " )
        print ( " 1. Reporte diario                             " )
        print ( " 2. Reporte semanal                            " )
        print ( " 3. Reporte mensual                            " )
        print ( " 4. Regresar al menú principal                 " )  
        print ( " ============================================= " )
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
        print ( " ============================================= " )
        print ( "¿Desea salir del programa? (S/N):              " )  
        print ( " ============================================= " )
        salirP = ( (input ( " Ingrese el numero de la opcion que quiere seleccionar: ")))
        if ( salirP == "s" ):
            print(" ")
        elif ( salirP == "n" ):
            print("")



