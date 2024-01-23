## Sumário

[1. Análise dos Dados](#c1)

[2. Arquitetura](#c2)

<br>


# <a name="c1"></a>1. Análise dos Dados
## Descrição Geral
### Objetivo
Identificar os tipos de dados fornecidos pela Integration e suas características, buscando verificar a utilidade e relevância das informações, a qualidade dos dados e compreender os tipos e formatos dos conteúdos disponíveis nas bases. Além disso, será realizada uma análise exploratória destes dados. 

### Dados Fornecidos

#### POF

A POF (Pesquisa de Orçamentos Familiares) visa principalmente mensurar as estruturas de consumo, dos gastos, dos rendimentos e parte da variação patrimonial das famílias. Possibilita traçar, portanto, um perfil das condições de vida da população brasileira a partir da análise de seus orçamentos domésticos. Além das informações diretamente associadas à estrutura orçamentária, várias características dos domicílios e das famílias são também investigadas, incluindo a autoavaliação subjetiva sobre qualidade de vida. Esta pesquisa é realizada pelo IBGE (Instituto Brasileiro de Geografia e Estatística). Nas tabelas abaixo, estão contidas respectivamente a descrição dos arquivos da POF e a descrição e justificativa das pesquisas que serão utilizadas no projeto. A análise descritiva e exploratória completa está disponível no link: [Análise Descritiva e Exploratória](https://github.com/2023M8T4Inteli/grupo4/blob/dev/document/Sprint%201/An%C3%A1lise%20descritiva%20e%20explorat%C3%B3ria.pdf)

| Pasta      | Descrição     |
|---------------|--------------|
|Dados em TXT|Esses arquivos contêm os dados brutos coletados durante a pesquisa, que podem ser utilizados para análises estatísticas e estudos relacionados aos orçamentos familiares.|
|Documentação|A documentação fornece informações detalhadas sobre a metodologia da pesquisa, a estrutura dos dados, as variáveis incluídas e outras informações relevantes para ajudar os pesquisadores a compreender e utilizar os dados.|
|Memória de Cálculo|A memória de cálculo contém informações sobre como os valores em algumas variáveis foram calculados a partir dos dados brutos. Isso é útil para entender como determinadas estatísticas ou índices foram obtidos.|
|Programas de Leitura|Esses programas são ferramentas que auxiliam na leitura e no processamento dos dados da pesquisa. Eles são úteis para quem deseja importar os dados em programas estatísticos ou de análise de dados, como o R ou o SPSS.|
|Questionários|Os questionários utilizados na pesquisa estão disponíveis nesse arquivo. Eles podem ser úteis para entender as perguntas feitas aos entrevistados e o formato das respostas.|
|Tradutores|Este arquivo contém informações sobre a tradução das tabelas de variáveis da pesquisa. Pode ser útil para compreender os nomes e as categorias das variáveis nos dados.|

Tabela 1. Estrutura dos arquivos da POF<br>
Fonte: IBGE (2023).

| PASTA | DESCRIÇÃO | JUSTIFICATIVA |
|---------------|--------------|--------------|
|Aluguel Estimado	|A tabela apresenta dados relacionados a domicílios e renda em várias unidades federativas do Brasil, incluindo informações como o número de domicílios, valores relacionados à renda, fatores de deflação e pesos associados a esses registros. Cada linha representa um domicílio específico e fornece detalhes sobre sua situação econômica. Esses dados são fundamentais para a análise e compreensão das condições financeiras das famílias em diferentes regiões do país, contribuindo para pesquisas e políticas públicas relacionadas à economia e bem-estar social.|Esta tabela oferece insights granulares sobre o potencial de consumo em diferentes regiões e canais, auxiliando na segmentação de dados para análises estatísticas. A informação pode ser crucial para entender melhor onde direcionar recursos e estratégias, sejam eles em categorias específicas ou canais de atendimento, contribuindo assim para o objetivo principal do projeto de otimizar as ações do cliente no mercado alimentar e de food service.|
|Caderneta - Coletiva	|A tabela fornece dados amostrais da pesquisa POF 2017-2018 no Brasil, com informações sobre despesas e aquisições de domicílios em diferentes unidades da federação. Os registros incluem detalhes como a unidade da federação, a situação do domicílio, valores de despesas, formas de aquisição e fatores de expansão, permitindo análises estatísticas e estudos sobre o orçamento familiar e gastos domésticos em todo o país.|A tabela fornece um conjunto abrangente de dados sobre despesas e aquisições de domicílios em diversas unidades da federação no Brasil. Ela é especialmente útil para análises estatísticas que visam compreender o orçamento familiar e os padrões de gastos em diferentes regiões do país. Isso torna a tabela uma ferramenta valiosa para qualquer estudo ou aplicação que busque insights sobre comportamento de consumo e alocação de recursos domésticos.|
|Características - Dieta|Os dados apresentados nesta tabela representam informações coletadas durante a Pesquisa de Orçamentos Familiares (POF) de 2017-2018 no Brasil. Cada linha corresponde a um domicílio específico e inclui detalhes como a localização geográfica (Unidade da Federação), o estrato da pesquisa, a situação do domicílio (urbano ou rural), códigos de identificação, hábitos alimentares, uso de suplementos, informações de saúde e renda. Esses dados fornecem uma visão abrangente das características e comportamentos das famílias brasileiras durante o período da pesquisa.|A tabela da Pesquisa de Orçamentos Familiares (POF) 2017-2018 fornece um retrato abrangente das características e comportamentos das famílias brasileiras, abrangendo aspectos como localização geográfica, estrato da pesquisa, situação do domicílio, hábitos alimentares, uso de suplementos, informações de saúde e renda. Esses dados podem ser úteis para uma variedade de aplicações, desde estudos socioeconômicos até análises de políticas públicas, permitindo uma compreensão aprofundada das necessidades, comportamentos e condições de vida dos domicílios em diferentes partes do Brasil.|

Tabela 2. Descrição e justificativa das pesquisas de aluguel estimado, caderneta-coletiva e características-dieta<br>
Fonte: Pessoal (2023).

# <a name="c2"></a>2. Arquitetura da Solução

## Introdução

Esta etapa descreve em detalhes a arquitetura da solução projetada para atender às necessidades da Integration Consultoria. O pipeline coleta e processa dados de diversas fontes, fornecendo uma saída visualizada em forma de infográfico, permitindo insights valiosos para os consultores da Integration.
<br>
A arquitetura da solução é composta por módulos que interagem entre si para realizar as tarefas solicitadas

## Desenho da Arquitetura
Abaixo é possível visualizar o desenho da arquitetura.<br>
![Arquitetura](https://github.com/2023M8T4Inteli/grupo4/blob/dev/assets/Arquitetura.png)

## Identificação de Dados
Nesta fase, segmentamos os dados em um módulo denominado "Fonte". Este módulo é responsável por receber os dados de entrada fornecidos pelo cliente, que incluem:

- Dados do Governo: Informações demográficas em formato CSV.
- Dados CNPJ: Informações sobre empresas em formato CSV.
- API do Parceiro: Dados em tempo real sobre o mercado e vendas.


## Ingestão de Dados
A etapa de Ingestão de Dados consiste em três grandes módulos: Automação e Ingestão, Preparação e Armazenamento, e Análise. A coleta de dados é realizada por meio de um processo de coleta e tratamento em Python, seguido por um processo ETL. E por fim, os dados são armazenados em um banco de dados PostgreSQL.


### Processamento de Dados
O processamento de dados envolve a limpeza, transformação e análise exploratória. A análise exploratória permite compreender as relações entre os diferentes conjuntos de dados e extrair insights que podem auxiliar na tomada de decisões.

- Coleta de dados de diferentes fontes.
- Utilização do Apache Spark, AWS EC2, AWS Lambda e Amazon S3 para processamento e armazenamento.
- Controle de acesso com base no AWS IAM.

### Justificativa

O uso do Apache Spark, AWS Lambda e Amazon S3 é fundamental para garantir a eficiência da ingestão de dados. O Apache Spark é altamente eficiente na execução de operações ETL, permitindo o processamento rápido e a transformação de grandes volumes de informações. O AWS Lambda fornece escalabilidade automática, adaptando-se às demandas variáveis de dados em tempo real. A escolha desses serviços possibilita uma ingestão de dados rápida e flexível, alinhada às necessidades da Integration Consultoria.

### Benefícios

- Processamento rápido e eficiente.
- Escalabilidade automática conforme a demanda.
- Capacidade de lidar com grandes volumes de dados.
- Manutenção de alta disponibilidade e desempenho.

## Fluxo de Dados

- Coleta, processamento e análise dos dados.
- Uso do Kafka para transferência eficiente.
- Armazenamento em PostgreSQL, OLAP e visualização no Grafana.

### Justificativa

O uso do Kafka para transferência de dados é uma escolha estratégica que torna o pipeline resiliente. Caso ocorra uma falha em qualquer parte do processo, os dados podem ser recuperados do Kafka, garantindo a integridade do fluxo de informações. Além disso, o armazenamento em PostgreSQL e OLAP fornece suporte a consultas analíticas complexas, enquanto o Grafana oferece uma interface de visualização interativa.

### Benefícios

- Resiliência e recuperação de dados.
- Armazenamento otimizado para análises avançadas.
- Visualização de dados interativa e eficaz.

## Segurança

- Controle de acesso baseado no AWS IAM.
- Isolamento e segurança com contêineres Docker.

### Justificativa

A segurança é uma prioridade. O controle de acesso com base no AWS IAM garante que apenas pessoal autorizado tenha acesso aos dados e recursos da aplicação. Além disso, o uso de contêineres Docker fornece isolamento e segurança em todo o sistema, facilitando o gerenciamento de recursos em ambientes agnósticos à nuvem.

### Benefícios

- Proteção da integridade e confidencialidade dos dados.
- Isolamento seguro de serviços.

## Escolha de Serviços

- Web Scraping, EC2 e Kafka para coleta.
- AWS S3 para armazenamento escalável.
- Apache Spark para ETL.
- PostgreSQL e OLAP para bancos de dados.
- AWS Lambda para análise.
- Grafana para visualização.

### Justificativa

A escolha de serviços AWS se baseia nas necessidades específicas do pipeline. O Web Scraping, EC2 e Kafka são selecionados para coleta eficiente e gerenciamento de filas. O AWS S3 oferece escalabilidade e confiabilidade no armazenamento de dados. O Apache Spark é ideal para operações ETL, enquanto o PostgreSQL e OLAP fornecem armazenamento e suporte a consultas analíticas. O AWS Lambda é usado para análise, e o Grafana para visualização.

### Benefícios

- Adequação de serviços às necessidades específicas.
- Confiabilidade, escalabilidade e desempenho.
- Suporte a análises complexas.

## Boas Práticas

- Redundância com múltiplas fontes de dados.
- Balanceamento de carga com contêineres Docker e gerenciamento de contêineres com Docker Compose.
- Elasticidade com Apache Spark e AWS Lambda.

### Justificativa

A implementação de boas práticas, como redundância, balanceamento de carga e elasticidade, assegura a resiliência e o desempenho do pipeline. A redundância com múltiplas fontes de dados garante a disponibilidade contínua de informações. O balanceamento de carga com contêineres Docker e o gerenciamento de contêineres com Docker Compose distribuem a carga uniformemente e isolam serviços. A elasticidade do Apache Spark e do AWS Lambda permite adaptar-se às demandas variáveis de dados em tempo real.

### Benefícios

- Resiliência e alta disponibilidade.
- Distribuição uniforme da carga de trabalho.
- Adaptabilidade às variações de demanda.

## Medidas de Segurança

- Controle de acesso com AWS IAM.

### Benefícios

- Proteção da integridade e confidencialidade dos dados.

## Conclusão

A arquitetura de ingestão de dados na AWS é resultado de um planejamento cuidadoso e da busca por soluções escaláveis, seguras e eficientes. Ao escolher serviços específicos e adotar boas práticas, a Integration Consultoria garante a qualidade e o desempenho de seu pipeline de dados.

Além disso, a implementação de medidas de segurança, como o controle de acesso baseado no AWS IAM, protege a integridade e confidencialidade dos dados. O pipeline é resiliente e escalável, capaz de enfrentar desafios em tempo real e se adaptar às necessidades da empresa.

Por fim, ao preferir o uso do Kafka e do Apache Spark, a Integration Consultoria mantém flexibilidade na migração entre provedores de serviços em nuvem, reduzindo o bloqueio a uma plataforma específica. Isso garante que o pipeline permaneça ágil e alinhado com as estratégias de negócios em constante evolução.
