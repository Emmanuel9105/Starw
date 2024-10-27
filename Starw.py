def inicio():
    print(''' ===STAR WARS CÓDIGOS SECRETOS === \n
          Hace mucho tiempo, en una galaxya muy, muy lejana... La princesa\n
          Leia, Luke Skywolker, Han Solo, Chewbacca, C3PO y R2D2 viajan\n
          en una nave imperial robada en una misión secreta para infiltrarse\n
          en otra estrella de la muerte que el imperio está construyendo para\n
          destruirla''')
    input("Presiona 'Enter' para continuar...")
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
    elif operador != suma:
        print("Has falladoo el resultado era: " + suma)


         
         
inicio()

inicio()
