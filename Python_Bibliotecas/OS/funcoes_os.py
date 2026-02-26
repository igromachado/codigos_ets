import os

os.listdir() #lista os arquivos de um diretório
os.mkdir("Nome da pasta")# cria uma nova pasta
os.path.abspath('')# verifica o caminho do arquivo python atual
os.path.isfile("caminho do arquivo") # verifica se um arquivo existe
os.path.isdir("caminho do diretório") # verifica se uma pasta existe
os.path.join("caminho1","arquivo ou caminho 2") #Junta dois caminhos ou um caminho e o nome de um arquivo
os.rename("arquivo",novo_local) # move o arquivo de lugar