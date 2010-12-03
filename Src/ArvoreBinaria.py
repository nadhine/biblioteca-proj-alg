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
        if (Info(NoFilho) > Info(NoPai)):
            
            #Testa se o NoPai possui filho Dir
            if (Direito(NoPai) != None):
                
                #Chama a função recursivamente, mas o NoPai agora vai ser o
                #FilhoDir do NoPai
                InserirNo(NoFilho, Direito(NoPai));

            else:
                
                #Inseri o NoFilho como filho direito do NoPai
                NoPai.setFilhoDir(NoFilho);
                
        #Se o valor do NoFilho for menor ou igual ao do NoPai
        else:
            
            #Testa se o NoPai possui filho Esq
            if (Esquerdo(NoPai) != None):
                
                #Chama a função recursivamente, mas o NoPai agora vai ser o
                #FilhoEsq do NoPai
                InserirNo(NoFilho, Esquerdo(NoPai));

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
        Pai = Pai(No);
        if (Esquerdo(Pai) == No):
            return True;
        else:
            return False;

    def ehDireito(self, No):
        Pai = Pai(No);
        if (Direito(Pai) == No):
            return True;
        else:
            return False;

    def PreOrdem(self, No, Lista):
        
        Lista.append(No);
        if (Esquerdo(No) != None):
            Lista = PreOrdem(Esquerdo(No), Lista);
        if (Direito(No) != None):
            Lista = PreOrdem(Direito(No), Lista);
        else:
            return Lista;

    def ListarPreOrdem(self):
        Lista = [];
        Lista = PreOrdem(getRaiz(), Lista);

        return Lista;

    def Ordem(self, No, Lista):

        
        if (Esquerdo(No) != None):
            Lista = Ordem(Esquerdo(No), Lista);
        Lista.append(No);
        if (Direito(No) != None):
            Lista = Ordem(Direito(No), Lista)
        else:
            return Lista;

    def ListarOrdem(self):
        Lista = [];
        Lista = Ordem(getRaiz(), Lista);

        return Lista;

    def PosOrdem(self, No, Lista):

        
        if (Esquerdo(No) != None):
            Lista = PosOrdem(Esquerdo(No), Lista);

        elif (Direito(No) != None):
            Lista = PosOrdem(Direito(No), Lista)
        Lista.append(No)
        else:
            return Lista;

    def ListarPosOrdem(self):
        Lista = [];
        Lista = PosOrdem(getRaiz(), Lista);

        return Lista;

    def Maximo(self):
        aux = getRaiz();

        while (Direito(aux)!= None):
            aux = Direito(aux);

        return aux;

    def Minimo(self):
        aux = getRaiz();

        while (Esquerdo(aux) != None):
            aux = Esquerdo(aux);

        return aux;

    def Sucessor(self, No):
        if (Direito(No) != None):
            aux = Direito(No);
            while (Esquerdo(aux) != None):
                aux = Esquerdo(aux);
            return aux;
        else:
            aux = No;
            while (ehEsquerdo(aux) == False):
                aux = Pai(aux);
            return Pai(aux);

        
    def Predecessor(self, No):
        if (Esquerdo(No) != None):
            aux = Esquerdo(No);
            while (Direito(aux)!= None):
                aux = Direito(aux);
            return aux;
        else:
            aux = No;
            while(ehDireito(aux) == False):
                aux = Pai(aux);
            return Pai(aux);
            

    def DeletarNo(self, No):
        if (Direito(No)== None and Esquerdo(No) == None):
            No = None;

        elif (Esquerdo(No) != None and Direito(No) == None):
            aux = Predecessor(No);
            DeletarNo(Predecessor(No));
            No.setValor() = aux.setValor();

        else:
            aux = Sucessor(No);
            DeletarNo(Sucessor(No));
            No.setValor() = aux.setValor()
                
     def busca(self, no):
         if no.getValor == self.getRaiz.getValor:
             return no
         else:
             if no.getValor < self.getRaiz.getValor:
                 return busca(Esquerdo(self),no)
                return busca(Direito(self),no)
            
                

       
