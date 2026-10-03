from playlist import PlayList
from musica import Musica
from playlist_item import PlayListItem


class UI:

    playlists = []
    musicas = []
    itens = []

    # =========================
    # PLAYLIST
    # =========================

    @staticmethod
    def inserir_playlist():
        id = int(input("ID da playlist: "))
        nome = input("Nome: ")
        descricao = input("Descrição: ")

        playlist = PlayList(id, nome, descricao)

        UI.playlists.append(playlist)

        print("Playlist cadastrada!")

    @staticmethod
    def listar_playlists():
        if len(UI.playlists) == 0:
            print("Nenhuma playlist cadastrada.")
            return

        for playlist in UI.playlists:
            print(playlist)

    @staticmethod
    def atualizar_playlist():
        id = int(input("ID da playlist: "))

        for playlist in UI.playlists:
            if playlist.get_id() == id:

                nome = input("Novo nome: ")
                descricao = input("Nova descrição: ")

                playlist.set_nome(nome)
                playlist.set_descricao(descricao)

                print("Playlist atualizada!")
                return

        print("Playlist não encontrada.")

    @staticmethod
    def excluir_playlist():
        id = int(input("ID da playlist: "))

        for playlist in UI.playlists:
            if playlist.get_id() == id:
                UI.playlists.remove(playlist)
                print("Playlist excluída!")
                return

        print("Playlist não encontrada.")

    # =========================
    # MÚSICAS
    # =========================

    @staticmethod
    def inserir_musica():
        id = int(input("ID da música: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")
        duracao = float(input("Duração em minutos: "))

        musica = Musica(
            id,
            titulo,
            artista,
            album,
            duracao
        )

        UI.musicas.append(musica)

        print("Música cadastrada!")

    @staticmethod
    def listar_musicas():
        if len(UI.musicas) == 0:
            print("Nenhuma música cadastrada.")
            return

        for musica in UI.musicas:
            print(musica)

    @staticmethod
    def atualizar_musica():
        id = int(input("ID da música: "))

        for musica in UI.musicas:
            if musica.get_id() == id:

                titulo = input("Novo título: ")
                artista = input("Novo artista: ")
                album = input("Novo álbum: ")
                duracao = float(input("Nova duração: "))

                musica.set_titulo(titulo)
                musica.set_artista(artista)
                musica.set_album(album)
                musica.set_duracao(duracao)

                print("Música atualizada!")
                return

        print("Música não encontrada.")

    @staticmethod
    def excluir_musica():
        id = int(input("ID da música: "))

        for musica in UI.musicas:
            if musica.get_id() == id:
                UI.musicas.remove(musica)
                print("Música excluída!")
                return

        print("Música não encontrada.")

    # =========================
    # ITENS DA PLAYLIST
    # =========================

    @staticmethod
    def inserir_item():
        id = int(input("ID do item: "))
        id_playlist = int(input("ID da playlist: "))
        id_musica = int(input("ID da música: "))
        data = input("Data de inclusão: ")
        sequencia = int(input("Sequência: "))

        item = PlayListItem(
            id,
            id_playlist,
            id_musica,
            data,
            sequencia
        )

        UI.itens.append(item)

        for playlist in UI.playlists:
            if playlist.get_id() == id_playlist:
                playlist.adicionar_item(item)

        print("Música adicionada à playlist!")

    @staticmethod
    def listar_itens():
        if len(UI.itens) == 0:
            print("Nenhum item cadastrado.")
            return

        for item in UI.itens:
            print(item)

    @staticmethod
    def atualizar_item():
        id = int(input("ID do item: "))

        for item in UI.itens:
            if item.get_id() == id:

                id_playlist = int(input("Novo ID da playlist: "))
                id_musica = int(input("Novo ID da música: "))
                data = input("Nova data: ")
                sequencia = int(input("Nova sequência: "))

                item.set_id_playlist(id_playlist)
                item.set_id_musica(id_musica)
                item.set_data_inclusao(data)
                item.set_sequencia(sequencia)

                print("Item atualizado!")
                return

        print("Item não encontrado.")

    @staticmethod
    def excluir_item():
        id = int(input("ID do item: "))

        for item in UI.itens:
            if item.get_id() == id:
                UI.itens.remove(item)
                print("Item excluído!")
                return

        print("Item não encontrado.")

    # =========================
    # MENU
    # =========================

    @staticmethod
    def main():

        while True:

            print()
            print("========== PLAYLIST ==========")
            print("1 - Inserir playlist")
            print("2 - Listar playlists")
            print("3 - Atualizar playlist")
            print("4 - Excluir playlist")
            print()
            print("5 - Inserir música")
            print("6 - Listar músicas")
            print("7 - Atualizar música")
            print("8 - Excluir música")
            print()
            print("9 - Inserir música na playlist")
            print("10 - Listar itens das playlists")
            print("11 - Atualizar item")
            print("12 - Excluir item")
            print()
            print("0 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                UI.inserir_playlist()

            elif opcao == "2":
                UI.listar_playlists()

            elif opcao == "3":
                UI.atualizar_playlist()

            elif opcao == "4":
                UI.excluir_playlist()

            elif opcao == "5":
                UI.inserir_musica()

            elif opcao == "6":
                UI.listar_musicas()

            elif opcao == "7":
                UI.atualizar_musica()

            elif opcao == "8":
                UI.excluir_musica()

            elif opcao == "9":
                UI.inserir_item()

            elif opcao == "10":
                UI.listar_itens()

            elif opcao == "11":
                UI.atualizar_item()

            elif opcao == "12":
                UI.excluir_item()

            elif opcao == "0":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida.")


UI.main()