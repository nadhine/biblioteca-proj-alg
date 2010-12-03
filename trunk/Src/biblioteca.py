import os

class Biblioteca:
    def __init__(self):
        ArvoreUsuario = ArvoreUsuario(ArvoreRB)
        ArvoreLivro = ArvoreLivro(ArvoreRB)
        
    def adcLivro(self, novoLivro):
        valor = novoLivro.getCodigo
        if not(os.path.exists('Livros.txt')):
            m=open('Livros.txt','w') 
            m.close()
        inserirNoFixUp(???ArvoreLivro, valor, )
        
        
    def delLivro(self, livro):
        valor = livro.getCodigo
        
    def adcUsuario(self, novoUsuario):
        valor = novoUsuario.getCodigo
        if not(os.path.exists('Usuarios.txt')):
            m=open('Usuarios.txt','w') 
            m.close()
        inserirNoFixUp...

    def delUsuario(self, usuario):

    def buscaLivro(self,codLivro):
        livro = busca(ArvoreLivro, codLivro)
        codLivro = livro.getCodigo()
        P = pickle.load(file('teste1.pck','r'))
        

        
    def reserva(self, livro):
        if livro.getDisponivel == False:
            livro.setDisponivel(livro.getDisponivel)
        
