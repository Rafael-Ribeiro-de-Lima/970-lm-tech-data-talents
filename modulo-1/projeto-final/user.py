import funcs
import string


def menu_usuario():
    fluxos_usuario = {
        '1': buscar_playlist,
        '2': criar_playlist,
        '3': funcs.sair
        }
    while True:
        resposta_usuario = input('''Selecione uma das opções: \n\n1- Buscar Playlist \n2- Criar Playlist \n3- Sair\n\n''')
        if resposta_usuario in fluxos_usuario:
            break
        else:
            print('\nValor inválido!')
    fluxos_usuario[resposta_usuario]()

def buscar_playlist():
    fluxos_busca_playlist = {
        '1': buscar_por_musica,
        '2': buscar_por_artista,
        '3': buscar_por_nome_playlist,
        '4': menu_usuario
        }
    while True:
        resposta_busca = input('''Selecione uma das opções de busca de playlists: \n\n1- Buscar por música \n2- Buscar por artista \n3- Buscar por nome \n4- Sair\n\n''')
        if resposta_busca in fluxos_busca_playlist:
                break 
        else:
            print('\nValor inválido!')
    fluxos_busca_playlist[resposta_busca]()

def buscar_por_musica():  
    nome_musica = string.capwords(input('\nDigite o nome da música procurada ou enter para sair: '))
    if nome_musica == '':
        return menu_usuario()
    
    playlists_cadastradas = funcs.carregar_playlists()
    playlists_encontradas = []

    for playlist in playlists_cadastradas:
        try:
            for musica in playlist['conteudo']:
                if nome_musica in musica:
                    playlists_encontradas.append(playlist)
                    break
        except:
            pass
    
    if playlists_encontradas == []:
        print(f'Nenhuma playlist com a música {nome_musica} foi encontrada!\n')                 
    else:
        print(f'\nAs playlists que contém a música {nome_musica} são: \n')
        for playlist in playlists_encontradas:
            {funcs.printar_playlist(playlist)}
            print()
    print()
    return menu_usuario()

def buscar_por_artista():
    nome_artista = string.capwords(input('\nDigite o nome do artista procurado ou enter para sair: '))
    if nome_artista == '':
        return menu_usuario()
    else:
        playlists_cadastradas = funcs.carregar_playlists()
        playlists_encontradas = []

        for playlist in playlists_cadastradas:
            try:
                for musica in playlist['conteudo']:
                    if nome_artista in list(musica.values())[0]['artista']: # Tentar reescrever essa parte...
                        playlists_encontradas.append(playlist)
                        break    
            except:
                pass                   
        
        if playlists_encontradas == []:
            print(f'Nenhuma playlist com o artista {nome_artista} foi encontrada!\n')                 
        else:
            print(f'\nAs playlists que contém o artista {nome_artista} são: \n')
            for playlist in playlists_encontradas:
                {funcs.printar_playlist(playlist)}
                print()
        print()
        return menu_usuario()

def buscar_por_nome_playlist():
    nome_playlist = string.capwords(input('\nDigite o nome da playlist procurada ou enter para sair: '))
    if nome_playlist == '':
        return menu_usuario()
    else:
        playlists_cadastradas = funcs.carregar_playlists()
        playlists_encontradas = []

        for playlist in playlists_cadastradas:
            try: 
                if playlist['nome_playlist'] == nome_playlist:
                    playlists_encontradas.append(playlist)
            except:
                pass

        if playlists_encontradas == []:
            print(f'Nenhuma playlist com o nome {nome_playlist} foi encontrada!\n')                 
        else:
            print(f'\nAs playlists cujo nome é {nome_playlist} são: \n')
            for playlist in playlists_encontradas:
                {funcs.printar_playlist(playlist)}
                print()
        print()
        return menu_usuario()

def criar_playlist():
    nome_playlist = string.capwords(input('\nDigite o nome da playlist que deseja criar ou enter para sair: '))
    conteudo = []
    nova_playlist = {}

    if nome_playlist == '':
        return menu_usuario()
    
    while True:
        while True:
            nome_artista = string.capwords(input('\nDigite o nome do artista ou enter para sair: '))
            if nome_artista == '':
                if nova_playlist == {}:
                    return menu_usuario()
                else:
                    return funcs.salvar_playlist(nova_playlist)
            
            albuns_cadastrados = funcs.carregar_albuns()
            try: 
                discografia = list(filter(lambda art: list(art.keys())[0] == nome_artista, albuns_cadastrados))[0]
                if discografia:
                    print(f'Álbuns cadastrados de {nome_artista}: {list(discografia[nome_artista].keys())}\n')
                    break
            except:
                print('Artista não cadastrado ou sem ábuns registrados! Tente novamente!')
        
        while True:
            nome_album = string.capwords(input('\nDigite o nome do álbum ou enter para sair: '))
            if nome_album == '':
                if nova_playlist == {}:
                    return menu_usuario()
                else:
                    return funcs.salvar_playlist(nova_playlist)

            album = discografia[nome_artista].get(nome_album, False)
            
            if album:
                print(f'Músicas do ábum {nome_album} de {nome_artista}: {album}')
                break
            else:
                print('Album não encontrado! Tente novamente.') 
               
        while True:
            nome_musica = string.capwords(input('\nDigite o nome da música ou enter para sair: '))
            if nome_musica == '':
                if nova_playlist == {}:
                    return menu_usuario()
                else:
                    return funcs.salvar_playlist(nova_playlist)

            musica = list(filter(lambda m: m == nome_musica, album))

            if musica:
                break
            else:
                print('Música não encontrada! Tente novamente!')
        
        conteudo.append({nome_musica: {"artista" : nome_artista, 'album': nome_album}}) 

        salvar = input('Digite "S" para salvar a playlist criada ou qualquer coisa para adicionar novas músicas à playlist: ')

        if salvar.lower() == 's':
            nova_playlist = {"nome_playlist": nome_playlist, "conteudo": conteudo}
            print('\nPlaylist adicionada com sucesso!\n')
            funcs.salvar_playlist(nova_playlist)
            return menu_usuario()

'''if __name__ == '__main__':
   menu_usuario()'''
