import re

# \s tab
# \d numeros
# \w letras e numeros
# ? opcional ex: \d?
# ^ Começa com string ex: ^#
# $ Final da string  ex: xt$
# {} limite de caracteres ex: {6}

result = re.match('[A-Za-z]y','Python')
print result.group()

result = re.findall('[A-Za-z]y','Python ou Rython')
print result

result = re.findall('[A-Za-z]y[A-Za-z]+','Python ou Rython')
print result

result = re.findall('\wy\w+','Python ou Rython ou 9ython')
print result

result = re.findall('\wy\w+','Python ou Rython ou 9ython')
print result

def procurar_regex(nomes):
    print('Digite a expressão regular')
    regex = raw_input()
    nomes_concatenados = ' '.join(nomes)
    resultado = re.findall(regex, nomes_concatenados)
    print resultado
	