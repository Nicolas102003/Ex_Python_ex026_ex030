frase = str(input('Digite uma frase:')).strip().upper()
print('a letra a aparece {} vez(es) na frase digitada'.format(frase.count('A')))
print('o primeiro A se encontra na posição:{}'.format(frase.find('A')+1))
print('o ultimo A se encontra na posição: {}'.format(frase.rfind('A')+1))
