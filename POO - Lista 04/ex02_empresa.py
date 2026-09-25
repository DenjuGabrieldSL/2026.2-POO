# ==========================================
# CLASSE CLIENTE
# ==========================================

class Cliente:
    def __init__(self, nome, cpf, limite):
        self.nome = nome
        self.cpf = cpf
        self.limite = limite
        self.socio = None

    # GET E SET DO NOME

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    # GET E SET DO CPF

    def getCpf(self):
        return self.cpf

    def setCpf(self, cpf):
        self.cpf = cpf

    # GET E SET DO LIMITE

    def GetLimite(self):
        if self.socio is not None:
            return self.limite + self.socio.limite

        return self.limite

    def SetLimite(self, limite):
        self.limite = limite

    # DEFINIR SOCIO

    def SetSocio(self, socio):
        self.socio = socio
        socio.socio = self

    # TOSTRING

    def ToString(self):
        texto = (
            f"Nome: {self.nome}, "
            f"CPF: {self.cpf}, "
            f"Limite: R$ {self.GetLimite():.2f}"
        )

        if self.socio is not None:
            texto += f", Sócio: {self.socio.nome}"

        return texto


# ==========================================
# CLASSE EMPRESA
# ==========================================

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []

    # GET E SET DO NOME

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    # INSERIR CLIENTE

    def Inserir(self, cliente):
        self.clientes.append(cliente)

    # LISTAR CLIENTES

    def Listar(self):
        return self.clientes


# ==========================================
# CLASSE UI
# ==========================================

class UI:
    def __init__(self):
        self.empresas = []

    # INSERIR EMPRESA

    def InserirEmpresa(self, empresa):
        self.empresas.append(empresa)

    # LISTAR EMPRESAS

    def ListarEmpresas(self):
        return self.empresas

    # INSERIR CLIENTE

    def InserirCliente(self, empresa, cliente):
        empresa.Inserir(cliente)

    # ASSOCIAR CLIENTES

    def AssociarClientes(self, cliente1, cliente2):
        cliente1.SetSocio(cliente2)

    # LISTAR CLIENTES

    def ListarClientes(self, empresa):
        return empresa.Listar()


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

ui = UI()


# ==========================================
# EMPRESA
# ==========================================

print("========== EMPRESA ==========")

empresa = Empresa("Empresa de Cartão")


# ==========================================
# CLIENTES
# ==========================================

cliente1 = Cliente(
    "João",
    "111.111.111-11",
    1000
)

cliente2 = Cliente(
    "Maria",
    "222.222.222-22",
    2000
)

cliente3 = Cliente(
    "Carlos",
    "333.333.333-33",
    1500
)


# ==========================================
# INSERINDO EMPRESA
# ==========================================

ui.InserirEmpresa(empresa)


# ==========================================
# INSERINDO CLIENTES
# ==========================================

ui.InserirCliente(empresa, cliente1)
ui.InserirCliente(empresa, cliente2)
ui.InserirCliente(empresa, cliente3)


# ==========================================
# ASSOCIANDO JOÃO E MARIA
# ==========================================

ui.AssociarClientes(cliente1, cliente2)


# ==========================================
# MOSTRANDO EMPRESA
# ==========================================

print(f"Empresa: {empresa.getNome()}")

print("\nClientes:")

for cliente in ui.ListarClientes(empresa):
    print(cliente.ToString())