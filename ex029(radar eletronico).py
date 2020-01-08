vel = int(input('qual a velocidade do carro ?'))
if vel > 80:
    multa = vel-80
    print('Motorista multado...\n O valor da multa é: {}'.format(multa))
else:
    print('O motorista não excedeu o limite de velocidade')
