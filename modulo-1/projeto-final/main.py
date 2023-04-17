import json
from init import verificar_arquivos
from funcs import sair
from user import menu_usuario
from admin import menu_admin

############## MENU PRINCIPAL ##############

def menu_principal():
    fluxos_principal = {
        '1': login_usuario,
        '2': login_admin,
        '3': cadastro_usuario,
        '4': sair
    }
    while True:
        resposta = input('''Selecione uma das opções: \n\n1- Logar como usuário \n2- Logar como administrador \n3- Cadastrar-se \n4- Sair\n\n''')
        if resposta in fluxos_principal:
            break
        else:
            print('\nValor inválido!')

    return fluxos_principal[resposta]()
    
def login_admin():
    login(True)

def login_usuario():
    login(False)

def login(administrador=False):
    print('\n## Tela de Login ##')
    usuario = input('Digite seu usuario: ')
    senha = input('Digite sua senha: ')
    with open('db/usuarios.json', 'r') as file:
        usuarios_cadastrados = json.load(file)

    autenticado = list(filter(lambda login: login['usuario'] == usuario and login['senha'] == senha and login['admin'] == administrador, usuarios_cadastrados))
    
    if autenticado and administrador:
        print('\nLogin de admin autenticado com sucesso!')
        menu_admin()
    elif autenticado and not administrador:
        print('\nLogin de usuário autenticado com sucesso!')
        menu_usuario()
    else:
        print('\nUsuario e/ou senha não encontrados!')
        menu_principal()

def cadastro_usuario():
    print('\n## Tela de Cadastro ##')
    while True:
        usuario = input('Digite seu usuario ou enter para sair: ')
        senha = input('Digite sua senha ou enter para sair: ')
        if len(usuario) > 2 and len(senha) > 2:
            break
        elif usuario == '' or senha == '':
            return menu_principal()
        else:
            print('Seu usuário e/ou senha são muito curtos!')
        
    with open('db/usuarios.json', 'r') as file:
        usuarios_cadastrados = json.load(file)

    usuario_existente = list(filter(lambda login: login['usuario'] == usuario, usuarios_cadastrados))

    if usuario_existente:
        print('Usuário já cadastrado! Utilize outro login.')
    else:
        usuarios_cadastrados.append({'usuario': usuario, 'senha': senha, 'admin': False})
        with open('db/usuarios.json', 'w') as file:
            json.dump(usuarios_cadastrados, file, indent=4)
        print('\nUsuário cadastrado com sucesso!\n')
    menu_principal()

############## FIM MENU PRINCIPAL ##############

if __name__ == '__main__':
    verificar_arquivos(['db/albuns.json', 'db/artistas.json', 'db/playlists.json', 'db/usuarios.json'])
    menu_principal()

