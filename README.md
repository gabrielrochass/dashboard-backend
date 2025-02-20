# Dashboard Backend

## Criando um Ambiente Virtual

Criar um ambiente virtual significa isolar as dependências do seu projeto Python em um diretório separado, garantindo que bibliotecas e pacotes não entrem em conflito com outros projetos ou com pacotes globais do seu sistema.

### Vantagens de Usar um Ambiente Virtual

- ✅ **Evitar Conflitos:** Evita conflitos entre versões de pacotes.
- ✅ **Organização:** Mantém o projeto mais organizado.
- ✅ **Reprodutibilidade:** Garante que outros desenvolvedores possam instalar as mesmas dependências sem problemas.

### Como Criar um Ambiente Virtual

1. **Criar o Ambiente Virtual:**
    ```bash
    python -m venv nome_do_ambiente
    ```
2. **Ativar o Ambiente Virtual:**
    - No Windows:
      ```bash
      nome_do_ambiente\Scripts\activate
      ```
    - No macOS/Linux:
      ```bash
      source nome_do_ambiente/bin/activate
      ```
3. **Instalar Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## Comparação entre Ambiente Virtual e Docker

### Semelhanças

- ✅ **Isolamento:** Ambos isolam dependências para evitar conflitos.
- ✅ **Reprodutibilidade:** Permitem que o código rode de forma previsível em diferentes máquinas.
- ✅ **Facilitam o Desenvolvimento:** Criam um ambiente configurado especificamente para um projeto.

### Diferenças

| Recurso                | Ambiente Virtual (venv)                       | Docker                                      |
|------------------------|-----------------------------------------------|---------------------------------------------|
| **O que isola?**       | Pacotes e dependências do Python.             | Todo o sistema operacional (incluindo Python, banco de dados, etc.). |
| **Nível de Isolamento**| Apenas bibliotecas Python dentro do mesmo SO. | Isolamento total do sistema, podendo rodar em qualquer máquina. |
| **Reprodutibilidade**  | Funciona apenas se a versão do Python for compatível. | Garante que o ambiente será idêntico, independentemente do SO. |
| **Leveza**             | Mais leve, pois só gerencia pacotes.          | Mais pesado, pois cria containers completos. |
| **Execução**           | Depende do Python já instalado no sistema.    | Não precisa de nada além do Docker para rodar. |
| **Uso Principal**      | Projetos Python locais.                       | Ambientes completos para rodar aplicações em produção. |

## Quando Usar um ou Outro?

- 🟢 **Ambiente Virtual (venv):** Use quando você só precisa isolar as bibliotecas Python dentro de um projeto. Ideal para desenvolvimento local, rodando scripts e pequenos projetos.
- 🟢 **Docker:** Use quando você precisa isolar todo o ambiente, incluindo banco de dados, servidores, e dependências do sistema operacional. Útil para garantir que a aplicação rode exatamente igual em qualquer máquina.


## Criando um Projeto Django

Para iniciar um novo projeto Django, você pode usar o comando `django-admin startproject`. Este comando cria a estrutura básica de diretórios e arquivos necessários para um projeto Django.

### Como Criar um Projeto Django

1. **Criar o Projeto:**
    ```bash
    django-admin startproject backend
    ```
    Isso criará um diretório chamado `backend` contendo a estrutura inicial do projeto Django.

2. **Estrutura do Projeto:**
    Após executar o comando, a estrutura do projeto será semelhante a esta:
    ```
    backend/
        manage.py
        backend/
            __init__.py
            settings.py
            urls.py
            wsgi.py
    ```

3. **Executar o Servidor de Desenvolvimento:**
    Navegue até o diretório do projeto e execute o servidor de desenvolvimento:
    ```bash
    cd backend
    python manage.py runserver
    ```
    O servidor estará disponível em `http://127.0.0.1:8000/`.


## Melhorias Finais

### Adicionar CORS Headers

Para permitir requisições do frontend, adicione CORS headers ao seu projeto Django.

1. **Instalar o pacote `django-cors-headers`:**
    ```bash
    pip install django-cors-headers
    ```

2. **Configurar o `settings.py`:**
    ```python
    INSTALLED_APPS += ['corsheaders']
    MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",  # React Frontend
    ]
    ```

### Criar Seeds para Popular o Banco

Para popular o banco de dados com dados iniciais, crie um script de seed.

1. **Criar o script `core/management/commands/popular_db.py`:**
    ```python
    from django.core.management.base import BaseCommand
    from core.models import Categoria, Produto

    class Command(BaseCommand):
        def handle(self, *args, **kwargs):
            categorias = ["Eletrônicos", "Roupas", "Alimentos"]
            for cat in categorias:
                Categoria.objects.get_or_create(nome=cat)

            produtos = [
                {"nome": "Celular", "preco": 1500, "categoria": "Eletrônicos"},
                {"nome": "Camisa", "preco": 50, "categoria": "Roupas"},
                {"nome": "Pizza", "preco": 30, "categoria": "Alimentos"},
            ]
            
            for prod in produtos:
                categoria = Categoria.objects.get(nome=prod["categoria"])
                Produto.objects.get_or_create(nome=prod["nome"], preco=prod["preco"], categoria=categoria)

            self.stdout.write(self.style.SUCCESS("Banco populado com sucesso!"))
    ```

2. **Executar o script de seed:**
    ```bash
    python manage.py populate_db
    ```
    ## Estrutura do Projeto

    Aqui está uma visão geral das pastas e arquivos do projeto e suas funções:

    - **backend/**: Diretório principal do projeto Django.
        - **manage.py**: Script de linha de comando para interagir com o projeto Django.
        - **backend/**: Diretório contendo a configuração do projeto.
            - **__init__.py**: Arquivo que indica que este diretório deve ser tratado como um pacote Python.
            - **settings.py**: Arquivo de configuração do projeto Django.
            - **urls.py**: Arquivo de roteamento de URLs do projeto.
            - **wsgi.py**: Ponto de entrada para servidores web compatíveis com WSGI para servir o projeto.

    - **core/**: Diretório para a aplicação principal do projeto.
        - **models.py**: Definição dos modelos de dados.
        - **views.py**: Definição das views que controlam a lógica de apresentação.
        - **urls.py**: Roteamento de URLs específicas da aplicação.
        - **admin.py**: Configurações do Django admin para os modelos.
        - **migrations/**: Diretório que contém as migrações do banco de dados.

    - **requirements.txt**: Arquivo que lista todas as dependências do projeto.

    - **README.md**: Documentação do projeto.

    - **.gitignore**: Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git.

    - **Dockerfile**: Arquivo de configuração para criar uma imagem Docker do projeto.

    - **docker-compose.yml**: Arquivo de configuração para definir e executar serviços Docker.

    - **venv/**: Diretório do ambiente virtual Python (não deve ser incluído no controle de versão).

    - **static/**: Diretório para arquivos estáticos (CSS, JavaScript, imagens).

    - **templates/**: Diretório para templates HTML.

    - **media/**: Diretório para arquivos de mídia carregados pelos usuários.

    - **logs/**: Diretório para arquivos de log.

    - **scripts/**: Diretório para scripts auxiliares e utilitários.

    - **tests/**: Diretório para testes automatizados.

    - **docs/**: Diretório para documentação adicional do projeto.

