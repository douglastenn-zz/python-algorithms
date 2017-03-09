import datetime

idades = []

def ano_como_string():
    print 'Digite o ano de nascimento:'
    ano = raw_input()
    now = datetime.datetime.now()
    idade = now.year - int(ano)
    idades.append(idade)


ano_como_string()
ano_como_string()
ano_como_string()

print idades
