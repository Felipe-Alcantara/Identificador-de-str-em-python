mensagem = 'olá mundo'
print(mensagem)

d = str(input('Digite alguma coisa: '))
print(type(d))
print('É alfabético?', d.isalpha())
print('É Numérico?', d.isnumeric())
print('É alfanumérico?', d.isalnum())
print('Está tudo escrito em maiúsculo?', d.isupper())
print('Está tudo escrito em minúsculo?', d.islower())
print('É um número decimal?', d.isdecimal())
print('É um identificador?', d.isidentifier())
print('Pode ser impresso?', d.isprintable())
print('Começa com letras maiúsculas e termina com minúsculas?', d.istitle())
print('É um dígito?', d.isdigit())
print('Este caractere é um indentificador?', d.isspace())
