peso = float(input('Digite o peso dos peixes em kg: \n'))
if peso > 50:
    excesso = peso - 50
    print('Há '+ str(excesso)+'kg em excesso de acordo com o regulamento de pesca do estado de São Paulo.\n')
    multa = excesso * 4
    print('Você será multado em '+ str(multa)+ " reais por descumprir o regulamento de pesca de São Paulo.\n")
else:
    print('\nPeso adequado com as normas.')