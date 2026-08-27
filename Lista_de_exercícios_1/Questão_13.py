#Pedido de número inteiro para o usuário.
numero = int(input('Digite um número inteiro: '))

print(f'\n-TABUADA DO {numero}-') #Mostra o título e pula uma linha (estética)

for i in range(1, 11):  #Repete o código para os números de 1 até 10.
    print(f'{numero} x', i, '=', numero*i)   #Mostra a multiplicação e o resultado.