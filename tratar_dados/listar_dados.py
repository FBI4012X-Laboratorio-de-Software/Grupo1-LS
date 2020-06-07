import pickle
import os

def order_by_date(id_dist, start_date, end_date):
    
    dates_list = []
    arquivos = []

    arq_path = ''
    arq = ''
    
    dist_path = "C:\PLENOSONO\CAIXA DISTRIBUIDORES\"

    dist_path = dist_path + id_dist

    caminhos = [os.path.join(dist_path, nome) for nome in  os.listdir(dist_path)]

    for i in caminhos.nome:
        
        if i > start_date and i < end_date:

            dates_list.append(date(i))
            
    dates_list = dates_list.sorted()

    for i in dates_list:

        arq_path = dist_path + i

        if os.path.exists(arq_path):
            
            arq = open(arq_path, "r")
            arquivos.append(cPickle.load(arq))
            
    arq.close

    return arquivos