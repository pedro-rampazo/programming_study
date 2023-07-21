"""
Detecção de Senha Robusta
Crie uma função que utilize expressões regulares para garantir que a string
da senha recebida seja robusta. Uma senha robusta deve ter pelo menos 8 caracteres,
deve conter tanto letras maiúsculas quanto letras minúsculas e ter pelo menos um dígito.
Talvez seja necessário testar a string em relação a diversos padrões de Regex para validar
a robustez.
"""
import re

def is_strong_password(password):
    character_rules = [re.compile('[A-Z]'), re.compile('[a-z]'), re.compile('[0-9]')]
    founded_characters = list()

    if len(password) < 8:
        return False
    
    for cr in character_rules:
        fc = cr.search(password)
        founded_characters.append(fc)

    for char in founded_characters:
       if char == None:
           return False
    return True
    

password = input("Password: ")

print(is_strong_password(password))

