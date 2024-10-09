# Ferramenta Break
# É uma ferramneta para interromper e encerrar um loop.
# Isso quer dizer que vamos parar o loop naquele momento e vamossair dele.
# Execute o código abaixo e explique o que ele fez

while True: 
    nome = input('Digite o seu nome ou escreva "sair": ')

    if nome == 'sair':
        break  # para a execução do while, sai do loop de repetição

    print(f'Seu nome é {nome}')

    print('Acabou')
    