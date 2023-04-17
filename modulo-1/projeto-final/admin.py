import funcs
import string

def menu_admin():
    fluxos_admin = {
        '1': registrar_artista,
        '2': registrar_album,
        '3': funcs.sair
        }
    while True:
        resposta_admin = input('''Selecione uma das opções: \n\n1- Registrar Artista \n2- Registrar Álbum \n3- Sair\n\n''')
        if resposta_admin in fluxos_admin:
            break
        else:
            print('\nValor inválido!')
    fluxos_admin[resposta_admin]()

def registrar_artista():
    print('\n## Tela de Registro de Artista ##')
    artista = string.capwords(input('Digite o nome do artista que você deseja registrar ou tecle enter para sair: '))
    if artista != '':
        artistas = funcs.carregar_artistas()
        if artista in artistas:
            print(f'{artista} já foi registrado/a!\n')
        else:
            funcs.salvar_artista(artista)
            print('Artista registrado com sucesso!\n')
    return menu_admin()

def registrar_album():
    print('\n## Tela de Registro de Álbum ##')
    artista_album = string.capwords(input('Digite o nome do artista que você deseja registrar ou tecle enter para sair: '))
    if artista_album == '':
        return menu_admin()

    artistas = funcs.carregar_artistas()
    
    if artista_album not in artistas:
        print(f'Artista não encontrado! Você deve registar {artista_album} antes de registar um álbum!\n')
        return registrar_album()
    
    while True: # Loop para nome do album
        nome_album = string.capwords(input(f'Digite o nome do álbum de {artista_album} que você deseja registrar ou tecle enter para sair: '))
        if nome_album == '':
            return menu_admin()
        
        albuns_artista = funcs.carregar_albuns(artista_album)
        
        try:
            if nome_album in albuns_artista:
                print('Esse álbum já foi registrado!')
            else:
                break
        except:
            break 
            
    while True: # Loop para nome músicas
        numero_musicas = input('Digite o número de músicas que deseja registar ou digite enter para sair: ')
        if numero_musicas == '':
            return menu_admin()
        try:
            numero_musicas = int(numero_musicas)
            break
        except:
            print('[ERRO] Você deve digitar um número!')

    musicas_album = [string.capwords(input('Digite o nome da música que deseja adicionar: ')) for _ in range(numero_musicas)]
        
    funcs.salvar_album(artista_album, nome_album, musicas_album)
    print('\nÁlbum registrado com sucesso!\n')
    return menu_admin()
    

