from tratar_dados.serializacao.distribuidor_DAO import DistribuidorDAO
from tratar_dados.serializacao.vendas_DAO import VendasDAO
from tratar_dados.load_niveis import load_niveis_data
from estrutura_dados.distrbuidor import Distribuidor
from tratar_dados.erro_tratamento import ErroTratamento


def tratamento_registro_cadastro(*args):
    """nome, cnpj, contato, nivel, nome_pai, pecas_vendidas"""
    dist_dao = DistribuidorDAO()
    vendas_dao = VendasDAO()

    dados_vendas = vendas_dao.load_data()
    dados_dist = dist_dao.load_data()

    result = verificar_conteudo_dos_dados(dados_dist, *args)

    if type(result) == ErroTratamento:
        return result.get_msg()
    if type(result) == Distribuidor:
        dados_dist.append(result)
        vendas_dao.save_data(dados_vendas)
        dados_dist.save_data(dados_dist)

    return 'Sucesso'


def verificar_conteudo_dos_dados(
    dados_dist: list,
    *args: tuple,
):
    try:
        tratar_nome(args[0])
    except ErroTratamento as e:
        return e

    try:
        tratar_cnpj(args[1])
    except ErroTratamento as e:
        return e

    try:
        tratar_nivel(args[3])
    except ErroTratamento as e:
        return e

    try:
        tratar_nome_pai(args[4], dados_dist)
    except ErroTratamento as e:
        return e

    try:
        tratar_float(args[5])
    except ErroTratamento as e:
        return e


def tratar_nome(to_be_string) -> None:

    if not to_be_string:
        raise ErroTratamento(
            'Não foi possivel tratar o nome. Deixou em branco?'
        )

    try:
        to_be_string = str(to_be_string)
    except Exception:
        raise ErroTratamento(
            'Não foi possivel tratar o nome. Digitou Corretamente?'
        )

    to_be_string = str(to_be_string)


def tratar_cnpj(cnpj: str):

    cnpj_str = cnpj
    try:
        cnpj = int(cnpj)
    except Exception:
        raise ErroTratamento(
            'CNPJ digitado incorretamente.'
        )

    algorismos = list(cnpj_str)
    if not len(algorismos) == 14:
        raise ErroTratamento(
            'CNPJ digitado incorretamente.'
        )
    sobra = cpf_iter(algorismos, 11)
    sobra = 11 - sobra

    if sobra >= 10:
        if not int(algorismos[12]) == 0:
            raise ErroTratamento(
                'CNPJ digitado incorretamente.'
            )
        return
    if not int(algorismos[12]) == sobra:
        raise ErroTratamento(
            'CNPJ digitado incorretamente.'
        )

    sobra = cpf_iter(algorismos, 12)
    sobra = 11 - sobra

    if sobra >= 10:
        if not int(algorismos[13]) == 0:
            raise ErroTratamento(
                'CNPJ digitado incorretamente.'
            )
        return
    if not int(algorismos[13]) == sobra:
        raise ErroTratamento(
            'CNPJ digitado incorretamente.'
        )


def cpf_iter(algorismos: list, start: int):
    soma = 0
    j = 2

    for i in range(start, -1, -1):
        soma += int(algorismos[i]) * j

        j += 1
        if j == 10:
            j = 2

    return soma % 11


def tratar_nivel(nivel: str):

    if not nivel:
        raise ErroTratamento(
            'Não foi possivel tratar o nivel. Deixou em branco?'
        )

    niveis_dict = load_niveis_data()

    if not nivel.upper() in niveis_dict['NIVEL'].values():
        raise ErroTratamento(
            'Não foi possivel Encontrar o nivel inserido'
        )


def tratar_nome_pai(nome_pai: str, dados_dist):

    if not nome_pai:
        return

    nome_pai = nome_pai.upper()

    for distribuidor in dados_dist:
        if distribuidor.get_nome_pai() == nome_pai:
            return
    raise ErroTratamento(
        'Não foi possivel Encontrar o nome do pai, Digitou Corretamente'
    )


def tratar_float(to_be_float: str):

    try:
        to_be_float = float(to_be_float)
    except Exception:
        raise ErroTratamento(
            'Não foi possivel tratar o nome. Digitou Corretamente?'
        )
