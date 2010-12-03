class No:
    def __init__(self, valor):
        
        self.__valor = valor;
        self.__filhoEsq = None;
        self.__pai = None;
        self.__filhoDir = None;
        self.__vermelho = False;

    def getValor(self):
        return self.__valor;
    def setValor(self, novovalor):
        self.__valor = novovalor;

    def getFilhoEsq(self):
        return self.__filhoEsq;
    def setFilhoEsq(self, novofilhoEsq):
        self.__filhoEsq = novofilhoEsq;
        
    def getPai(self):
        return self.__pai;
    def setPai(self, novopai):
        self.__pai = novopai;

    def getFilhoDir(self):
        return self.__filhoDir;
    def setFilhoDir(self, novofilhoDir):
        self.__filhoDir = novofilhoDir;

    def getVermelho(self):
        return self.__vermelho;
    def setVermelho(self, preto):
        self.__vermelho = preto 

