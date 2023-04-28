import shutil
import os

# Pasta de Origem
path = r'Y:\02-CLIENTES\HCA\DIGITALIZAÇÃO\999-PDF-A PARA PROCESSAR\FEITO\INCLUIDOS EM MIDIA'
origin = os.listdir(path)

# Pasta de destino
destiny = r'W:\HCA\HCA_P_B'

folders = ['134430102', '134430432', '134430472', '134430622', '134430697', '134430735',
           '134431104', '134431145', '134431233', '134431431', '34431518', '134431702',
           '134357433', '134431473', '134431610']

for folder in origin:

    if folder in folders:

    # listening comprehension
     x = [item for item in os.listdir(path + "\\" + folder) if item.endswith('.pdf')]
     y = [valor for valor in x if "meta_A3b" not in valor]

     print()
