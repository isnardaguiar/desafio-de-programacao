O objetivo desse projeto é processar um arquivo do tipo .tab e salvar seus dados em um banco de dados relacional.

## Configuração

1. **Instalação do PostgreSQL:**
   - Certifique-se que o PostgreSQL se encontra instalado em seu computador e configurado. Crie um novo banco de dados para o bom funcionamento deste projeto. A criação das tabelas será feita a partir da execução de uma função do Django, que criará as tabelas de acordo com as models presentes nos arquivos `model.py`
2. **Instalação do Python**
   - Este projeto utiliza o framework Django da linguagem Python. Certifique-se de que o Python se encontra instalado em seu computador. A versão utilizada para a criação deste projeto foi a 3.8.10
3. **Instalação e configuração do ambiente virtual**
   - Este passo não é obrigatório mas é recomendado que seja instalado o pacote do Python chamado `virtualenv` para a execução do projeto. Dessa forma, é possível instalar as depêndencias apenas dentro do ambiente virtual de forma que fiquem isoladas de outros pacotes do Python. O pacote pode ser instalado executando o seguinte comando em um terminal:
     ```bash
     pip3 install virtualenv
     ```

     Mais informações podem ser obtidas na [documentação do virtual env](https://virtualenv.pypa.io/en/latest/index.html)
    - Após a instalação, navegue para este diretório e execute o seguinte comando para criar um ambiente virtual
      ```bash
      virtualenv venv
      ```
      Se não tiver ocorrido nenhum erro, o diretório `venv` irá ter sido criado
   - Ative o ambiente virtual executando o seguinte comando no mesmo diretório em que foi executado o último comando
     ```bash
     source venv/bin/activate   # No Windows, use 'venv\Scripts\activate'
     ```

4. **Instalação de Dependências:**
   - Instale as dependências do projeto:
     ```bash
     pip install -r requirements.txt
     ```

5. **Configuração do Arquivo .env:**
   - Crie um arquivo `.env` e adicione as variáveis de ambiente necessárias, como as configurações do banco de dados PostgreSQL:
     ```env
     DB_NAME=seu_banco_de_dados
     DB_USER=seu_usuario
     DB_PASSWORD=sua_senha
     DB_HOST=localhost
     DB_PORT=5432
     ```

     Para a facilitar a criação do arquivo `.env`, pode ser duplicado o arquivo `.env-example` e modificar o nome para `.env`. Após isso, altere as variáveis de acordo com as credenciais do seu banco de dados.
## Utilização
1. **Migrations**
   - O Django utiliza um sistema de migrações para controlar e aplicar alterações no esquema do banco de dados de forma automatizada. Essas migrações são arquivos Python que contêm as instruções necessárias para realizar alterações no banco de dados, como criar tabelas, adicionar ou remover colunas, entre outras.

        Ao executar o comando:
        ```bash
        python manage.py migrate
        ```
     As tabelas necessárias serão criadas em seu banco de dados. Algumas dessas tabelas são de configuração do Django. A tabela que utilizaremos é a sales_salesdata, que conterá os dados de venda presentes no arquivo a ser processado.
2. **Execução do Projeto:**
   - Com o ambiente virtual ativado e as migrations aplicadas, execute o seguinte comando:
     ```bash
     python manage.py runserver
     ```

    - Com o servidor ativo, acesse em seu navegador o link
    `localhost:8000/sales/upload/`
    
    - Ao acessar, uma página com instruções será exibida e para utilizar o projeto, basta realizar o upload de uma arquivo do tipo `.tab`. Um exemplo funcional e outro para testar o erro podem ser encontrados na raiz desse projeto.
3. **Testando o projeto:**
   -  Para testar a aplicação, foi escolhido o runner pytest. Os testes se encontram nos diretórios [`application/tests`](application/tests) e [`sales/tests`](sales/tests)
   -  Ao instalar as dependências, o pytest será instalado e basta executar o seguinte comando neste diretório para que os testes automatizados sejam realizados:
      ```bash
      pytest
      ```