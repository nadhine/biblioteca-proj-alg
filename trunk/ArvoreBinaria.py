class Arvore:
    def __init__(self, raiz):
        self.__raiz = raiz;
        self.__tamanhore = 1
        self.__folha = folha

    def getRaiz(self):
        return self.__raiz;
    def setRaiz(self, raiz):
        self.__raiz = raiz;

    def getTamanho(self):
        return self.__tamanho;
    def setTamanho(self, tamanho):
        self.__tamanho = tamanho;

        
        

    def InserirNo(self, NoFilho, NoPai):
        #Testa se o Valor do No a ser add [NoFilho] é maior que o do NoPai
        if (self.Info(NoFilho) > self.Info(NoPai)):
            
            #Testa se o NoPai possui filho Dir
            if (self.Direito(NoPai) != None):
                
                #Chama a função recursivamente, mas o NoPai agora vai ser o
                #FilhoDir do NoPai
                InserirNo(NoFilho, self.Direito(NoPai));

            else:
                
                #Inseri o NoFilho como filho direito do NoPai
                NoPai.setFilhoDir(NoFilho);
                
        #Se o valor do NoFilho for menor ou igual ao do NoPai
        else:
            
            #Testa se o NoPai possui filho Esq
            if (self.Esquerdo(NoPai) != None):
                
                #Chama a função recursivamente, mas o NoPai agora vai ser o
                #FilhoEsq do NoPai
                InserirNo(NoFilho, self.Esquerdo(NoPai));

            else:
                
                #Inseri o NoFilho como filho esquerdo do NoPai
                NoPai.setFilhoEsq(NoFilho);

        setTamanho(getTamanho() + 1);


    def InfoNo(self, No):
        return No.getValor();

    def Esquerdo(self, No):
        return No.getFilhoEsq();

    def Direito(self, No):
        return No.getFilhoDir();

    def Pai(self, No):
        return No.getPai();

    def Irmao(self, No):
        Pai = Pai(No);
        if (Esquerdo(Pai) == No):
            return Direito(Pai);
        else:
            return Esquerdo(Pai);

    def ehEsquerdo(self, No):
        Pai = self.Pai(No);
        if (self.Esquerdo(Pai) == No):
            return True;
        else:
            return False;

    def ehDireito(self, No):
        Pai = self.Pai(No);
        if (self.Direito(Pai) == No):
            return True;
        else:
            return False;

    def PreOrdem(self, No, Lista):
        
        Lista.append(No);
        if (self.Esquerdo(No) != None):
            Lista = PreOrdem(self.Esquerdo(No), Lista);
        if (self.Direito(No) != None):
            Lista = PreOrdem(self.Direito(No), Lista);
        else:
            return Lista;

    def ListarPreOrdem(self):
        Lista = [];
        Lista = PreOrdem(self.getRaiz(), Lista);

        return Lista;

    def Ordem(self, No, Lista):

        
        if (self.Esquerdo(No) != None):
            Lista = Ordem(self.Esquerdo(No), Lista);
        Lista.append(No);
        if (self.Direito(No) != None):
            Lista = Ordem(self.Direito(No), Lista)
        else:
            return Lista;

    def ListarOrdem(self):
        Lista = [];
        Lista = Ordem(self.getRaiz(), Lista);

        return Lista;

    def PosOrdem(self, No, Lista):

        
        if (self.Esquerdo(No) != None):
            Lista = PosOrdem(self.Esquerdo(No), Lista);

        elif (self.Direito(No) != None):
            Lista = PosOrdem(self.Direito(No), Lista)
        Lista.append(No)
        else:
            return Lista;

    def ListarPosOrdem(self):
        Lista = [];
        Lista = PosOrdem(self.getRaiz(), Lista);

        return Lista;

    def Maximo(self):
        aux = self.getRaiz();

        while (self.Direito(aux)!= None):
            aux = self.Direito(aux);

        return aux;

    def Minimo(self):
        aux = self.getRaiz();

        while (self.Esquerdo(aux) != None):
            aux = self.Esquerdo(aux);

        return aux;

    def Sucessor(self, No):
        if (self.Direito(No) != None):
            aux = self.Direito(No);
            while (self.Esquerdo(aux) != None):
                aux = self.Esquerdo(aux);
            return aux;
        else:
            aux = No;
            while (self.ehEsquerdo(aux) == False):
                aux = self.Pai(aux);
            return self.Pai(aux);

        
    def Predecessor(self, No):
        if (self.Esquerdo(No) != None):
            aux = self.Esquerdo(No);
            while (self.Direito(aux)!= None):
                aux = self.Direito(aux);
            return aux;
        else:
            aux = No;
            while(self.ehDireito(aux) == False):
                aux = self.Pai(aux);
            return self.Pai(aux);
            

    def DeletarNo(self, No):
        if (self.Direito(No)== None and self.Esquerdo(No) == None):
            No = None;

        elif (self.Esquerdo(No) != None and self.Direito(No) == None):
            aux = self.Predecessor(No);
            self.DeletarNo(self.Predecessor(No));
            No.setValor() = aux.setValor();

        else:
            aux = self.Sucessor(No);
            self.DeletarNo(Sucessor(No));
            No.setValor() = aux.setValor()
                
     def busca(self, no):
         if (no.getValor() == self.getRaiz.getValor()):
             return no
         else:
             if (no.getValor() < self.getRaiz.getValor()):
                 return self.busca(self.Esquerdo(no))

            else:
                return self.busca(self.Direito(no))
            
                

       
