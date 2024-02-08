import os
import pandas as pd
import glob

print("ABC")
def consolidate_excels(input_folder,output_folder,output_file_name):
    """
        Consolida todos os arquivos do Excel num unico arquivo
    """
    #Garantir que a pasta de saída exista
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    #lista de arquivos Excel na pasta input_folder
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))

    #Lendos todos os arquivos de Excel em uma lista de Dataframes pandas
    all = [pd.read_excel(file,engine='openpyxl') for file in files]

    #Concatenando todos os DataFrame em un 
    consolidated_df = pd.concat(all, axis = 0, ignore_index=True)




