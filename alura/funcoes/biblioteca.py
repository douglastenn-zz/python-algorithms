def gera_nome_convite(nome):
    return nome[0:4] + ' ' + nome[len(nome)-4:len(nome)]

def envia_convite(nome_formatado):
    return "Enviando convite para " + nome_formatado


def processa_convite(nome):
    nome_formatado = gera_nome_convite(nome)
    return envia_convite(nome_formatado)