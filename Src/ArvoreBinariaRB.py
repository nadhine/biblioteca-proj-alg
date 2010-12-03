class ArvoreRB(Arvore):
    def __init__(self, arvore):
        self.__arvore = arvore
        self.__tamanhoPreto = 1
        self.__folha = No(None)

    def getArvore(self):
        return self.__arvore;
    def setArvore(self, arvore):
        self.__Arvore = arvore;

    def getTamanhoPreto(self):
        return self.__tamanhoPreto;
    def setTamanhoPreto(self,amanhoPreto):
        self.__tamanhoPreto = tamanhoPreto;

    def getFolha(self):
        return self.__folha;

    
        
    def rotacaoEsq(self, x):
        y = Direito(x)
        Direito(x) = Esquerdo(y)
        if Esquerdo(y) != self.getFolha:
            y.getFilhoEsq.getPai = x
        Pai(y) = Pai(x)
        if Pai(x) == self.getFolha:
            self.getRaiz = y
        elif x == x.getPai.__filhoEsq: 
            x.pai.__filhoEsq = y #x.irmao = y?
        else:
            x.pai.__filhoDir = y #x.irmao = y?
        y.__filhoEsq = x
        Pai(x) = y


    def rotacaoDir(self, y):
        x = Esquerdo(y)
        Esquerdo(y) = Direito(x)
        if Direito(x)!= self.getFolha:
            x.getFilhoDir.getPai = y
        Pai(x) = Pai(y)
        if y.p == self.getFolha:
            self.getRaiz = x
        elif y == y.getPai.getFilhoDir:
            y.getPai.getFilhoDir = x
        else:
            y.getPai.getFilhoEsq = x
        Direito(x) = y
        Pai(y) = x

        
    
