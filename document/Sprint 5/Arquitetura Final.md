# Arquitetura Final

![Arquitetura Final](https://github.com/2023M8T4Inteli/grupo4/blob/main/document/Sprint%205/Arquitetura%20Final.md) <br>
Figura 01: Arquitetura final do projeto  <br>
Fonte: Elaboração própria

A arquitetura final para a solução Big Data possui cinco etapas, iniciando com a captação de dados de diferentes fontes. Em seguida, automatiza e direciona os dados para processamento e armazenamento em AWS S3, com destaque para a remoção de dados sensíveis. Posteriormente, a análise dos dados por meio de scripts Python e o encaminhamento para criação de gráficos usando Metabase, permitindo a geração de infográficos. Cada etapa é descrita a seguir:

## 1. Fonte dos Dados

Foram mapeadas três fontes principais de dados, dando início ao processo:

- Dados Públicos (CSV)
- Dados de CNPJ (CSV)
- Dados provenientes da API do parceiro de projeto

Esta é a etapa para a identificação das origens dos dados a serem processados e analisados.

## 2. Automatização e Ingestão dos Dados

Ferramentas Utilizadas:

- AWS IAM: Fornece autenticação e controle de acesso.
- Python (Script com Docker): Automatiza a ingestão dos dados.

Nesta etapa, a automação e a correta ingestão dos dados são asseguradas por meio da autenticação com AWS IAM, restringindo o acesso aos analistas de dados autorizados, e as abordagens variam de acordo com a fonte dos dados:

- Dados Públicos e de CNPJ: São direcionados para um script Python executado em um ambiente Docker, encaminhando-os para um pacote específico.
- Dados da API do parceiro de projeto: São processados por um script Python separado, também utilizando um ambiente Docker específico para a construção de um arquivo (CSV).

## 3. Preparação e Armazenamento dos Dados

Ferramentas Utilizadas:

- AWS S3 (Data Lake): Armazenamento escalável e durável.
- AWS Redshift: Armazenamento relacional para processamento de dados.
- Docker: Ambientes de execução isolados.

Os dados são recebidos e armazenados no Data Lake (AWS S3). Destaca-se que os dados da API do parceiro de projeto passam por um processo de expurgo para remover informações sensíveis. Em seguida, os dados são direcionados ao Redshift Relacional da AWS, onde são processados e permitem a criação de Views. Todo o processo ocorre em um ambiente Docker, garantindo segurança e isolamento.

## 4. Análise dos Dados

Ferramentas Utilizadas:

- Python (Script Ensemble): Coleta e processamento de informações.
- Kafka: Pilha de mensageria para transferência de dados em tempo real.

Nesta fase, um script em Python de método ensemble coleta e processa as informações provenientes das etapas anteriores. Os dados são então encaminhados para uma pilha de mensageria utilizando o serviço Kafka, garantindo a transferência em tempo real para análise.

## 5. Criação de Infográficos

Ferramentas Utilizadas:

- Metabase: Ferramenta de criação de gráficos e visualizações.
- IAM (AWS): Controle de acesso gerenciado da AWS.

Nesta última etapa, a ferramenta Metabase é utilizada para criar gráficos e visualizações baseados nas informações processadas anteriormente. Adicionalmente, um componente dedicado à criação de infográficos, associado à autenticação IAM específica para analistas de marketing e vendas, utiliza os gráficos gerados para a composição de infográficos informativos.

## 6. Principais Diferenças

Enquanto a arquitetura final faz uso do Redshift Relacional da AWS e Metabase, a primeira versão utiliza Apache Spark, PostgreSQL, Grafana e AWS Lambda para processamento, armazenamento e análise.

Na arquitetura final, a análise é realizada via script Python e o serviço Kafka é utilizado para mensageria, enquanto na primeira versão, análises estatísticas e tendências são feitas via AWS Lambda e os infográficos são criados diretamente no Grafana.
