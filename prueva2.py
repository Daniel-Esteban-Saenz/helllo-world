import random
resultado: int
def suma_dos_valores(sumando1, sumando2):
    global resultado
    resultado = sumando1 + sumando2
    return resultado

#suma_dos_valores(4,5)
#print("primera suma")
#print(resultado)
#suma_dos_valores(1,2)
#print("segunda suma")
#print(resultado)
def calculadora_dos_valores(numero1, numero2, operador):
            global resultado
            if operador == 1: #si el operador es 1 es suma
                resultado = numero1 + numero2
                return resultado
            elif operador == 2: #si el operador es 2 es resta
                resultado = numero1 - numero2
                return resultado
            elif operador == 3: #si el operador es 3 es multiplicación
                resultado = numero1 * numero2
                return resultado
            elif operador == 4: #si el operador es 4 es division
                resultado = numero1 / numero2
            return resultado
        
#calculadora_dos_valores(1,2,1)
#print("suma :",resultado)
#calculadora_dos_valores(1,2,2)
#print("resta :",resultado)
#calculadora_dos_valores(1,2,3)
#print("multiplicación :",resultado)
#calculadora_dos_valores(1,2,4)
#print("division :",resultado)

def calculadora_Terminal(a,b):
    global c
    c = (a**2 + b**2)**0.5
    return c
#calculadora_Terminal(2,1)
#print("el resultado es :", c)

def despeje():
    global x
    b=int(input("ingrese el valor de B= "))
    c=int(input("ingrese el valor de c= "))
    x = (c-b)/2
    print("el valor de x es: ",x)
    return x

#despeje()

def funcion_and():
    global x
    a=bool(input("ingrese el valor de a true= cualquier numero false= presione enter."))
    b=bool(input("ingrese el valor de b true= cualquier numero false= presione enter. "))
    c=bool(input("ingrese el valor de c true= cualquier numero false= presione enter. "))
    x= a and b and c
    print("el resultado es: ", x)
    return x

#funcion_and()

def pitagoras_funcion_sumar():
    global resul_pitagoras
    a=int(input("ingresar el valor de a: "))
    b=int(input("ingresar el valor de b: "))
    a2= a**2
    b2= b**2
    suma= suma_dos_valores(a2,b2)
    resul_pitagoras = suma**0.5
    print("el valor de pitagoras es: ",resul_pitagoras)
    return resul_pitagoras

#pitagoras_funcion_sumar()

def separador_contador():
    global resultado_contador
    palabra= str(input("ingrese la palabra: "))
    letra= str(input("ingrese la letra a contar: "))
    resultado_contador= palabra.count(letra)
    print("la cantidad de letras ",letra," es= ",resultado_contador)
    print("la cantidad de letras de la palabra es: ", len(palabra))
    print("palabra separada por letras= ", list(palabra))
    return resultado_contador

#separador_contador()


def piedra_papel_tijera():
    global opciones
    opciones = ["piedra", "papel", "tijera"]
    jugador1 = random.choice(opciones)
    jugador2 = random.choice(opciones)
    if jugador1 == jugador2:
        resultado = "empate"
    elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
        resultado = "gana jugador 1"
    else:
        resultado = "gana jugador 2"
    print ("el jugador1: ",jugador1)
    print ("el jugador2: ",jugador2)
    print ("el resultado es: ", resultado)
    return resultado

piedra_papel_tijera()