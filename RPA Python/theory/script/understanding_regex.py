# Importando o módulo do Regex
import re 

# Criando um modelo de expressão regular
# '\d' significa um dígito
phoneNumberRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") # re.compile(r"\d{3}-\d{3}-\d{4}") 

# Objeto regex por correspondência
mo = phoneNumberRegex.search("My number is 415-555-4242")
print("Phone number found: " + mo.group())

# Objeto regex por correspondência de vários grupos, encontra o primeira correspondência
heroRegex = re.compile(f"Batman|Tina Fey")
mo1 = heroRegex.search("Batman and Tina Fey.")
# Encontra todas as correspondências
mo2 = heroRegex.findall("Batman and Tina Fey.")
print(mo1.group())
print(mo2)

# Objeto Regex por correspondência, com prefixo estabelecido
batRegex = re.compile(f"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())

# Objeto Regex por correspondência, independente das variações
batRegex = re.compile(f"Bat(wo)?man")
mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group())
mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group())

# Objeto Regex por correspondência, correspondendo a zero ou mais
batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group())
mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group())
mo3 = batRegex.search("The adventures of Batwowowoman")
print(mo3.group())

# Objeto Regex por correspondência, correspondendo a um ou mais
batRegex = re.compile(r"Bat(wo)+man")
mo1 = batRegex.search("The Adventures of Batwoman")
print(mo1.group())
mo2 = batRegex.search("The Adventures of Batwowowoman")
print(mo2.group())

# Objeto Regex por correspondência usando chaves
haRegex = re.compile(r"(Ha){3}")
mo1 = haRegex.search("HaHaHa")
print(mo1.group())

# Regex Greedy e Nongreedy
# Greedy: sempre exibira a correspondência máxima
greedyHaRegex = re.compile(r"(Ha){3,5}")
mo1 = greedyHaRegex.search("HaHaHaHaHa")
print(mo1.group())
# NonGreedy: sempre exibirá a correspondência mínima
nongreedyHaRegex = re.compile(r"(Ha){3,5}?")
mo2 = nongreedyHaRegex.search("HaHaHaHaHa")
print(mo2.group())

# CLASSE DE CARACTERES
# '\d' -> Qualquer dígito entre 0 e 9
# '\D' -> Qualquer dígito que não esteja entre 0 e 9 
# '\w' -> Qualquer letra, dígito ou o underscore
# '\W' -> Qualquer caractere que não seja letra, dígito ou underscore
# '\s' -> Qualquer espaço, tabulação ou caracter de quebra de linha
# '\S' -> Qualquer caracter que não seja espaço, tabulação ou caracter de quebra de linha

# Criando a própria classe Regex
vowelRegex = re.compile(f'[aeiouAEIOU]')
mo1 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo1)
