nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade utilizando um número inteiro: "))
print('\n')

if idade>=12:
    print(f'{nome}: Entrada permitida.')
else:
    print(f'{nome}: Entrada NÃO permitida.')