print('----- CALCULADORA INTELIGENTE -----')
print('=-=' * 13)
valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
# operacao = 0
while operacao != 6:

    print('''     [ 1 ] Somar  
     [ 2 ] Subtrair  
     [ 3 ] Multiplicar  
     [ 4 ] Dividir  
     [ 5 ] Escolha outros valores  
     [ 6 ] Sair do programa  ''')

    operacao = int(input('Escolha a operação desejada: '))
    if operacao == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é = {soma}')
    elif operacao == 2:
        subtracao = valor1 - valor2
        print(f'A diferença entra {valor1} e {valor2} é = {subtracao}')
    elif operacao == 3:
        multiplicacao = valor1 * valor2
        print(f'O resultado de {valor1} X {valor2} é = {multiplicacao:.2f}')
    elif operacao == 4:
        divisao = valor1 / valor2
        print(f'O resultado de {valor1} % {valor2} é = {divisao:.2f}')
    elif operacao == 5:
        valor1 = float(input('Digite um valor: '))
        valor2 = float(input('Digite outro valor: '))
    elif operacao == 6:
        print('Finalizando....')
    else:
        print('Opção inválida, tente novamente')
    print('=-=' * 13)
print('Fim do programa, volte sempre!')