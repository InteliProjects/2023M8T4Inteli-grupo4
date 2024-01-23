## Sumário

[1. Introdução ](#c1)

[2. Data Lake](#c2)

[3. OLAP (Online Analytical Processing) e Data Warehousing](#c3) 

[4. Views e Tables no Amazon Redshift](#c4)

[5. Seleção de Serviços AWS para ETL e Armazenamento](#c5)

[6. Aspectos de Segurança, Privacidade e Conformidade](#c6)

[7. Views e Tables no Amazon Redshift](#c7)

[8. Desafios e Custos Associados ao Uso da AWS](#c8)

[9. Referências Bibliográficas](#c9)

<br>

# <a name="c1"></a>1. Introdução
  A análise de dados desempenha um papel crucial no cenário contemporâneo, impulsionando decisões informadas e estratégias fundamentadas. Nesse contexto, a estruturação eficiente e o acesso facilitado aos dados tornam-se elementos-chave para a obtenção de insights significativos. Este documento aborda uma série de conceitos e tecnologias essenciais no universo da análise de dados, proporcionando uma compreensão abrangente e aprofundada. A seguir, cada seção explora aspectos específicos, começando pelo fundamental conceito de Data Lake.


# <a name="c2"></a>2. Data Lake

&emsp;&emsp; Um Data Lake é um ambiente de armazenamento que permite a retenção de dados em sua forma bruta, sem a necessidade imediata de impor estruturação. Essa característica é particularmente valiosa, pois oferece flexibilidade para analisar dados de diversas fontes e formatos conforme necessário.
&emsp;&emsp; O conceito de "Data Lake" desempenha um papel crucial em seu projeto, proporcionando um repositório flexível e expansível para armazenar uma vasta gama de dados brutos, sejam eles estruturados ou não, em sua forma nativa. Esta abordagem oferece uma série de benefícios significativos, alinhados aos requisitos específicos do seu projeto.


## 2.2. Importância do Data Lake no Contexto do Seu Projeto

### 2.2.1. Armazenamento Versátil
  O Data Lake, notadamente utilizando o serviço S3 da AWS, se destaca por proporcionar um local versátil para armazenar dados em uma variedade de formatos, como texto, imagens e vídeos. Essa capacidade é essencial para o seu projeto, permitindo a economia de recursos ao armazenar uma ampla gama de dados de maneira eficiente.

### 2.2.2. Análise Pós-Fato
  Ao preservar dados em sua forma bruta, o Data Lake oferece uma vantagem estratégica. Isso permite que sua equipe realize análises avançadas e aprofundadas à medida que surgem novas questões ou métodos analíticos. A flexibilidade para explorar dados sem a necessidade de pré-estruturação é particularmente valiosa em um contexto dinâmico como o do seu projeto.

### 2.2.3. Integração com Ferramentas de Big Data
  A integração natural do Data Lake com ecossistemas de Big Data, como Apache Spark ou Apache Hive, fornece uma base sólida para o processamento eficiente de grandes volumes de dados. Essa sinergia contribui diretamente para a capacidade do seu projeto de lidar com análises complexas e operações em larga escala.

  Dessa forma, o Data Lake emerge como uma peça fundamental no seu ecossistema de dados, fornecendo a flexibilidade necessária para armazenar, explorar e analisar dados de maneira eficaz e adaptável às demandas em constante evolução do seu projeto.

## 2.3. Quantidade e Diversidade de Dados Armazenados

&emsp;&emsp; A gestão eficaz dos dados é fundamental para análises precisas e insights significativos. A avaliação da distribuição por buckets, quantidade de arquivos e o volume total em gigabytes armazenados no Amazon S3 proporciona uma compreensão detalhada do escopo e da complexidade. Abaixo, apresentamos uma análise abrangente de cada buckets, destacando a variedade de dados presentes em cada um.

### Buckets e Seus Conteúdos
| Bucket                                          | Quantidade de Arquivos | Tamanho Total |
|-------------------------------------------------|------------------------|---------------|
| `cnpj-integration--bigd`                         | 5                      | 4.5GB         |
| `dados-parceiro-api`                             | 3                      | 57.7MB        |
| `ibge-integration--bigd`                         | 1                      | 1.2MB         |
| `inep-integration--bigd`                         | Pastas: 1              |               |
|                                                 | Arquivos: 28           | 1.3GB         |
| `mec-integration--bigd`                          | 4                      | 18.4MB        |
| `pof-integration--bigd`                          | 11                     | 796.7MB       |
| `receita-federal-integration--bigd`              | 18                     | 37.0MB        |
| `sus-integration--bigd`                          | Pastas: 6              | 17.1GB        |
|                                                 | Arquivos: 42           |               |
| `Sistema de Informação sobre Nascidos Vivos – Sinasc/` | Arquivos: 7      | 6.4GB         |
| `Hospitais e Leitos/`                            | Arquivos: 17           | 3.8GB         |
| `Registro de Ocupação Hospitalar COVID-19/`     | Arquivos: 3            | 340MB         |
| `Sistema de Atenção à Saúde Indígena (SIASI) - Módulo de Vigilância Alimentar e Nutricional (VAN)/` | Arquivos: 1 | 23.2MB |
| `Sistema de Informação sobre Mortalidade – SIM/` | Arquivos: 11           | 4.4GB         |
| `SRAG 2021 a 2023-Banco de Dados de Síndrome Respiratória Aguda Grave-incluindo dados da COVID-19/` | Arquivos: 3 | 1.4GB |


### 2.3.1 Distribuição por Buckets
#### <i>cnpj-integration--bigd</i>
Este bucket contém dados relacionados a CNPJs, com um total de 5 arquivos e um tamanho combinado de 4.5GB. A subdivisão dos dados em cinco categorias, representadas por diferentes sub-buckets, adiciona uma camada adicional de organização.

| Bucket: *cnpj-integration--bigd*                  | Tamanho Total: *4.5GB* |
|--------------------------------------------------|-------------------------|
|   `cnpjs_1`                                     | 1.1GB                   |
|   `cnpjs_2`                                     | 1.2GB                   |
|   `cnpjs_3`                                     | 408.1MB                 |
|   `cnpjs_4`                                     | 194.6MB                 |
|   `cnpjs_5`                                     | 1.6GB                   |

#### <i>dados-parceiro-api</i>
Neste bucket, encontramos informações provenientes de uma API de parceiros, compreendendo 3 arquivos com um tamanho total de 57.7MB.
| Bucket: *dados-parceiro-api*                      | Tamanho Total: *57.7MB* |
|--------------------------------------------------|-------------------------|
|   `category.csv`                                  | 1.8KB                   |
|   `establishment.csv`                             | 50.9MB                  |
|   `sale.csv`                                      | 6.8MB                   |

#### <i>ibge-integration--bigd</i>
O bucket ibge-integration--bigd contém dados do Instituto Brasileiro de Geografia e Estatística (IBGE). Com um total de 28 arquivos e um tamanho de 1.2MB, esses dados abrangem diversas tabelas e informações populacionais.

| Bucket: *ibge-integration--bigd*                   | Tamanho Total: *1.2MB* |
|----------------------------------------------------|-------------------------|
|   `Tabela 8b.csv`                                  | 16.9KB                  |
|   `Tabela 3a.csv`                                  | 16.9KB                  |
|   `Tabela 4a.csv`                                  | 16.9KB                  |
|   `Tabela 3b.csv`                                  | 17.0KB                  |
|   `Tabela 4b.csv`                                  | 17.0KB                  |
|   `Tabela 8a.csv`                                  | 17.1KB                  |
|   `Tabela 9b.csv`                                  | 20.5KB                  |
|   `Tabela 9a.csv`                                  | 20.5KB                  |
|   `Tabela 7a.csv`                                  | 20.5KB                  |
|   `Tabela 7b.csv`                                  | 20.6KB                  |
|   `Tabela 6b.csv`                                  | 20.7KB                  |
|   `Tabela 6a.csv`                                  | 20.8KB                  |
|   `Tabela 5b.csv`                                  | 20.8KB                  |
|   `Tabela 5a.csv`                                  | 20.8KB                  |
|   `Tabela 2a.csv`                                  | 21.4KB                  |
|   `Tabela 2b.csv`                                  | 21.4KB                  |
|   `Tabela 1b.csv`                                  | 21.5KB                  |
|   `Tabela 1a.csv`                                  | 21.6KB                  |
|   `Tabela Populacao, Homens, Unidade da Federacao e municipio.csv` | 335.9KB |
|   `Tabela conjunto-dados.csv`                      | 529.8KB                 |

#### <i>inep-integration--bigd</i>
No contexto da integração com o Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), este bucket é composto por uma estrutura de pastas, contendo 28 arquivos e alcançando um tamanho total de 1.3GB. Os dados incluem informações sobre o Censo da Educação Superior e outros conjuntos relacionados.

| Bucket: *inep-integration--bigd*                                         | Tamanho Total: *1.3GB*  |
|--------------------------------------------------------------------------|---------------------------|
|   **Censo da Educação Superior/**                                        |                           |
|   MICRODADOS_CADASTRO_CURSOS_2010.csv                                  | 30.0MB                    |
|   MICRODADOS_CADASTRO_CURSOS_2011.csv                                  | 32.0MB                    |
|   MICRODADOS_CADASTRO_CURSOS_2012.csv                                  | 35.4MB                    |
|   MICRODADOS_CADASTRO_CURSOS_2013.csv                                  | 36.6MB                    |
|   MICRODADOS_CADASTRO_CURSOS_2014.csv                                  | 41.0MB                    |
|   MICRODADOS_CADASTRO_CURSOS_2014(nohead)                              | 41.0MB                    |
|   MICRODADOS_CADASTRO_CURSOS_2015.csv                                  | 45.1MB                    |
|   MICRODADOS_CADASTRO_CURSOS_2016.csv                                  | 51.4MB                    |
|   MICRODADOS_CADASTRO_CURSOS_2017.csv                                  | 65.7MB                    |
|   MICRODADOS_CADASTRO_CURSOS_2018.csv                                  | 99.2MB                    |
|   MICRODADOS_CADASTRO_CURSOS_2019.csv                                  | 136.3MB                   |
|   MICRODADOS_CADASTRO_CURSOS_2020.csv                                  | 190.7MB                   |
|   MICRODADOS_CADASTRO_CURSOS_2021.csv                                  | 245.9MB                   |
|   MICRODADOS_CADASTRO_CURSOS_2022.csv                                  | 316.8MB                   |
|   MICRODADOS_CADASTRO_IES_2010 (1).csv                                | 877.5KB                   |
|   MICRODADOS_CADASTRO_IES_2010.csv                                     | 877.5KB                   |
|   MICRODADOS_CADASTRO_IES_2011.csv                                     | 870.3KB                   |
|   MICRODADOS_CADASTRO_IES_2012.csv                                     | 888.1KB                   |
|   MICRODADOS_CADASTRO_IES_2013.csv                                     | 881.0KB                   |
|   MICRODADOS_CADASTRO_IES_2014.csv                                     | 873.7KB                   |
|   MICRODADOS_CADASTRO_IES_2015.csv                                     | 878.7KB                   |
|   MICRODADOS_CADASTRO_IES_2016.csv                                     | 894.5KB                   |
|   MICRODADOS_CADASTRO_IES_2017.csv                                     | 905.5KB                   |
|   MICRODADOS_CADASTRO_IES_2018.csv                                     | 941.3KB                   |
|   MICRODADOS_CADASTRO_IES_2019.csv                                     | 969.4KB                   |
|   MICRODADOS_CADASTRO_IES_2020.csv                                     | 920.6KB                   |
|   MICRODADOS_CADASTRO_IES_2021.csv                                     | 1.0MB                    |
|   MICRODADOS_ED_SUP_IES_2022.csv                                        | 970.1KB                   |

#### <i>mec-integration--bigd</i>
Este bucket é dedicado à integração com o Ministério da Educação (MEC), contendo 4 arquivos com um tamanho total de 18.4MB. Os dados abrangem repasses para a área de educação e participação em programas específicos.

| Bucket: *mec-integration--bigd*                                         | Tamanho Total: *18.4MB* |
|--------------------------------------------------------------------------|---------------------------|
|   pda-repasses-mais-educacao-adesao2014.csv                           | 4.9MB                     |
|   pda-repasses-mais-educacao-adesao-2017.csv                           | 714.0KB                   |
|   pda-repasses-mais-educacao-adesao-2016.csv                           | 3.5MB                     |
|   PDA_PNME_2017_2018_2019.csv                                         | 9.2MB                     |

#### <i>pof-integration--bigd</i>
Com foco em dados da Pesquisa de Orçamentos Familiares (POF), este bucket contém 11 arquivos que totalizam 796.7MB. Esses dados incluem informações sobre aluguel estimado, consumo alimentar, rendimento e outras variáveis associadas aos domicílios.

| Bucket: *pof-integration--bigd*                                        | Tamanho Total: *796.7MB* |
|--------------------------------------------------------------------------|---------------------------|
|   aluguel_estimado.csv                                               | 4.8MB                     |
|   caderneta_coletiva.csv                                             | 91.0MB                    |
|   condicoes_vida.csv                                                 | 8.3MB                     |
|   consumo_alimentar.csv                                              | 345.6MB                   |
|   despesa_individual.csv                                             | 197.1MB                   |
|   domicilio.csv                                                      | 5.9MB                     |
|   inventario.csv                                                     | 69.3MB                    |
|   morador_quali_vida.csv                                             | 38.1MB                    |
|   outros_rendimentos.csv                                             | 22.0MB                    |
|   rendimento_trabalho.csv                                            | 13.0MB                    |
|   servico_nao_monetario.csv                                          | 1.5MB                     |

#### <i>receita-federal-integration--bigd</i>
Destinado à integração com a Receita Federal, este bucket engloba 18 arquivos, totalizando 37.0MB. Os dados variam desde informações sobre repasses a análises de arrecadação.

| Bucket: *receita-federal-integration--bigd*                             | Tamanho Total: *37.0MB* |
|--------------------------------------------------------------------------|---------------------------|
|   Anexo I - FDCA e FDI - RC2023 - Apuração.csv                        | 290.4KB                   |
|   Anexo II - FDCA e FDI - RC 2023 - Valores Repassados.csv            | 405.6KB                   |
|   Anexo III - FDCA e FDI - RC2023 - Valores Não Repassados.csv        | 120.4KB                   |
|   Anexo IV - FDCA - Repasses Pendentes TODOS os Anos.csv              | 162.6KB                   |
|   Anexo Único FDCA e FDI.csv                                          | 341.0KB                   |
|   Anexo V Portaria 319_2023.csv                                       | 2.9MB                     |
|   Anexo_I_Portaria_RFB_319_2023.csv                                  | 5.7MB                     |
|   arrecadacao-cnae (1).csv                                            | 522.1KB                   |
|   arrecadacao-estado.csv                                              | 2.0MB                     |
|   arrecadacao-ir-ipi.csv                                              | 40.2KB                    |
|   arrecadacao-natureza.csv                                            | 1.2MB                     |
|   distribuicao-renda-socios-exclusiva.csv                             | 6.1MB                     |
|   distribuicao-renda-socios.csv                                       | 6.1MB                     |
|   distribuicao-renda.csv                                              | 6.1MB                     |
|   IRBI Anexo III_exclusão MOSAIC FERTILIZANTES.csv                    | 2.9MB                     |
|   IRBI Anexo IV.csv                                                   | 1.9MB                     |
|   municipios.csv                                                      | 228.7KB                   |
|   repasse-s.csv                                                       | 75.1KB                    |

#### <i>sus-integration--bigd</i>
O bucket sus-integration--bigd é vasto e diversificado, envolvendo dados cruciais para o setor de saúde. Com 6 pastas e 42 arquivos, o tamanho total atinge 17.1GB. Os subconjuntos de dados incluem informações sobre nascidos vivos, hospitais, leitos, registro de ocupação hospitalar COVID-19, saúde indígena, mortalidade e síndrome respiratória aguda grave (SRAG).
| Bucket: *sus-integration--bigd*                                       | Tamanho Total: *17.1GB* |
|------------------------------------------------------------------------|---------------------------|
|   **Sistema de Informação sobre Nascidos Vivos – Sinasc/**              |                           |
|       SINASC_2012.csv                                               | 818.0MB                   |
|       SINASC_2013.csv                                               | 893.8MB                   |
|       SINASC_2014.csv                                               | 939.1MB                   |
|       SINASC_2015.csv                                               | 952.7MB                   |
|       SINASC_2016.csv                                               | 923.2MB                   |
|       SINASC_2017.csv                                               | 928.9MB                   |
|       SINASC_2018.csv                                               | 950.0MB                   |
|   **Hospitais e Leitos/**                                               |                           |
|       Leitos_2007.csv                                               | 12.2MB                    |
|       Leitos_2008.csv                                               | 24.4MB                    |
|       Leitos_2009.csv                                               | 24.7MB                    |
|       Leitos_2010.csv                                               | 24.8MB                    |
|       Leitos_2011.csv                                               | 24.7MB                    |
|       Leitos_2012.csv                                               | 24.4MB                    |
|       Leitos_2013.csv                                               | 24.3MB                    |
|       Leitos_2014.csv                                               | 24.4MB                    |
|       Leitos_2015.csv                                               | 23.7MB                    |
|       Leitos_2016.csv                                               | 23.5MB                    |
|       Leitos_2017.csv                                               | 23.6MB                    |
|       Leitos_2018.csv                                               | 23.5MB                    |
|       Leitos_2019.csv                                               | 23.1MB                    |
|       Leitos_2020.csv                                               | 23.7MB                    |
|       Leitos_2021.csv                                               | 24.4MB                    |
|       Leitos_2022.csv                                               | 24.3MB                    |
|       Leitos_2023.csv                                               | 17.8MB                    |
|   **Registro de Ocupação Hospitalar COVID-19/**                        |                           |
|       esus-vepi.LeitoOcupacao_2020.csv                              | 119.0MB                   |
|       esus-vepi.LeitoOcupacao_2021.csv                              | 159.2MB                   |
|       esus-vepi.LeitoOcupacao_2022.csv                              | 62.7MB                    |
|   **Sistema de Atenção à Saúde Indígena (SIASI) - Módulo de Vigilância Alimentar e Nutricional (VAN)/** |                           |
|       VAN5_2022_SIASI.csv                                           | 23.2MB                    |
|   **Sistema de Informação sobre Mortalidade – SIM/**                   |                           |
|       DO23OPEN.csv                                                  | 169.0MB                   |
|       Mortalidade_Geral_2012.csv                                    | 305.5MB                   |
|       Mortalidade_Geral_2013.csv                                    | 312.1MB                   |
|       Mortalidade_Geral_2014.csv                                    | 407.4MB                   |
|       Mortalidade_Geral_2015.csv                                    | 407.5MB                   |
|       Mortalidade_Geral_2016.csv                                    | 422.1MB                   |
|       Mortalidade_Geral_2017.csv                                    | 424.9MB                   |
|       Mortalidade_Geral_2018.csv                                    | 427.8MB                   |
|       Mortalidade_Geral_2019.csv                                    | 438.6MB                   |
|       Mortalidade_Geral_2020.csv                                    | 507.3MB                   |
|       Mortalidade_Geral_2021.csv                                    | 603.4MB                   |
|   **SRAG 2021 a 2023-Banco de Dados de Síndrome Respiratória Aguda Grave-incluindo dados da COVID-19/** |                           |
|       INFLUD21-21-01-2023.csv                                        | 977.0MB                   |
|       INFLUD22-03-04-2023.csv                                        | 362.0MB                   |
|       INFLUD23-16-10-2023.csv                                        | 147.6MB                   |

A análise abrangente desses buckets destaca a riqueza e diversidade dos dados armazenados no S3, fornecendo uma visão detalhada que servirá como base essencial para futuras análises e tomadas de decisão.


# <a name="c3"></a> 3. OLAP (Online Analytical Processing) e Data Warehousing
O OLAP (Online Analytical Processing) é uma categoria de software que permite a análise eficiente de dados multidimensionais. Projetado para consultas e análises complexas, o OLAP proporciona uma visão multidimensional dos dados. Essa abordagem é essencial para entender padrões, tendências e realizar análises de dados em larga escala.

## 3.1. Definição do OLAP
No contexto do OLAP, os dados são organizados em cubos, onde cada cubo contém métricas ou medidas para análise, juntamente com dimensões que representam diferentes maneiras de visualizar os dados. As dimensões categorizam os dados, enquanto as medidas são os dados numéricos analisados, como receita, quantidade vendida e lucro.

## 3.2. Data Warehouse
  O OLAP geralmente é implementado em um ambiente de Data Warehousing. Um data warehouse é um sistema de gerenciamento de banco de dados projetado para consolidar e armazenar grandes volumes de dados de diferentes fontes em um único local centralizado.

## 3.3. Amazon Redshift

O Amazon Redshift é um serviço de data warehouse na nuvem, projetado para armazenar e analisar grandes conjuntos de dados. Ele utiliza um sistema de gerenciamento de banco de dados orientado a colunas (Column-oriented DBMS) e tecnologia de processamento paralelo massivo para gerenciar e analisar grandes volumes de dados (AMAZON WEB SERVICES, 2023).

### 3.3.1.Justificativa da Utilização  
Um ambiente OLAP  é uma solução utilizada para armazenar e consultar grandes conjuntos de dados de maneira eficiente, para fins de análise e tomada de decisão. Neste projeto, busca utilizá-lo para realizar uma análise multidimensional, ou seja, analisar os dados de múltiplas perspectivas. Por exemplo, analisar vendas por canal, categoria e região. Sendo assim, o Amazon Redshift está sendo utilizado, pois oferece suporte a recursos que facilitam a criação deste ambiente, como:

**Armazenamento Colunar**

O Redshift armazena dados em um formato colunar, o que significa que cada bloco de dados armazena valores para várias linhas em uma única coluna. Este método reduz significativamente o requisito geral de E/S (entrada/saída) de disco, uma vez que apenas as colunas necessárias para uma consulta são acessadas, diminuindo a quantidade de dados que precisam ser carregados do disco (STACK OVERFLOW, 2017; AMAZON WEB SERVICES, 2023).

**Paralelismo Massivo**

Como uma tecnologia MPP (Massively Parallel Processing) colunar, o Redshift distribui e paraleliza consultas em múltiplos nós, acelerando o processamento de consultas complexas e oferecendo desempenho rápido de consultas e E/S para praticamente qualquer tamanho de conjunto de dados (AMAZON WEB SERVICES, 2023).

**Consultas SQL**

O Redshift é baseado em ANSI SQL, o que permite executar consultas existentes com pouca ou nenhuma modificação. Isso facilita a criação de consultas analíticas complexas envolvendo várias tabelas e operações de agregação (AMAZON WEB SERVICES, 2023).

**Integração com Ferramentas de BI**

Redshift se integra facilmente com uma variedade de ferramentas de Business Intelligence (BI), como Tableau, Power BI, Looker e outras, permitindo criar painéis e relatórios interativos que ajudam na tomada de decisões baseada em dados (TO THE NEW BLOG, 2023).

**Escalabilidade**

O Redshift é altamente escalável, permitindo ajustar os recursos de acordo com as necessidades de armazenamento e processamento de dados, oferecendo eficiência de custo e segurança robusta (TO THE NEW BLOG, 2023).

## 3.4. Alternativas ao Amazon Redshift no Ambiente Azure
  No ecossistema dinâmico da computação em nuvem, várias opções competem com o Amazon Redshift. Destaco uma solução no ambiente Azure.

### 3.4.1. Azure Synapse Analytics
O Azure Synapse Analytics é um data warehouse que oferece recursos para consultas analíticas rápidas em grandes conjuntos de dados. Destacam-se vantagens como integração profunda com o ecossistema Azure, flexibilidade na escala e capacidade de análise em tempo real. Contudo, é importante considerar a complexidade do modelo de preços e a curva de aprendizado.



# <a name="c4"></a>4. Definição das Etapas de Extração, Transformação e Carga (ETL)
No contexto do projeto, as etapas de Extração, Transformação e Carga (ETL) são fundamentais para a construção de um Data Lake/Data Warehouse robusto. Embora a análise inicial tenha focado na verificação da presença dos dados em formato CSV nos buckets, é crucial estabelecer um processo mais abrangente para atender às necessidades de adequação dos dados ao modelo do Data Lake/Data Warehouse.

## 4.1 Extração (Raw Data ou Dados Brutos)
A fase de extração inicia-se com a coleta de dados brutos de diversas fontes, refletindo a diversidade e amplitude do ecossistema do projeto. Nessa etapa, os dados são obtidos sem passar por modificações significativas, preservando sua integridade e formato original. Este conjunto inicial de dados brutos representa a camada "Raw" no pipeline de dados.

## 4.2 Transformação (Worker Data ou Dados em Processamento)
Embora a análise atual tenha se concentrado na verificação da presença dos dados, a etapa de transformação é crucial para moldar os dados de acordo com as necessidades analíticas do projeto. Embora a transformação não tenha sido executada completamente nesta sprint, essa decisão estratégica permitiu à equipe aprender com os erros identificados. Na sprint 4, está planejada a recriação do script Python de tratamento, agora em formato de pacote com classes e funções para lidar efetivamente com os erros identificados na sprint 3 do Amazon Redshift. Essa abordagem iterativa proporcionará uma melhoria contínua no processo.

## 4.3 Carga (Trusted Data ou Dados Confiáveis)
A etapa final do processo, a carga, envolve a transferência dos dados processados e transformados para os buckets no Amazon S3, que servirão como a camada "Trusted" do pipeline. Embora o tratamento não tenha sido executado completamente nesta sprint, os dados nesta fase são validados e preparados para uso em análises mais profundas. Ao chegar nessa etapa, os dados, refinados e estruturados, atendem às demandas específicas do projeto. O tratamento adequado dos dados está planejado para a sprint 4, agregando a camada "Worker" ao processo.

# <a name="c5"></a>5. Seleção de Serviços AWS para ETL e Armazenamento
A seleção dos serviços AWS é um componente crítico na arquitetura de um pipeline de ETL eficiente. No projeto, a escolha de armazenar os dados no Amazon S3 é estratégica, proporcionando escalabilidade e flexibilidade para acomodar grandes volumes de dados brutos e transformados. A utilização do Amazon Redshift para a criação de tables e views adiciona uma camada de estruturação e facilita a execução de consultas analíticas complexas.

## 5.1 Amazon S3
O Amazon S3 é adotado como o local primário para armazenar os dados brutos e transformados. Sua capacidade de escalabilidade e a flexibilidade para trabalhar com dados em diversos formatos fazem dele uma escolha ideal para a camada "Raw" e "Trusted".

## 5.2 Amazon Redshift
O Amazon Redshift é utilizado para criar tables e views, proporcionando uma estrutura tabular para dados organizados e processados. Sua capacidade de processamento em paralelo e integração nativa com ferramentas de Business Intelligence (BI) o torna adequado para análises complexas e consultas eficientes.

# <a name="c6"></a> 6. Aspectos de Segurança, Privacidade e Conformidade
Considerando a importância da segurança dos dados, foi implementada uma Identity and Access Management (IAM) Role específica para o Amazon Redshift, garantindo que apenas usuários autorizados possam acessar e manipular os dados armazenados. Esta medida contribui para a proteção de dados sensíveis e está alinhada com as melhores práticas de segurança na AWS.

No entanto, é crucial continuar avaliando e implementando medidas de segurança, privacidade e conformidade, especialmente à medida que o projeto avança. O comprometimento com práticas rigorosas de segurança é essencial para garantir a integridade e confidencialidade dos dados.

# <a name="c7"></a>7. Views e Tables no Amazon Redshift

## 7.1 O que é uma View?
  Uma view é uma representação lógica de dados, definida por uma consulta SQL. Permite encapsular complexidade, ocultar detalhes desnecessários e fornecer uma interface simplificada para os usuários. No caso da POF, é possível criar views que agregam, filtram ou transformam dados específicos conforme necessário.

### 7.1.1. Views no Amazon Redshift
  Views no Amazon Redshift são consultas predefinidas armazenadas, representando subconjuntos específicos de dados ou operações complexas. Essencialmente, uma view é uma tabela virtual que não armazena os dados fisicamente, mas oferece uma perspectiva estruturada sobre os dados subjacentes. No contexto da sua utilização da Pesquisa de Orçamentos Familiares (POF) para criar uma view de teste, as views oferecem vantagens notáveis.

### 7.1.2. Importância das Views
  A importância das views no contexto analítico é multifacetada. Primeiramente, elas oferecem uma camada de abstração sobre a complexidade dos dados brutos, tornando as análises mais compreensíveis. Além disso, as views podem ser utilizadas para criar visões personalizadas dos dados, adaptadas às necessidades específicas dos usuários.

  Ao criar uma view de teste usando dados da POF, foi possível explorar como diferentes variáveis se relacionam, identificando a organização dos dados e testar hipóteses, tudo sem modificar a estrutura original dos dados.


## 7.2. O que é uma Table?
  Uma table no Amazon Redshift é uma coleção organizada de dados, seguindo um esquema definido. Cada table contém colunas que representam diferentes atributos e linhas que representam registros específicos. Ao importar dados dos seus buckets do S3 para tables no Redshift, é possível criar uma estrutura tabular que facilita consultas e análises.

### 7.2.1. Tables no Amazon Redshift
  As tables no Amazon Redshift são estruturas fundamentais que armazenam dados de maneira organizada. Elas podem ser alimentadas diretamente a partir de buckets do Amazon S3, consolidando dados brutos em um formato acessível para consultas analíticas. No caso, ao criar um banco de dados da API do parceiro e outro com todos os buckets, entender as tables é crucial.

### 7.2.2. Importância das Tables
  As tables formam a base do seu ambiente de dados no Amazon Redshift. Elas oferecem uma estrutura organizada para armazenar grandes volumes de dados, permitindo consultas eficientes. Além disso, as tables são altamente escaláveis, suportando o crescimento contínuo dos dados ao longo do tempo.

  Ao criar um banco de dados da API do parceiro e consolidar todos os buckets em tables, podemos centralizar dados de diferentes fontes, facilitando a análise holística e a obtenção de insights abrangentes.

# <a name="c8"></a> 8. Desafios e Custos Associados ao Uso da AWS

Este documento explora os desafios e custos associados ao uso da Amazon Web Services (AWS) no projeto de Big Data da Integration Consulting, destacando as complexidades e considerações financeiras envolvidas no desenvolvimento de um pipeline de dados avançado.

## 8.2 Visão Geral da AWS e Seu Impacto no Projeto

### 8.2.1 Descrição Geral da AWS
A AWS oferece uma gama de serviços como S3 para armazenamento de dados, AWS Glue e AWS Lambda para processamento e preparação de dados, EMR, Apache Spark e Apache Hadoop para análise de dados, e AWS QuickSight para visualização de dados. Esses serviços são cruciais para o manuseio eficiente de Big Data.

### 8.2.3 Importância para o Projeto
Cada um desses serviços desempenha um papel vital no pipeline de Big Data, desde a ingestão de dados até a análise e visualização, facilitando insights profundos e suporte à tomada de decisão para nosso cliente.

## 8.3 Desafios e Dificuldades Associados à AWS

### 8.3.1 Verificação de Conta AWS
O processo de verificação de conta na AWS pode levar até 24 horas, o que pode atrasar o início dos trabalhos. Este fator deve ser considerado no planejamento do projeto.

### 8.3.2 Complexidade Técnica
A configuração e integração dos diversos serviços da AWS podem ser tecnicamente desafiadoras, exigindo um alto nível de expertise e experiência.

### 5.3.3 Gerenciamento de Dados Grandes
O manuseio de grandes volumes de dados, especialmente no AWS Redshift, apresenta desafios em termos de performance, escalabilidade e custo.

## 8.4 Custo e Orçamento

### 8.4.1 Free Trial de 300 dólares
O trial gratuito da AWS oferece até 300 dólares, o que pode ser um recurso valioso nas fases iniciais do projeto para testar e prototipar soluções sem custo adicional.

### 8.4.2 Custos por Requisição no AWS Redshift
A estrutura de custos do AWS Redshift é baseada em cada requisição, o que pode acumular custos significativos dependendo do volume de dados processados e consultas realizadas.

### 8.4.3 Orçamento e Planejamento Financeiro
É crucial planejar o orçamento com antecedência, levando em consideração os custos variáveis associados aos serviços da AWS e alocando recursos de forma eficiente.

## 8.5 Estratégias de Mitigação

### 8.5.1 Otimização de Custos
Recomendações para reduzir custos incluem a escolha do plano de serviço adequado, monitoramento contínuo do uso dos serviços e desativação de recursos não utilizados.

### 8.5.2 Gestão de Dados e Recursos
Uma gestão eficiente dos dados e dos recursos da AWS pode ajudar a minimizar custos e otimizar o desempenho, especialmente em projetos de Big Data.

## 8.6 Conclusão
Este projeto enfrenta uma série de desafios técnicos e financeiros no uso da AWS, mas com planejamento cuidadoso e estratégias de otimização, esses obstáculos podem ser superados. As lições aprendidas aqui não apenas facilitarão a execução eficiente deste projeto, mas também servirão como referência valiosa para iniciativas futuras envolvendo tecnologias avançadas de Big Data na nuvem


# <a name="c9"></a>9. Referências Bibliográficas

AMAZON WEB SERVICES, INC. **What is Amazon Redshift?**. Disponível em: https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html. Acesso em: 26 nov. 2023.

STACK OVERFLOW. **Columnar database queries in Amazon Redshift**. Disponível em: https://stackoverflow.com/questions/45176680/columnar-database-queries-in-amazon-redshift. Acesso em: 26 nov. 2023.

AMAZON WEB SERVICES, INC. **Columnar storage**. In: *Amazon Redshift*. Disponível em: https://docs.aws.amazon.com/redshift/latest/dg/c_columnar_storage_disk_mem_mgmnt.html. Acesso em: 26 nov. 2023.

AMAZON WEB SERVICES, INC. **Amazon Redshift deep dive - Data Warehousing on AWS**. Disponível em: https://docs.aws.amazon.com/redshift/latest/dg/welcome.html. Acesso em: 26 nov. 2023.

AMAZON WEB SERVICES, INC. **Amazon Redshift - Big Data Analytics Options on AWS**. Disponível em: https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html. Acesso em: 26 nov. 2023.

TO THE NEW BLOG. **Amazon Redshift: A Comprehensive Overview**. Disponível em: https://www.tothenew.com/blog/amazon-redshift-a-comprehensive-overview/. Acesso em: 26 nov. 2023.

