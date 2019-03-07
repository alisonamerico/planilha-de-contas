# planilha-de-contas
API desenvolvida em Django e DjangoRest para administrar os gastos/ganhos de usuários.

Aplicação disponível em https://api-planilha-contas.herokuapp.com

[![codecov](https://codecov.io/gh/alisonamerico/planilha-de-contas/branch/master/graph/badge.svg)](https://codecov.io/gh/alisonamerico/planilha-de-contas)
[![Build Status](https://travis-ci.org/alisonamerico/planilha-de-contas.svg?branch=master)](https://travis-ci.org/alisonamerico/planilha-de-contas)
[![Python 3](https://pyup.io/repos/github/alisonamerico/planilha-de-contas/python-3-shield.svg)](https://pyup.io/repos/github/alisonamerico/planilha-de-contas/)
[![Updates](https://pyup.io/repos/github/alisonamerico/planilha-de-contas/shield.svg)](https://pyup.io/repos/github/alisonamerico/planilha-de-contas/)

Processos utilizados no desevolvimento do projeto:

Entrega Contínua:

 - Integração com Pipenv Travis e Pyup
 
 - Deploy Automático
 
 - Pytest: Para configurar e construir testes automatizados para o Django.
 
 - Codecov: Para cobertura de testes
 
 - python-decouple: Para desacoplar as configurações de instância da aplicação.

 

Como instalar localmente (supondo que você tenha git e python> = 3.7 instalado):
```console
git clone https://github.com/alisonamerico/planilha-de-contas
cd planilha-de-contas
cp contrib/env-sample .env
pipenv install
pipenv shell
```
Se você quiser usar o SQLite no seu ambiente de desenvolvimento, remova DATABASE_URL do arquivo .env. Caso contrário, preencha este valor com suas credenciais de banco de dados.

Você pode fazer várias migrações para gerar o esquema do banco de dados:
```console
python manage.py migrate
``` 
Você também pode criar um usuário:
```console
python manage.py createsuperuser
```
Para executar o servidor localmente (com virtualenv ativado):
```console
python manager.py runserver
```
Para executar os testes:
```console
pytest celero --cov=celero
```
