# -*- coding: UTF-8 -*-

def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def listar(nomes):
    print 'Listando nomes:'
    print nomes

def alterar(nomes):
    print 'Qual nome vc gostaria de alterar?'
    nome = raw_input()
    if(nome in nomes):
        index = nomes.index(nome)
        print 'Digite o novo nome para alteração'
        nomes[index] = raw_input()
    else:
        print 'Nome não encontrado'

def procurar(nomes):
    print 'Digite o nome que deseja procurar'
    nome = raw_input()
    if(nome in nomes):
        print 'O nome %s está cadastrado' % (nome)
    else:
        print 'O nome %s não está cadastrado' % (nome)

def menu():
    nomes = []
    menu = ''
    while menu != '0':
        print 'Menu:'
        print '- Digite 1 para cadastrar um nome'
        print '- Digite 2 para remover um nome'
        print '- Digite 3 para alterar um nome'
        print '- Digite 4 para procurar um nome'
        print '- Digite 5 para listar os nomes'
        print '- Digite 0 para finalizar'
        menu = raw_input()
        if (menu == '1'):
            cadastrar(nomes)
        if (menu == '2'):
            remover(nomes)
        if (menu == '3'):
            alterar(nomes)
        if (menu == '4'):
            procurar(nomes)
        if (menu == '5'):
            listar(nomes)
    
menu()