# Documentação do Pacote de Tratamento e Carga  de dados Públicos na AWS S3

## Visão Geral

Este pacote oferece funcionalidades para realizar tratamento superficial de dados e carregar os resultados para um bucket na AWS S3. O módulo incluído possibilita a manipulação de dados nulos, a conversão dos dados para um formato tabular específico e a renomeação de colunas para melhor entendimento.

## Funcionalidades

- **Tratamento de Nulos**: Limpeza e imputação de valores em campos nulos para manter a integridade dos dados.
- **Conversão de Estrutura**: Transformação dos dados para um formato de tabela padronizado, facilitando operações subsequentes de análise e processamento.
- **Renomeação de Colunas**: Atualização dos nomes das colunas para termos mais descritivos, visando uma visualização e compreensão mais clara dos dados.

## Uso

Após aplicar o tratamento de dados e enviar para a AWS S3, utilize a função `load_s3` da classe, preenchendo os parâmetros necessários. A função realizará o upload dos dados tratados para o bucket especificado na AWS S3.

### Pré-Requisitos

- Dados de entrada devem estar em um formato CSV para que a classe possa processar.
- Credenciais de acesso à AWS devem estar configuradas corretamente.

### Funções

#### `tratar_nulos(self)`

Realiza a limpeza de campos nulos nos dados, utilizando a estratégia de imputação definida.

#### `converter_arquivo(self, type)`

Converte o arquivo de dados para o formato de tabela especifica. O parâmetro `type`, esta sendo utilizando para criar uma coluna que descreva a origem dos dados, facilitando a futura união de tabelas e permitindo diferenciá-las, se necessário.

#### `substituicao_nomenclaturas(self, dicionario_de_substituicao)`

Para renomear as colunas dos dados, aplique um dicionário de substituição. Para usar essa função, simplesmente insira como argumento o dicionário a ser utilizado para a renomeação, que geralmente tem o mesmo nome da tabela. Este pode ser facilmente encontrado no arquivo localizado no mesmo diretório, chamado 'dic_pof'.


#### `load_s3(self, bucket_name, object_name, aws_access_key_id, aws_secret_access_key, token)`

Carrega os dados tratados para um bucket na AWS S3. Requer todos os parâmetros necessários para autenticação e especificação do destino dos dados.


# Documentação do Pacote de Tratamento e Carga da API do Parceiro na AWS S3

## Visão Geral

Este pacote foi desenvolvido para integrar dados provenientes da API do Parceiro, tratá-los e carregá-los em um bucket da AWS S3. A funcionalidade principal é facilitar a automação do processo de extração de dados, seu tratamento preliminar e o armazenamento na nuvem, permitindo que usuários e sistemas downstream acessem os dados prontos para uso.

## Funcionalidades

- **Consulta à API**: Permite a realização de consultas programáticas à API do Parceiro, obtendo dados recentes e relevantes.
- **Tratamento de Dados**: Aplica um conjunto de procedimentos para garantir que os dados estejam limpos e estruturados corretamente antes do carregamento.
- **Carga no S3**: Facilita o envio dos dados tratados para um bucket específico na AWS S3, tornando-os acessíveis para análise e aplicativos.

## Uso

O fluxo típico de uso deste pacote envolve a chamada da função de consulta à API do Parceiro, o tratamento dos dados recebidos e o subsequente carregamento no S3. 

### Pré-Requisitos

- É necessário possuir as credenciais de acesso API do Parceiro.
- As credenciais da AWS também devem estar configuradas para permitir o acesso ao serviço S3.

### Funções

#### `consulta_api(self, endpoint, parametros)`

Realiza uma requisição GET ao endpoint especificado da API do Parceiro, utilizando os parâmetros fornecidos. Retorna os dados em formato JSON.

#### `tratar_dados(self, dados_json)`

Recebe os dados em formato JSON, aplica o tratamento necessário e os converte para um DataFrame do pandas, preparando-os para o carregamento no S3.

#### `carregar_s3(self, bucket_name, object_name, dados_dataframe)`

Carrega o DataFrame tratado no bucket da AWS S3 especificado, utilizando o nome do objeto fornecido para o arquivo resultante.

#### `executar_carga(self)`

Orquestra o processo de consulta à API, tratamento dos dados e carga no S3. Esta função chama internamente as funções `consulta_api`, `tratar_dados` e `carregar_s3`.

## Exemplo de Uso

```python
# Instanciando a classe
api_parceiro = ConexaoAPIParceiro(api_key, secret_key, token)

# Executando a carga completa
api_parceiro.executar_carga()