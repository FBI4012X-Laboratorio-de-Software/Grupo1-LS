# Software para Cálculo de comissões da PlenoSono Ltda.

## Execução

Para usar o programa, instale os pacotes necessários usando 'pip install -r requirements.txt' e depois execute o arquivo 'main.py'.

```bash
pip install -r requirements.txt
```

## Testes

Para execução de testes deve-se executar o test.py.

## Utilização

A partir do menu principal, são apresentadas 4 opções:
* Cadastrar Distribuidor
* Alterar Distribuidor
* Gerar Relatório
* Visualizar Distribuidor

Todos funcionam exceto alterar distribuidor.

O programa salva o csv de relatório na pasta csv e configurações devem ser definidas no arquivo `config.cfg`.

Para cadastrar um destribuidor deve-se haver um cnpj válido para adicionar com os dados do cadastrado.

A visualização do distribuidor listará os filhos de um registrado de escolha que o usúario quiser averiguar mostrando seus dados filhos, bisnetos e netos para se certificar do resultado obtido ranto no cadastro quanto no geração de relatório.

Copyright 2020 César Carpeggiani, Franco Gatelli, Rubens Onzi e Vincius Casagrande