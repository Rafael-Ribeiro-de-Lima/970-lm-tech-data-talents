import os
import json

def verificar_arquivos(arquivos:list):
    rootdir = os.getcwd()
    pastas = [pasta for pasta in os.listdir(rootdir) if os.path.isdir(pasta)]
    if 'db' not in pastas:
        os.mkdir('db')
    for arquivo in arquivos:
        try:
            with open (arquivo, 'r') as json_file:
                pass
        except:
            with open(arquivo, 'w') as json_file:
                json.dump([], json_file)

if __name__ == '__main__':
    verificar_arquivos(['db/albuns.json', 'db/artistas.json', 'db/playlists.json', 'db/usuarios.json'])