import json

def sair():
    print('Até a próxima!')
    quit()

def carregar_artistas():
    with open("db/artistas.json", "r") as json_file:
        return json.load(json_file)

def salvar_artista(artista):
    artistas = carregar_artistas()
    artistas.append(artista)
    with open("db/artistas.json", "w") as json_file:
        json.dump(artistas, json_file)

def carregar_albuns(artista_album=False):
    with open("db/albuns.json", "r") as json_file:
        discografias = json.load(json_file)
    if not artista_album: # Carrega todos os albuns de todos os artistas com as músicas
        return discografias
    else:    # Carrega apenas o nome dos albuns do artista indicado 
        for discografia in discografias:
            if artista_album in discografia:
                return list(discografia[artista_album].keys())                   
            else:
                return []
                
def salvar_album(artista_album, nome_album, musicas_album):

    with open("db/albuns.json", "r") as json_file:
        discografias = json.load(json_file)
        discografia_atualizada = False
        for discografia in discografias:
            if artista_album in discografia:
                discografia[artista_album][nome_album] = musicas_album
                discografia_atualizada = True
                break
        if not discografia_atualizada:
            discografias.append({artista_album: {nome_album: musicas_album}})
    with open('db/albuns.json', 'w') as json_file:
        json.dump(discografias, json_file, indent=4)

def carregar_playlists():
    with open("db/playlists.json", "r") as json_file:
        return json.load(json_file)
    
def salvar_playlist(nova_playlist):
    with open("db/playlists.json", "r") as json_file:
        playlists = json.load(json_file)
    playlists.append(nova_playlist)
    with open("db/playlists.json", "w") as json_file:
        json.dump(playlists, json_file, indent=4)

def printar_playlist(playlist):
    print('*****'*10)
    print()
    print(f'Nome da Playlist: {playlist["nome_playlist"]}\n')
    print('Conteúdo: \n')
    for n, musica in enumerate(playlist["conteudo"]):
        nome_musica = list(musica.keys())[0]
        print(f'{n+1}. {nome_musica} - Artista: {musica[nome_musica]["artista"]} - Álbum: {musica[nome_musica]["album"]}')
    print()
    print('*****'*10)    