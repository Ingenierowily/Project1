from random import randint as azar
ganador = azar(1,11)

#Programa para rifas
contador = 0
num = int(input('Adivina que numero es el ganador del 1 al 10:  '))
i = 0
while i == 0:
     if num > ganador:
        print('El numero indicado es muy alto')
        contador = contador + 1
        num = int(input('Intentalo nuvamente: '))
     elif num < ganador:
        print('El numero indicado es muy bajo')
        contador = contador + 1
        num = int(input('Intentalo nuvamente: '))
     else:
        print('Has acertado al numero ganador')
        contador = contador + 1
        i = 1
    
print(f'Felicitaciones, lo adivinaste en {contador} intentos')
