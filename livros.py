""" Esse programa tem por objetivo facilitar o manejo de um carrinho para compras de livro.
Ele solicita o nome do cliente e cria um arquivo,caso ele não exista, com o nome do cliente,
onde será guardado os livros que serão comprados. O programa utiliza um arquivo chamado 'preco'
que guarda os títulos e respectivos preços dos livros disponíveis para compra. Dessa maneira,
é possível adicionar livros ao carrinho, retirar, checar que livros estão no carrinho
e verificar o preço total dos livros no carriho. Outras funcionalidades possíveis são
checar todos os títulos disponíveis no catálogo, fazer uma busca por livros no catálogo e
adicionar títulos ao catálogo ou retirá-los. """

import pickle
from classes import Cliente
from pathlib import Path
import os

with open('preco.pkl', 'rb') as fp:  # aqui carregamos o arquivo com os títulos e preços disponíveis.
    preco = pickle.load(fp)

nome_cliente=input("entre com seu nome\n")  # o cliente se identifica aqui para determinar seu carrinho
cliente=Cliente(nome_cliente)

while True: # aqui temos o menu de ações possíveis.

    chave=input("""    digite 1 para adicionar um livro ao carrinho.
    digite 2 para retirar um livro do carrinho
    digite 3 para mostrar os livros no carrinho
    digite 4 para mostrar o custo total do carrinho
    digite 5 para ver o catalogo
    digite 6 para pesquisar por um livro no catalogo
    digite 7 para adicionar um livro ao catalogo
    digite 8 para retirar um livro do catalogo
    digite 9 para apagar o carrinho
    digite 0 para sair do programa\n""")
    
    if chave=='1':
        cliente.adicionar(preco)  #aqui se adiciona um livro ao carrinho. Deve-se digitar o titulo do livro como está escrito no catálogo
    if chave=='2':
        cliente.retirar()         # aqui se retira um livro do carriho. Deve-se digitar o titulo do livro como está escrito no catálogo

    if chave =='3':
        cliente.mostrar_carrinho() # aqui se mostra todos os livros no carrinho.
    if chave =='4':
        cliente.preco_total(preco) # aqui se verifica o preço total  dos livros no carrinho.
    if chave =='5':
        cliente.disponiveis(preco)# aqui se verifica os títulos disponíveis no catálogo e seus respectivos preços.
    if chave == '6':
        cliente.pesquisar(preco) # aqui se pode procurar por títulos específicos no catálogo.
    if chave == '7':
        cliente.novo(preco) # aqui se adicona um novo livro e seu preço no catálogo.
    if chave =='8':
        cliente.deletar(preco) # aqui se retira um livro do catálogo. Essa ação também retira o livro do carrinho.
    if chave == '9':
        cliente.deletar_carrinho() # apaga o carrinho atual e sai do programa
        break

    if chave=='0':
        print('volte logo!') # aqui se sai do programa.
        break

