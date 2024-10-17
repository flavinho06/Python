# Inicializa a variável para armazenar a soma
soma_pares = 0
print("Calculando a soma dos números pares de 1 a 50: ")

# Usar um laço for para iterar pelos números
for num in range(2, 51, 2):  # Começa em 2 e vai até 50, pulando de 2 em 2
    soma_pares += num  # Adiciona o número par à soma

# Após o loop, imprime o resultado final
print(f"A soma dos números pares entre 1 e 50 é: {soma_pares}")
