import sys
from random import randint, random, uniform # importa randint para ser utuilizado en las funciones 
import math 
        
def nivel1():
    print('Los problemas empiezan cuando deben realizar un salto\nhiperespacial hasta al sistema S1 en el sector S2, pero el sistema de\nnavegación está estropeado y el computador tiene problemas para\ncalcular parte de las coordenadas de salto. Chewbacca, piloto\nexperto, se da cuenta que falta el cuarto número de la serie.\nRecuerda de sus tiempos en la academia de pilotos que para\ncalcularlo hay que calcular el sumatorio entre el nº del sistema y el\nnº del sector (ambos inclusive).')
    while True:

        S1= randint(1,10)
        S2 = randint(20,30)
        numeros = range(S1, S2 + 1)
        suma = sum(numeros)
        print("S1 es: " + str(S1))
        print("S2 es : " + str(S2))              # Realiza el sumatorio aleatorio
        print("¿Qué debe introducir?")
        print(suma) #nos dice la respuesta para comprobar mejor
        try:
            operador = int(input("Escribe tu respuesta: "))
            if operador == suma:
                print("Has acertadoo")
                nivel2()
                break
            else:
                perder()
                break
        except ValueError:
            print("Por favor, introduce un numero valido")


def nivel2():
    print('Gracias a Chewbacca consiguen llegar al sistema correcto y ven a lo\nlejos la estrella de la muerte. Como van en una nave imperial robada\nse aproximan lentamente con la intención de pasar desapercibidos.\nDe repente suena el comunicador. “Aquí agente de espaciopuerto\nP1 contactando con nave imperial P2. No están destinados en este\nsector. ¿Qué hacen aquí?”. Han Solo coge el comunicador e\nimprovisa. “Eh… tenemos un fallo en el… eh… condensador de\nfluzo... Solicitamos permiso para atracar y reparar la nave”. El\nagente, que no se anda con tonterías, responde “Proporcione código\nde acceso o abriremos fuego”. Han Solo ojea rápidamente el manual\ndel piloto que estaba en la guantera y da con la página correcta. El\ncódigo es el productorio entre el nº del agente y el nº de la nave\n(ambos inclusive).')
    while True:
        P1= randint(1,7)
        P2 = randint(8,12)
        producto = 1 #Empezamos por 1 porque es el elemento neutro de la multiplicacion
        for num in range(P1, P2 + 1):  #Realiza el productorio de P1 y P2
            producto *= num
        
        print("P1 es: " + str(P1))
        print("P2 es : " + str(P2))
        print("¿Qué debe introducir?")
        print(producto) #nos dice la respuesta para comprobar mejor
        try:
            operador = int(input("Escribe tu respuesta: "))
            if operador == producto:
                print("Has acertadoo")
                nivel3()
                break
            else:
                perder()
                break
        except ValueError:
            print("Por favor, introduce un numero")
    
def nivel3():
    print('Han Solo proporciona el código correcto. Atracan en la estrella de la\nmuerte, se equipan con trajes de soldados imperiales que\nencuentran en la nave para pasar desapercibidos y bajan. Ahora\ndeben averiguar en qué nivel de los N existentes se encuentra el\nreactor principal. Se dirigen al primer panel computerizado que\nencuentran y la Princesa Leia intenta acceder a los planos de la\nnave pero necesita introducir una clave de acceso. Entonces\nrecuerda la información que le proporcionó Lando Calrissian “La\nclave de acceso a los planos de la nave es el factorial de N/10\n(redondeando N hacia abajo), donde N es el nº de niveles”.')
    while True:
        N = randint(50,100)
        i = 1
        factorial = 1
        while (i <= N/10):
            factorial = factorial * i    # Realiza el factorial de N/10
            i = i + 1
        print("N es: " + str(N))
        print("¿Qué debe introducir?")
        print(factorial)   #nos dice la respuesta para comprobar mejor
        try:
            operador = int(input("Escribe tu respuesta: "))
            if operador == factorial:
                print("Has acertadoo")
                nivel4()
                break
            else:
                perder()
                break
        except ValueError:
            print("Por favor, introduce un numero")
        
  
