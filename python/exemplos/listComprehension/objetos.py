import sys
import os
#

if len(sys.argv) != 2:
    print('usage:python nome.py nome_dir')
    sys.exit(1)
print(f'qde parametro:{len(sys.argv)}')
print(sys.argv)
#print(dir(sys))
arquivos = os.listdir(sys.argv[1])
print(arquivos)

#criando  a lista
arq_logs = [nome for nome in arquivos if nome.endswith('.log')]
