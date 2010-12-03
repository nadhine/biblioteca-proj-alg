class Usuario:
    def __init__(self, codigo, nome, cpf, telefone):
        self.__codigo = codigo
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        
    def getCodigo(self):
        return self.__codigo;
    def setCodigo(self):
        self.__codigo = codigo;

    def getNome(self):
        return self.__nome;
    def setNome(self, nome):
        self.__nome = nome;

    def getCpf(self):
        return self.__cpf;
    def setNome(self, cpf):
        self.__cpf = cpf;

    def getTelefone(self):
        return self.__telefone;
    def setTelefone(self, telefone):
        self.__telefone = telefone;

