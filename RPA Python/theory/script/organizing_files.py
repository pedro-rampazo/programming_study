# a biblioteca shutil permite copiar, mover e excluir diretórios e arquivos
import shutil
import os

# a função copy() vai duplicar o arquivo especificado no primeito argumento (origem)
# até o segundo argumento (destino) 
# Pode ser acrescentado o nome do arquivo caso seja necessário a mudança na cópia
shutil.copy('organizing_files.txt', '../theory/script')

# função copytree() vai copiar um diretório inteiro, contendo seus arquivos até o destino
shutil.copytree('./organizing_files', './theory/script')

# função move() vai mover o arquivo para o diretório-destino
# Pode ser especificado o nome do arquivo ao mover
shutil.move('./organizing_files/organizing_files.txt', './theory/script')

# a função unlink itá apagar o arquivo dado pelo path no argumento
os.unlink('./organizing_files/organizing_files.txt')

# a função rmdir() irá apagar o diretório especificado
# o diretório deve estar vazio para funcionar
os.rmdir('./organizing_files/')

# a função rmtree() removerá o diretório e seus arquivos ali contidos
shutil.rmtree('./organizing_files/')

