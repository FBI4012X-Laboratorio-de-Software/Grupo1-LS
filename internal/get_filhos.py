from tratar_dados.serializacao.distribuidor_DAO import DistribuidorDAO


def get_filhos(random_entrada):

    if isinstance(random_entrada, int):
        return cpf_compare(random_entrada)
    if isinstance(random_entrada, str):
        return name_compare(random_entrada)

    return 'Não foi possível tratar a entrada, digitou corretamente?'


def cpf_compare(random_entrada):
    dist_dao = DistribuidorDAO()
    dist_list = dist_dao.load_data()

    return_list = []

    for distribuidor in dist_list:
        if distribuidor.get_cnpj() != random_entrada:
            continue

        to_read_list = [(distribuidor, 0)]

        busca_filhos_dist(to_read_list, dist_list, return_list)
        return return_list
    return []


def name_compare(random_entrada):
    dist_dao = DistribuidorDAO()
    dist_list = dist_dao.load_data()

    return_list = []

    for distribuidor in dist_list:
        if distribuidor.get_dist_nome() != random_entrada.upper():
            continue
        to_read_list = [(distribuidor, 0)]

        busca_filhos_dist(to_read_list, dist_list, return_list)
        return return_list
    return []


def busca_filhos_dist(dist_list, all_dist, return_list):

    try:
        dist_to_seek = dist_list.pop(0)
    except IndexError:
        return

    if dist_to_seek[1] == 3:
        return

    for dist in all_dist:
        if dist.get_nome_pai() == dist_to_seek[0].get_dist_nome():
            dist_list.append((dist, dist_to_seek[1] + 1))
            return_list.append(dist)

    busca_filhos_dist(dist_list, all_dist, return_list)
