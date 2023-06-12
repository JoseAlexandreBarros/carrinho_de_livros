from pathlib import Path
import pickle
import os


class Cliente : # aqui se inicia a classe que contém todos os métodos utilizados.
    def __init__(self,nome):
        self.nome=nome # o nome do cliente que é utilizado para criar o carrinho especifico do cliente.
        self.carrinho={} # aqui se cria o dicionário que determina os livros e suas respectivas quantidades no carrinho.

        myfile = Path(f'{nome}.pkl') # aqui se cria o arquivo que guarda o dicionário do carrinho do cliente.
        myfile.touch(exist_ok=True)
        with open(f'{self.nome}.pkl', 'wb') as fp:# o novo dicionário é salvo no arquivo do carrinho.
                pickle.dump(self.carrinho, fp)
       


    def adicionar(self,preco): # método para adicionar um livro ao carrinho. O dicionário 'preco' é passado como parametro.
        with open(f'{self.nome}.pkl', 'rb') as fp: # primeiramente,  abre-se o arquivo do dicionário do carrinho para checar o status atual.
            self.carrinho = pickle.load(fp)
        livro=input("digite o nome do livro\n")# deve se digitar o nome do livro como está no catálogo.
        if livro in preco.keys(): # aqui se determina se exite o livro no catálogo.
            if livro in self.carrinho.keys(): #se o livro existir, o dicionário do carrinho é atualizado.
                self.carrinho[livro]+=1
            else:
                self.carrinho[livro]=1
            with open(f'{self.nome}.pkl', 'wb') as fp:# o novo dicionário é salvo no arquivo do carrinho.
                pickle.dump(self.carrinho, fp)
            print("livro adicionado ao carrinho")# mensagem de sucesso.
            return
        else:                               # se o livro não existir, a mensagem de erro ocorre
            print("livro não encontrado")
            return
        

    def preco_total(self,preco): # aqui se apresenta o preço total dos itens no carrinho.O dicionário 'preco' é passado como parametro.
        total=0                  # acumulador.
        with open(f'{self.nome}.pkl', 'rb') as fp: # abre-se o arquivo do carrinho para checar o status atual.
            self.carrinho = pickle.load(fp)
        for livros in self.carrinho.keys(): # para cada chave no dicionário do carrinho e do preco, 
            total+=self.carrinho[livros]*preco[livros] #multiplica-se o preço pela quantidade e adiciona-se ao total
        print(f"O total é {total}") # mensagem com o preço total dos livros no carrinho.
        return

    def retirar(self): # método para retirar um livro ao carrinho.
        with open(f'{self.nome}.pkl', 'rb') as fp: # abre-se o arquivo do dicionário do carrinho para checar o status atual.
            self.carrinho = pickle.load(fp)
        livro=input("digite o nome do livro\n") # deve-se digitar o nome do livro como está no catálogo.
        if livro in self.carrinho.keys(): # checa se o livro está no carrinho.
            del self.carrinho[livro] # retira o livro do dicionário do carrinho.
            with open(f'{self.nome}.pkl', 'wb') as fp: # salva o novo status do dicionário do carriho.
                pickle.dump(self.carrinho, fp)
            print('livro retirado') # mensagem de sucesso
            return
        
        print('livro não está no carrinho')# caso o livro não esteja no carrinho, aparece a mensagem de erro.
        return
      
        
    def mostrar_carrinho(self):  #método para mostrar que livros estão no carrinho.
        i=False
        with open(f'{self.nome}.pkl', 'rb') as fp: #abre-se o arquivo do dicionário do carrinho e imprime cada chave.
            self.carrinho = pickle.load(fp)
        for livro in self.carrinho.keys():
            i=True
            print(livro)
        if i==False:
            print("não há livros no carrinho")
        return

    def disponiveis(self,preco): # método para ver todos os títulos do catálogo e seu respectivos preços.O dicionário 'preco' é passado como parametro.
        print("Os livros disponiveis são:\n")
        for livros in preco.keys():
            print(f'Título:{livros},preço:{preco[livros]}')
            print('\n')
        return

    def pesquisar(self,preco):# método para pesquisar por um determinado título.O dicionário 'preco' é passado como parametro.
        i=False
        pesquisa=input("digite a sua pesquisa:\n")# digita-se o texto que será procurado nos títulos.
        for livros in preco.keys():
            if (pesquisa in livros): # se o texto existir numa chave, a chave é impressa.
                print(livros)
                i=True         # 'i' é setado como 'true' para indicar que uma correspondencia foi encontrada.
        if i==False:
            print('nenhuma correspondencia') # se 'i' é falso, nenhuma correspondenca foi encontrada e a mensagem de erro aparece.
        return

    def novo(self,preco): #método para inserir um novo título no catálogo.
        titulo=input("Digite o título do novo livro\n") # aqui se entra com o novo título.
        price=int(input("Digite o preço do novo livro\n"))# aqui se entra com o preço do novo título.
        if titulo in preco.keys():
            print("livro já existente")
            return
        else:
            preco[titulo]=price
            print("Novo livro adicionado")
            with open('preco.pkl', 'wb') as fp:
                pickle.dump(preco, fp)
            return

    def deletar(self,preco): # método para remover título do catálogo.
        titulo=input("Digite o título do livro a ser retirado do catalogo:\n")
        if titulo in preco.keys():
            del preco[titulo]
            with open('preco.pkl', 'wb') as fp:
                pickle.dump(preco, fp)
            with open(f'{self.nome}.pkl', 'rb') as fp: # o método também retira o livro caso esteja no carrinho.
                self.carrinho = pickle.load(fp)
            if titulo in self.carrinho.keys():
                del self.carrinho[titulo]
            with open(f'{self.nome}.pkl', 'wb') as fp:
                pickle.dump(self.carrinho, fp)
            print("Livro retirado do catalogo")
            return
        else:
            print('livro nao encontrado no catalogo\n' )
            return

    def deletar_carrinho (self): # método que apaga o carrinho atual e sai do programa.
        os.remove(f'{self.nome}.pkl')
        print('carrinho apagado')
        return
