import os #importa la libreria necesaria para hacer 'clean' en  cmd

numero_datos=0      #variable para guardar el numero de datos que ingresara
numero_variable=0   #variable para el numero de variables 'x' que usara 
datos=[]    #para hacer la matriz de ecuaciones y aplicar Gauss
y=[]    #lista para guardar datos en Yn
suma_y=0    #variable para hacer la suma de Rienan de datos de y
x=[]    #para hacer matriz de datos de nX
suma_x=[]   #lista para sumas de nX despues
suma_xy=[]   #lista para sumatoria de Xn*Y despues
suma_xx=[]   #lista paara sumatoria de Xn*Xn despues
resultado=[]    #lista para guardar los resultados de la matriz  
vari=[] #lista para variables que se usara en una estimacion de f(x)
fx=0    #variable para guardar la f(x) resultante
pregunta="y"    #variable para condicones de while y if ultimo 

while pregunta=="y" :   #ciclo para todo el proceso
    os.system('cls ')
    print("Este programa hace el metodo de regresion multiple\n\n")
    numero_variable=(int(input("Ingresa el numero de variables X: ")))
    numero_datos=(int(input("\nIngresa el numero de Datos: ")))

    #ciclo para pedir datos de y & hacer sumatoria de y
    os.system('cls')
    for i in range(numero_datos):
        y.append(float(input("Ingresa valor para Y, Valor "+str(i+1)+" : ")))
        suma_y = suma_y + y[i]

    #ciclo para pedir x & hacer sumatoria  de todas las x y multiplicacion de x con y 
    for i in range(numero_variable):
        os.system('cls')
        x.append([])
        suma_x.append(0)
        suma_xy.append(0)
        for j in range(numero_datos):
            x[i].append(float(input("Ingresa valor para X "+str(i+1)+". Valor "+str(j+1)+" : ")))
            suma_x[i] += x[i][j]    
            suma_xy[i] += x[i][j] * y[j]

    #multiplica las x entre si mismas   
    os.system('cls')
    cen=0
    for i in range(numero_variable):
        for j in range(numero_variable):
            suma_xx.append(0)
            for k in range(numero_datos):
                suma_xx[cen] += x[i][k] * x[j][k]
            cen+=1

    #ordena todos lod datos para hacer la matriz correcta
    cen=0
    for i in range(numero_variable+1):        
        datos.append([])
        if i==0:
            for j in range(numero_variable+2): 
                if j==0:
                    datos[i].append(numero_datos)
                elif j==numero_variable+1:
                    datos[i].append(suma_y)              
                else:
                    datos[i].append(suma_x[j-1])
        else:
            for j in range(numero_variable+2):
                if j==0:
                    datos[i].append(suma_x[i-1])
                elif j==numero_variable+1:
                    datos[i].append(suma_xy[i-1])
                else:
                    datos[i].append(suma_xx[cen])
                    cen+=1

    #con la matriz ya hecha, ahora se aplica el metodo de Gauss
    divisor=0
    multiplicador=0
    cen=0
    for i in range(numero_variable+1):
        divisor=datos[i][i]
        for j in range(numero_variable+2):
            datos[i][j] /=divisor  
        for k in range(numero_variable+1):
            if k==i:
                hola=0  
            else:
                multiplicador=datos[k][cen]
                for l in range(numero_variable + 2):
                    datos[k][l] -=(datos[i][l]*multiplicador)           
        cen+=1
        
    print("Resultados de a, b1, b2, b3, bn")
    for i in range(numero_variable+1):
        print(datos[i][numero_variable+1])

    pausa=input()
    os.system('cls')

    #para estimar algun F(x)
    pregunta=input("Desea estimar algun F(x)\nY=si; N=no\n")
    if pregunta =='y':
        for i in range(numero_variable+1):
            resultado.append(datos[i][numero_variable+1])
        for i in range(numero_variable):
            vari.append(float(input("Ingresa el valor de X"+str(i+1)+" : ")))
        for i in range(numero_variable+1):
            if i==0:
                fx +=resultado[i]
            else:
                fx +=(resultado[i]* vari[i-1])
        print("el resultado de F(x) es: "+str(fx))
        pausa=input()
        os.system('cls')
        pregunta=input("Desea hacer otra regresion lineal multiple?\nY=si; N=no\n")
    else:
        pregunta=input("Desea hacer otra regresion lineal multiple?\nY=si; N=no\n")

