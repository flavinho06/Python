# Lista de números inteiros
numeros = []
for i in range(5):
    num = int(input("Digite o número {}: ".format(i+1)))
    numeros.append(num)

# Encontrar o maior, menor e calcular a soma
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

# Imprimir os resultados
print("Maior número: ", maior)
print("Menor número: ", menor)
print("Soma dos números: ", soma)
