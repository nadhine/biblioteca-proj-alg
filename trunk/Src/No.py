class No:
    def __init__(self, valor):
        
        self.__valor = valor;
        self.__filhoEsq = None;
        self.__pai = None;
        self.__filhoDir = None;

    def getValor(self):
        return self.__valor;
    def setValor(self, valor):
        self.__valor = valor;

    def getFilhoEsq(self):
        return self.__filhoEsq;
    def setFilhoEsq(self, filhoEsq):
        self.__filhoEsq = filhoEsq;
        
    def getPai(self):
        return self.__pai;
    def setPai(self, pai):
        self.__pai = pai;

    def getFilhoDir(self):
        return self.__filhoDir;
    def setFilhoDir(self, filhoDir):
        self.__filhoDir = filhoDir;

