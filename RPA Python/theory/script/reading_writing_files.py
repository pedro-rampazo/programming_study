import os
import shelve
import pprint

# alterando diretório
txt_files = os.path.join('theory', 'txt')
os.chdir('./' + txt_files)

# abrindo arquivo .txt e lendo conteúdo
file = open('reading_writing_files.txt', 'r')
print(file.read())
file.close()

# retorna uma lista contendo as linhas do arquivo .txt
file = open('reading_writing_files[2].txt', 'r')
print(file.readlines())
file.close()

# escrevendo em arquivos de texto, o argumento 'w' sobrescreve o conteúdo existente
file = open('reading_writing_files.txt', 'w')
file.write('Testing write() function')
file = open('reading_writing_files.txt', 'r')
print(file.read())
file.close()

# escrevendo em arquivos de texto, o argumento 'a' adiciona ao conteúdo existente
file = open('reading_writing_files.txt', 'a')
file.write('\nTesting write() function with "a" parameter')
file = open('reading_writing_files.txt', 'r')
print(file.read())

# salvando variáveis com o módulo Shelve
shelf_file = shelve.open('reading_writing_files[3]')
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cats'] = cats
shelf_file.close()

# abrindo variáveis com o módulo Shelve
shelf_file = shelve.open('reading_writing_files[3]')
print(type(shelf_file))
print(list(shelf_file.keys()))
print(shelf_file['cats'])
shelf_file.close()

# armazenando coleção de dicionário em um arquivo Python para uso futuro
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))
file = open('reading_writing_files[4].py', 'w')
file.write('cats=' + pprint.pformat(cats) + '\n')
file.close()

