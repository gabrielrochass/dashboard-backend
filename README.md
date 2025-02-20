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

