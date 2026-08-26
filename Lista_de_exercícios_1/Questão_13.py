#Pedido de número inteiro positivo para o usuário.
numero = int(input('Digite um número inteiro: '))

for i in range(1,11):  #Repete o código para os números de 1 até 10.
    print(f'{numero} x', i, '=', numero*i)   #Mostra a multiplicação e o resultado.