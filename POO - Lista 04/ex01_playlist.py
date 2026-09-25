# ==========================================
# CLASSE MUSICA
# ==========================================

class Musica:
    def __init__(self, titulo, artista, album):
        self.titulo = titulo
        self.artista = artista
        self.album = album

    # GET E SET DO TITULO

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo

    # GET E SET DO ARTISTA

    def getArtista(self):
        return self.artista

    def setArtista(self, artista):
        self.artista = artista

    # GET E SET DO ALBUM

    def getAlbum(self):
        return self.album

    def setAlbum(self, album):
        self.album = album

    # TOSTRING

    def ToString(self):
        return f"Título: {self.titulo}, Artista: {self.artista}, Álbum: {self.album}"


# ==========================================
# CLASSE PLAYLIST
# ==========================================

class PlayList:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.musicas = []

    # GET E SET DO NOME

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    # GET E SET DA DESCRICAO

    def getDescricao(self):
        return self.descricao

    def setDescricao(self, descricao):
        self.descricao = descricao

    # INSERIR MUSICA

    def Inserir(self, musica):
        self.musicas.append(musica)

    # LISTAR MUSICAS

    def Listar(self):
        return self.musicas

    # TOSTRING

    def ToString(self):
        return f"Playlist: {self.nome} - {len(self.musicas)} músicas"


# ==========================================
# CLASSE UI
# ==========================================

class UI:
    def __init__(self):
        self.playlists = []

    # INSERIR PLAYLIST

    def InserirPlaylist(self, playlist):
        self.playlists.append(playlist)

    # LISTAR PLAYLISTS

    def ListarPlaylists(self):
        return self.playlists

    # INSERIR MUSICA

    def InserirMusica(self, playlist, musica):
        playlist.Inserir(musica)

    # LISTAR MUSICAS

    def ListarMusicas(self, playlist):
        return playlist.Listar()


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

ui = UI()


# ==========================================
# PLAYLISTS
# ==========================================

print("========== PLAYLIST ==========")

playlistFunk = PlayList(
    "Funk",
    "Playlist de funk"
)

playlistTrap = PlayList(
    "Trap",
    "Playlist de trap"
)


# ==========================================
# MUSICAS DO MC IG
# ==========================================

musica1 = Musica(
    "3 Dias Virado",
    "MC IG",
    "Funk"
)

musica2 = Musica(
    "Let's Go 4",
    "MC IG",
    "Funk"
)

musica3 = Musica(
    "Goodnight Menina",
    "MC IG",
    "Funk"
)


# ==========================================
# MUSICAS DO MATUÊ
# ==========================================

musica4 = Musica(
    "Máquina do Tempo",
    "Matuê",
    "Máquina do Tempo"
)

musica5 = Musica(
    "Anos Luz",
    "Matuê",
    "Matuê"
)

musica6 = Musica(
    "333",
    "Matuê",
    "333"
)


# ==========================================
# INSERINDO MUSICAS
# ==========================================

ui.InserirMusica(playlistFunk, musica1)
ui.InserirMusica(playlistFunk, musica2)
ui.InserirMusica(playlistFunk, musica3)

ui.InserirMusica(playlistTrap, musica4)
ui.InserirMusica(playlistTrap, musica5)
ui.InserirMusica(playlistTrap, musica6)


# ==========================================
# INSERINDO PLAYLISTS
# ==========================================

ui.InserirPlaylist(playlistFunk)
ui.InserirPlaylist(playlistTrap)


# ==========================================
# LISTANDO PLAYLISTS
# ==========================================

for playlist in ui.ListarPlaylists():

    print()
    print(playlist.ToString())
    print(f"Descrição: {playlist.getDescricao()}")

    for musica in ui.ListarMusicas(playlist):
        print(musica.ToString())