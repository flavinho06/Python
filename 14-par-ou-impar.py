def par(x):
    x % 2 == 0
    

def par_ou_impar(x):
    if par(x):
        return "Par"
    else:
        return "Impar"


print(par_ou_impar(8))



valor = 0
while valor != 'S':
        valor = input("Digite um valor ou 'S' para sair: ")
        if valor != 'S':
            print(par_ou_impar(int(valor)))
        else:
            print("Fim do programa")