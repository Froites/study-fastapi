# Estudo de FastAPI

Bem-vindo ao repositório de estudo sobre o FastAPI! Este projeto foi desenvolvido como parte do meu Plano de Desenvolvimento Individual (PDI), com foco no desenvolvimento em Python, utilizando o framework FastAPI. Durante um período de quatro semanas, estudei e desenvolvi uma aplicação com FastAPI, incluindo a implementação de testes automatizados utilizando o Pytest.

## Ferramentas Utilizadas

### Poetry
O Poetry é uma ferramenta de gerenciamento de dependências e ambientes virtuais para Python. Ele simplifica a instalação de pacotes e o gerenciamento do ambiente virtual do projeto.

### FastAPI
O FastAPI é um framework web moderno e de alto desempenho, baseado em funções, que facilita a criação de APIs RESTful. Com apenas um decorador, é possível tornar uma função acessível via rede.

### Pytest
O Pytest é um framework de testes que permite a criação de testes automatizados de forma simples e eficiente. Segue as fases de desenvolvimento de testes:

- **Organizar (Arrange):** Monta o ambiente necessário para a execução do teste.
- **Agir (Act):** Executa o código de produção que está sendo testado.
- **Afirmar (Assert):** Verifica se o comportamento observado corresponde ao esperado.

### Pydantic
O Pydantic é utilizado para a validação e serialização de dados. Ele garante que os dados recebidos e enviados pela API estejam no formato correto, utilizando schemas e tipos de dados específicos, como o `EmailStr`.

### SQLAlchemy
O SQLAlchemy é uma biblioteca de ORM (Mapeamento Objeto-Relacional) que facilita a comunicação entre o código orientado a objetos e bancos de dados relacionais. Para este projeto, utilizei o SQLite como banco de dados.

### Taskipy
O [Taskipy](https://github.com/taskipy/taskipy) é um executor de tarefas (*task runner*) que facilita a execução de comandos definidos no `pyproject.toml`.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `app/`: Contém a aplicação FastAPI.
  - `main.py`: Arquivo principal da aplicação.
  - `models.py`: Definição dos modelos de dados utilizando SQLAlchemy.
  - `schemas.py`: Definição dos schemas de dados utilizando Pydantic.
  - `database.py`: Configuração do banco de dados.
  - `tests/`: Contém os testes automatizados com Pytest.
  
- `pyproject.toml`: Arquivo de configuração do projeto.

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/froites/study-fastapi.git
