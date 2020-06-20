from openpyxl import load_workbook
import os
from configparser import RawConfigParser

def gera_comissao():

    config = RawConfigParser()
    config.read('.config.cfg')
    csv_folder = config['comissoes']['comissoes_path'].split(',')
    file_list = csv_folder
    for file in file_list:
        wb = load_workbook(filename=file)
        sheet_ranges = wb['range names']
        print(sheet_ranges['D18'].value)

def atualiza_os_csvs():

    config = RawConfigParser()
    config.read('.config.cfg')
    file_list = config['comissoes']['comissoes_path'].split(',')

    for file in file_list:

        df = pd.read_excel(file, sheet_name=None)
        file_name = f'{config["comissoes"]["sheet"]}_{file}'
        zie_file_name = os.path.join('csv', file_name.split('.')[0] + '.csv')
        df[config['comissoes']['sheet']].to_csv(zie_file_name)

    return file_list

if __name__ == "__main__":
    gera_comissao()