# -*- coding: UTF-8 -*-

nomes = []

def cadastrar_nome():
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def remover_nome():
    print 'Qual nome você gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

cadastrar_nome()
cadastrar_nome()
cadastrar_nome()
remover_nome()

print nomes
