#Declaração de variáveis 
opcao = 0
resultado = 0

#Início do código 
while (opcao != 6):
    print("CALCULADORA DAS OPERAÇÕES BÁSICAS:")
    print("Menu de escolha:\n")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão\n")
    print("5. Resto da Divisão")
    print("6. Sair")
    print("Digite a sua opção: ")
    int(input(opcao))

    if (opcao == 1):
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 + n2
        print(f"A soma = {resultado}")

    elif  (opcao == 2):
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 - n2
        print(f"A subtração = {resultado}")

    elif (opcao == 3):
        ...

    elif (opcao == 6): 
        print("Finalizando o código!")

    else:
        print("Opção inválida. Tente novamente.")