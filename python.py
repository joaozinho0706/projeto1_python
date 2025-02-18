import os

def exiber_nome_do_programa():
    print('fast food\n')

def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. ativar restaurante')
    print('4. sair \n')

opcao_escolhida =int(input('Escolha uma opção: '))
print(f'Voce escolheu a opcao {opcao_escolhida}')

def finalizar_app():
    os.system('cls')
    print('finalizar o app')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurante')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    finalizar_app()

def main():
    exiber_nome_do_programa()
    exibir_opcoes

if __name__ == '__main__':