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
        y = self.Direito(x)
        self.Direito(x) = self.Esquerdo(y)
        if self.Esquerdo(y) != self.getFolha():
            y.getFilhoEsq().setPai(x)
        self.Pai(y) = self.Pai(x)
        if self.Pai(x) == self.getFolha():
            self.setRaiz(y)
        elif x == x.getPai().getFilhoEsq(): 
            x.getPai().setFilhoEsq(y) #x.irmao = y?
        else:
            x.getPai().setFilhoDir(y) #x.irmao = y?
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

    def InserirNovoNo(self, No):
        self.InserirNo(No, self.getRaiz())
        self.InsertFixup(No)


    def InsertFixup(self, No):
        while (No.getPai().getVermelho() == True):
            
            if (No.getPai() == No.getPai().getPai().getFilhoEsq()):
                aux = No.getPai().getPai().getFilhoDir()
                
                if (aux.getVermelho() == True):
                    No.getPai().setVermelho(False)
                    aux.setVermelho(False)
                    No.getPai().getPai().setVermelho(True)
                    No = No.getPai().getPai()

                else:
                    
                    if(No == No.getPai().getFilhoDir()):
                        
                        No = No.getPai()
                        self.rotacaoEsq(No)

                        No.getPai().setVermelho(False)
                        No.getPai().getPai().setVermelho(True)
                        self.rotacaoDir(No.getPai().getPai())


            else:
                
                aux = No.getPai().getPai().getFilhoEsq()
                
                if (aux.getVermelho() == True):
                    No.getPai().setVermelho(False)
                    aux.setVermelho(False)
                    No.getPai().getPai().setVermelho(True)
                    No = No.getPai().getPai()

                else:
                    
                    if(No == No.getPai().getFilhoEsq()):
                        
                        No = No.getPai()
                        self.rotacaoDir(No)

                        No.getPai().setVermelho(False)
                        No.getPai().getPai().setVermelho(True)
                        self.rotacaoEsq(No.getPai().getPai())


        self.getRaiz().setVermelho(False)


    def DeletarNovoNo(self, No):
        
        self.DeletarNo(No)
        if (No.getVermelho() == False):
            self.DeletFixup(No)
        
            


                    
    
