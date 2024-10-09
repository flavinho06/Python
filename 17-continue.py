# Ferramenta Continue
# A ferramenta continue no Python vai interromper o looping
# mas vai dar continuidade a ele.

contador = 0

while contador <= 40:
    contador += 1

    # Verifica se o valor de 'contador' é múltiplo de 4
    if (contador % 4 ==0):
        print("pim") # Se for mútiplo de 4, imprime "pim"
        continue # Interrompe a interação atual e volta para o início do loop

    # Se o número não for múltiplo de 4, imprime o valor do contador
    print(contador)
# Após o término do loop, imrpime a mensagem de finalização
print("Fim do programa")
    