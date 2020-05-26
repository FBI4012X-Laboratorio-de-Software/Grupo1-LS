import pandas as pd


class Excellent():

    _total = 0.0
    _data = ''
    _numpedido = 0

    def __init__(self, caminho):
        planilha = pd.read_excel(caminho)
        linha_pagar = planilha.loc[planilha['Unnamed: 7'].isin(['A PAGAR', 'a pagar'])]
        linha_num_data = planilha.loc[planilha['Unnamed: 7'].isin(['DATA'])]
        self._numpedido  = linha_num_data.values[0][5]
        self._data       = linha_num_data.values[0][8]
        self._total      = linha_pagar.values[0][-1]  # -1 traz o ultimo elemento da lista       


pedido = Excellent('pedido.xlsx')

print(pedido._numpedido)
print(pedido._total)
print(pedido._data)

