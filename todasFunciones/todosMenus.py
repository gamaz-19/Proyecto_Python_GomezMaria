def menuPrincipalT ():
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
    
def menuRegistroNuevo ():
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
    
def menuListarGastos ():
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
    
def menuCalcularTotalGastos ():
    print ( '''
==================================================== 
            Calcular Total de Gastos            
==================================================== 
Seleccione el periodo de cálculo:          
1. Calcular total diario                     
2. Calcular total semanal                    
3. Calcular total mensual                    
4. Regresar al menú principal               
==================================================== ''' )

def menuGenerarReportes ():
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

def menuSalirPrograma ():
    print ( '''
====================================================
¿Desea salir del programa? (S/N):               
==================================================== ''' )

