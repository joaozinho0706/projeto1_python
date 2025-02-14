print('fast food\n')

print('1. cadastrar restaurante')
print('2. listar restaurante')
print('3. ativar restaurante')
print('4. sair')

opcao_escolhida =int(input('Escolha uma opção: '))
print(f'Voce escolheu a opcao {opcao_escolhida}')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurante')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    print('Encerrando o programa')