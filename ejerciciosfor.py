
import time
def ejercicio():
    palabra= str(input("por favor ingrese la palabra: "))
    cantidad= int(input("por favor ingrese la cantidad de veces: "))
    for i in range(cantidad):
        print("valor de la variable i: ", i+1)
        time.sleep(2)
        print(palabra)
    return

#ejercicio()

def ejercicio_edad():
    edad= int(input("por favor ingrese la edad:"))
    for i in range(edad):
        print(i+1)
        time.sleep(2)
    return
    
#ejercicio_edad()

def calcular_edad():
    año_actual=  int(2024)
    fecha_nacimiento= int(input("por favor ingrese su fecha de nacimiento: "))
    edad= año_actual - fecha_nacimiento
    for i in range(edad):
        print(i+1)
        time.sleep(1)
    print("su edad es: ",edad)
    return

#calcular_edad()

def numero_impar():
    numero= int(input("por favor ingrese el numero: "))
    for i in range(1,numero+1,2):
        time.sleep(1)
        print(i, end=",\n")
        if i==15:
            break;

#numero_impar()

def relog_stop():
    numero_parar= int(input("ingrese el segundo en que desea parar: "))
    for i in range(60,0,-1):
        time.sleep(1)
        print("segundo:",i, end="\n")
        if i==numero_parar:
            print("\33[31m"+"tiempo maximo: ",i, " segundos"+"\33[0m")
            break;

#relog_stop()

def interes_compuesto():
    cantidad_invertida= float(input("ingrese la cantidad a invertir: "))
    interes_inversion= float(input("ingrese el interes de la inversion: "))
    años_inversion= int(input("ingrese la cantidad de años de inversion: "))
    dinero_ganado=cantidad_invertida
    for i in range(1,años_inversion+1):
        inversion= dinero_ganado*(interes_inversion/100)
        time.sleep(1)
        inversion_año= dinero_ganado+inversion
        dinero_ganado= inversion_año
        print(inversion)
        print(inversion_año)
        print(dinero_ganado)
        print("Dinero ganado al año es: ",dinero_ganado)
        
interes_compuesto()