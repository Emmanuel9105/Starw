def inicio():
    print(''' ===STAR WARS CÓDIGOS SECRETOS === \n
          Hace mucho tiempo, en una galaxya muy, muy lejana... La princesa\n
          Leia, Luke Skywolker, Han Solo, Chewbacca, C3PO y R2D2 viajan\n
          en una nave imperial robada en una misión secreta para infiltrarse\n
          en otra estrella de la muerte que el imperio está construyendo para\n
          destruirla''')
    tecla = input("Presiona 'Enter' para continuar...")
    nivel1()






from random import randint, random, uniform
def sumatorio():
    S1 = randint(1,10)
    S2 = randint(20,30)                   # Realiza el sumatorio aleatorio
    numeros = range (S1, S2)
    suma = sum(numeros)
    print(suma)
    



def nivel1():
    print('''Los problemas empiezan cuando deben realizar un salto\n
          hiperespacial hasta al sistema S1 en el sector S2, pero el sistema de\n
          navegación está estropeado y el computador tiene problemas para\n
          calcular parte de las coordenadas de salto. Chewbacca, piloto\n
          experto, se da cuenta que falta el cuarto número de la serie.\n
          Recuerda de sus tiempos en la academia de pilotos que para\n
          calcularlo hay que calcular el sumatorio entre el nº del sistema y el\n
          nº del sector (ambos inclusive).''')
    S1= randint(1,10)
    S2 = randint(20,30)
    numeros = range(S1, S2 + 1)
    suma = sum(numeros)
    print("S1 es: " + str(S1))
    print("S2 es : " + str(S2))              # Realiza el sumatorio aleatorio
    print("¿Qué debe introducir?")
    operador = int(input("Escribe tu respuesta: "))
    if operador == suma:
        print("Has acertadoo")
    else:
        print(f"Has falladoo el resultado era: {suma}")
        print("La galaxya esta perdida")
        inicio()

def nivel2():
    print('''\n
          Gracias a Chewbacca consiguen llegar al sistema correcto y ven a lo\n
          lejos la estrella de la muerte. Como van en una nave imperial robada\n
          se aproximan lentamente con la intención de pasar desapercibidos.\n
          De repente suena el comunicador. “Aquí agente de espaciopuerto\n
          P1 contactando con nave imperial P2. No están destinados en este\n
          sector. ¿Qué hacen aquí?”. Han Solo coge el comunicador e\n
          improvisa. “Eh… tenemos un fallo en el… eh… condensador de\n
          fluzo... Solicitamos permiso para atracar y reparar la nave”. El\n
          agente, que no se anda con tonterías, responde “Proporcione código\n
          de acceso o abriremos fuego”. Han Solo ojea rápidamente el manual\n
          del piloto que estaba en la guantera y da con la página correcta. El\n
          código es el productorio entre el nº del agente y el nº de la nave\n
          (ambos inclusive).''')
    P1= randint(1,7)
    P2 = randint(8,12)
    producto = 1 #Empezamos por 1 porque es el elemento neutro de la multiplicacion
    for num in range(P1, P2 + 1):
        producto *= num
       
    print("P1 es: " + str(P1))
    print("P2 es : " + str(P2))
    print("¿Qué debe introducir?")
    operador = int(input("Escribe tu respuesta: "))
    

    if operador == producto:
        print("Has acertadoo")
        print("Acceso concedido.")
        nivel3()
    else:
        print("Acceso denegado")
        print("La galaxya esta perdida.")
        inicio()
    
def nivel3():
    
         
# inicio()



