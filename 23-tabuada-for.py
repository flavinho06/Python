# Solicitar um número ao usuário
n = int(input("Informe um número para ver sua tabuada: "))
print(f"Tabuada do {n}:")

# Usar um contador para a tabuada
contador = 1
while contador <= 10:  # tabuada do 1 ao 10
    resultado = n * contador
    print(f"{n} x {contador} = {resultado}")
    contador += 1  # Incrementa o contador