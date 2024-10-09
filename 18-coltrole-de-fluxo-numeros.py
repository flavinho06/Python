contador = 0

while contador < 100:
    contador +=1

    if(contador == 6):
        print("Não quero  mostrar o 6")
        continue 

    if (contador>=10 and contador <= 38):
        print(f"Não quero mostrar o {contador}")
        continue 

    print(contador)

    if contador == 40: 
        break   
print("Acabou!")
        