# Importando a biblioteca para manipulação de arquivos
import os

# a função join() retorna o caminho de diretórios da forma correta de cada sistema operacional
vpath = os.path.join('theory', 'script')
print(vpath)

# a função join() também pode retornar um caminho acrescentando um arquivo
# OS ARQUIVOS NÃO SERÃO CRIADOS
my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(os.path.join('theory', 'script', filename))

# a função getcwd() retorna o diretório atual de trabalho
print(os.getcwd())

# a função chdir() modifica o diretório pelo caminho fornecido
# os.chdir('./theory/script')
# print(os.getcwd())

# a função makedirs() cria uma diretório no caminho fornecido
# os.makedirs('./theory/script/using_makedirs')

# outra forma de mostrar o caminho absoluto
print(os.path.abspath('.'))

# obtendo tamanho dos arquivos com getsize()
os.chdir('./' + vpath)
for file in os.listdir(os.getcwd()):
    print(os.path.getsize(file))

# verificando se um path existe com exists()
print(os.path.exists('/home/pedro/Example'))

# verificando se o path informado é um arquivo com isfile()
print(os.path.isfile(os.getcwd() + "/understanding_regex.py"))

# verificando se o path informado é um diretório com isdir()
print(os.path.isdir(os.getcwd()))
