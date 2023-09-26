genero = input("Digite H se for homem ou digite M se for mulher:\n")

if genero =='H':
    altura = float(input('Digite sua altura:\n'))
    peso_ideal = (altura * 72.7) - 58
    print("Seu peso ideal é" + str(peso_ideal))
elif genero =='M':
    altura = float(input('Digite sua altura:\n'))
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é" + str(peso_ideal))
else:
    print('Resposta inválida')
   