#Pedido de número inteiro positivo para o usuário.
numero = int(input('Digite um número inteiro positivo: '))

#Condição para que seja aceito apenas números inteiros positivos, caso contrário, aparecerá "número inválido".
if numero>0:

#Repete o código de 0 até o antecessor do número, ou seja, o código é repetido a mesma quantidade de vezes do número.
    for i in range(numero):  
        print(numero-i)

else:
    print('Número inválido!')