def nivel4():
    print('Gracias a la inteligencia de Leia llegan al nivel correcto y encuentran\nla puerta acorazada que da al reactor principal. R2D2 se conecta al\npanel de acceso para intentar hackear el sistema y abrir la puerta.\nPara desencriptar la clave, necesita verificar si el número P es primo\no no. Si es primo introduce un 1, si no lo es introduce un 0')
    while True:
        P = randint(10,100)

        def es_primo(P):
            if P < 2:
                return False
            for i in range(2, int(math.sqrt(P))+1):  #Comprueba si es primo o no el numero P
                if  (P % i)== 0:
                    return False
            return True

        resultado = es_primo(P)

        print("P es: " + str(P))
        print("¿Qué debe introducir?")
        print(resultado) #nos dice la respuesta para comprobar mejor
        try:
            operador = int(input("Escribe tu respuesta: "))
            if operador == resultado:
                print("Has acertadoo")
                nivel5()
                break
            else:
                perder()
                break
        except ValueError:
            print("Por favor, introduce un numero")



def nivel5():
    print('Consiguen entrar al reactor. Ya solo queda que Luke Skywalker\ncoloque la bomba, programe el temporizador y salir de allí corriendo.\nNecesita programarlo para que explote en exactamente M minutos y\nS segundos, el tiempo suficiente para escapar antes de que explote\npero sin que el sistema de seguridad anti-explosivos detecte y\ndesactive la bomba. Pero el temporizador utiliza un reloj Zordgiano\nun tanto peculiar. Para convertir los minutos y segundos al sistema\nZordgiano hay que sumar el factorial de M y el factorial de S.')
    while True:
        M = randint(5,10)
        S = randint(5,10)
        factorial1 = math.factorial(M)
        factorial2 = math.factorial(S)    #Realiza la suma de el factorial de M y el facotiral de S
        resultado = factorial1 + factorial2
        print("M es: " + str(M))
        print("S es : " + str(S))
        print("¿Qué debe introducir?")
        print(resultado)
        try:
            operador = int(input("Escribe tu respuesta: "))
            if operador == resultado:
                print("Has acertadoo")
                ganar()
                break
            else:
                perder()
                break
        except ValueError:
            print("Por favor, introduce un numero")


def ganar():
    print('Luke Skywalker introduce el tiempo correcto, activa el temporizador\ny empiezan a sonar las alarmas. Salen de allí corriendo, no hay\ntiempo que perder. La nave se convierte en un hervidero de\nsoldados de arriba a abajo y entre el caos que les rodea consiguen\nllegar a la nave y salir de allí a toda prisa. A medida que se alejan\nobservan por la ventana la imagen de la colosal estrella de la muerte\nexplotando en el silencio del espacio, desapareciendo para siempre\njunto a los restos del malvado imperio.\n¡Has salvado la galaxia gracias a la Fuerza Jedi de las matemáticas!\nEnhorabuena ;D')
    while True:
        operador = input("Presiona 'Enter' para continuar...")
        if operador == '':                     #Pregunta si queremos volver a jugar o no
            volverj()
            break
        else:
            print("Introduce solo enter")

def perder():
    print('Ese no era el código correcto… La misión ha sido un fracaso… :( :(\n:(\nTodavía no eres un Maestro Jedi de las Matemáticas.') 
    while True:
        operador = input("Presiona enter para continuar: ")

        if operador == '':
            volverj()         #Despues de perder ejecuta volver a jugar
            break
        else:
            print("Presiona solo enter")
    


def volverj():
    print("¿Quieres volver a jugar (si / no)?")
    si = "si"
    no = "no"
    operador = str(input("Presiona enter para continuar: "))
    if operador == si:
        inicio()
    elif operador == no:              #Pregunta si quieremos volver a jugar o no
        fin()



def fin():
    print("Gracias por jugar :D")
    sys.exit()           # Se cierra el programa
   
    
def inicio():
    print('===STAR WARS CÓDIGOS SECRETOS ===\nHace mucho tiempo, en una galaxya muy, muy lejana... La princesa\nLeia, Luke Skywolker, Han Solo, Chewbacca, C3PO y R2D2 viajan\nen una nave imperial robada en una misión secreta para infiltrarse\nen otra estrella de la muerte que el imperio está construyendo para\ndestruirla')

    while True:
        operador = input("Presiona 'Enter' para continuar...")
        if operador == '':
            nivel1()
            break                   #Comprueba que solo hemos seleccionado enter
        else:
            print("Introduce solo enter")  

inicio()

        












