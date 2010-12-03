class livro:
    def __init__(self, codigo, nome, autor, ano, disponivel):
        self.__codigo = codigo
        self.__nome = nome
        self.__autor = autor
        self.__ano = ano
        self.__disponivel = True

    def getCodigo(self):
        return self.__codigo;
    def setCodigo(self, codigo):
        self.__codigo = codigo;

    def getNome(self):
        return self.__nome;
    def setNome(self, nome):
        self.__nome = nome;

    def getAutor(self):
        return self.__autor;
    def setAutor(self, autor):
        self.__autor = autor;

    def getAno(self):
        return self.__ano;
    def setAno(self, ano):
        self.__ano = ano;

    def getDisponivel(self):
        return self.__disponivel;
    def setDisponivel(self, disponivel):
        self.__disponivel = disponivel;
