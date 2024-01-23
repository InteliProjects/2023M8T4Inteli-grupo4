# Script - API Parceiro
## Descrição
A API do Parceiro possui dados fictícios de um cliente, envolvendo informações de vendas, categorias de produtos e CNPJs de empresas. Abaixo são descritas as tabelas:

1. `Categoria`: Contém informações sobre diferentes categorias de produtos, como chocolates, cerveja, vinho, arroz, etc. Cada categoria tem um ID, um status de atividade (ativo ou não), e um nome. Exemplo:
   
2. `Venda`: Registra detalhes das vendas, incluindo a quantidade vendida, a categoria do produto, o CNPJ da empresa que realizou a venda, um ID de venda, um ID de categoria, a data da venda e o valor da venda.

3. `CNPJ`: Lista CNPJs de empresas junto com um ID associado.

O script desenvolvido envolve o consumo dos dados da API e o envio para um bucket no AWS S3.

## Documentação API 
Base URL da API: ...

Métodos Aceitos: Apenas GET

Token de uso: ...

### Parâmetros de consulta (query parameters) disponíveis:

- **code**: Carregará consigo o token de autenticação para que a requisição possa ser feita. É obrigatório que esse código (ou token) seja informado como um query parameter para que a chamada seja feita.
- **table**: Informa à API para qual tabela da base de dados será feita a chamada HTTP Get. Existem 3 possíveis tabelas: Category, Establishment e Sale.
  
**OBS**: O parâmetro table pode ser enviado em minúsculo ou maiúsculo. Mas o nome da tabela deve ser exatamente um dos 3 citados acima.

- **saleDate (opcional)**: Parâmetro de filtro por data de venda. Retorna todos os registros da tabela Sale na data informada. Deve ser informada no padrão yyyy-MM-dd (ex.: 2023-09-23).
- **saleCnpj (opcional)**: Parâmetro de filtro por CNPJ. Retorna todos os registros da tabela Sale vinculados àquele CNPJ. Deve ser um CNPJ válido.
- **saleCategory (opcional)**: Parâmetro de filtro por Nome de Categoria. Retorna todos os registros da tabela Sale vinculados àquela Categoria. Deve ser um nome válido de categoria.

### Exceptions: O código no momento está preparado para 4 tipos de Exceção, sendo elas:

1. Parâmetros faltando

      a. Mensagem de erro: No source table was provided in the query parameters. Make sure to send the 'table' query param, followed by one of the three valid source tables (Category, Sale or Establishment).

      b. Motivo: Não foi enviada uma tabela alvo da requisição. Certifique-se que antes ou após do query param “code”, seja enviado também o parâmetro table. Ex.: table=category irá listar os registros da tabela Category.

2. Parâmetros desconhecidos
   
      a. Mensagem de erro: Please inform a valid source table. Valid source tables are: Category, Sale and Establishment. The informed source table was: {}

      b. Motivo: Foi enviada uma tabela que não foi identificada na base de dados, muito provavelmente por erro de digitação. Ex.: table=categoryy (y a mais).

3. CNPJ Inválido
   
      a. Mensagem de erro: Invalid CNPJ. Provided CNPJ was: {}

      b. Motivo: Foi enviado um CNPJ que não consta na base de dados.

4. Categoria Inválida 

      a. Mensagem de erro: Invalid category. Provided category was: {}

      b. Motivo: Foi enviada uma categoria que não consta na base de dados.

## Documentação Script

No notebook `Script_Api_Parceiro` ocorre a conexão com a API do Parceiro, manipulação dos dados recebidos e armazenamento no S3. Abaixo há uma descrição das seções do notebook:

1. `Importações e Instalação de Pacotes`: é realizada as importações de pacotes necessários e a instalação do boto3, um SDK do Python para AWS, que permite a interação com serviços da AWS, como o S3.

2. Função `recuperar_dados`: esta função é responsável por recuperar dados da API. Ela aceita um nome das tabelsa como argumento e faz uma solicitação GET para URL da API, passando um código de acesso e o nome da tabela como parâmetros.
   
4. Função `transformar_csv`: esta função converte dados JSON em formato CSV. Ela cria uma lista para as linhas do CSV, adicionando uma linha por item no JSON. Os dados são escritos em um arquivo CSV usando as funcionalidades de escrita de arquivo do Python.

5. Função `iniciar_api_parceiro`: esta função atua como um controlador para o processo de ETL. Ela define uma lista de tabelas e os respectivos nomes de arquivos CSV de saída. Para cada tabela, ela chama a função recuperar_dados para obter os dados JSON e em seguida usa a função transformar_csv para escrever esses dados em um arquivo CSV.

6. `Envio de Dados para o AWS S3`: esta seção estabelece uma conexão com o serviço Amazon S3 usando as credenciais da AWS. Em seguida, o código itera sobre os arquivos CSV em um diretório local, fazendo o upload de cada arquivo para um bucket do S3. Cada arquivo é enviado com uma chave correspondente ao seu nome.
