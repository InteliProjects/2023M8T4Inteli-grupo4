## Sumário

[1. Análise das Fontes de Dados Disponibilizadas](#c1)

[1.1. Instituto Brasileiro de Geografia e Estatística (IBGE)](#c1)

[1.2. POF (pesquisa orçamento familiar](#c2)

[1.3. RAIS e CAGED Microdados](#c3)

[1.4. Receita Federal Dados Abertos](#c4)

[1.5. Dados Abertos MEC](#c5)

[1.6. Dados Abertos INEP](#c6)

[1.7. Open Data SUS](#c7)

[1.8. Conjunto de dados de Códigos Postais Mundiais](#c7)


# <a name="c1"></a>1. Análise das Fontes de Dados Disponibilizadas

A análise das fontes de dados é importante para compreender a origem, o formato, o tamanho e a frequência de atualização dos dados, garantindo a integridade e confiabilidade das informações utilizadas. Essa prática assegura também a um controle melhor dos resultados obtidos, evitando discrepâncias nos dados usados na ingestão, possibilitando também a otimização de processos, identificar tendências e antecipar problemas.

### <a name="c1"></a>1.1. Instituto Brasileiro de Geografia e Estatística (IBGE)

O Instituto Brasileiro de Geografia e Estatística (IBGE) disponibiliza seus dados por meio do Plano de Dados Abertos (PDA), conforme estabelecido pelo Decreto nº 8.777/2016. O PDA abrange os períodos de 2016-2017, 2018-2019 e 2020-2022. Este documento orienta a implementação e manutenção de processos institucionais para a divulgação de dados abertos, promovendo transparência. A fonte de dados abrange informações estatísticas e geoespaciais, alinhando-se a normativas como a Lei de Acesso à Informação (LAI) e a Infraestrutura Nacional de Dados Abertos (INDA). O IBGE também segue compromissos da Parceria para Governo Aberto. O PDA é um instrumento de planejamento interno, disponibilizado ao público no canal de transparência ativa, e é atualizado a cada biênio, podendo ser adaptado conforme novas diretrizes institucionais e legislações vigentes.

Os dados são disponibilizados por meio do Plano de Dados Abertos (PDA) onde os conjuntos de dados são apresentados em formatos abertos, como CSV e JSON, e são catalogados no Portal Brasileiro de Dados Abertos, seguindo os Padrões de Interoperabilidade de Governo Eletrônico (ePING) e a Cartilha Técnica para Publicação de Dados Abertos no Brasil. A frequência de atualização dos dados varia de acordo com o período estabelecido no PDA, sendo este atualizado a cada biênio, possibilitando a adaptação às novas diretrizes institucionais e legislações vigentes.


### <a name="c2"></a>1.2. Pesquisa de orçamento familiar (POF)

Pesquisa de Orçamentos Familiares (POF): A fonte de dados da Pesquisa de Orçamentos Familiares (POF) apresenta tabelas referentes à evolução dos Indicadores não Monetários de Pobreza e Qualidade de Vida no Brasil. Estas tabelas, disponíveis em formatos XLS e ODS, abrangem os períodos de 2008-2009 e 2017-2018. Importante notar que essas estatísticas são consideradas experimentais, estando em fase de teste e avaliação, exigindo cautela em sua utilização. Desenvolvidas para envolver usuários e partes interessadas, as tabelas são atualizadas a cada 5 anos ou mais.

### <a name="c3"></a>1.3. RAIS e CAGED Microdados

Os Microdados provenientes das bases RAIS e CAGED oferecem informações não identificadas do CAGED Estatístico, onde todos são disponibilizados em formato texto (.txt). Esses conjuntos de microdados, concebidos para integração em aplicativos estatísticos como SPSS, SAS ou R, são regularmente atualizados, sendo o mais recente registro de publicação datado em 16 de outubro de 2023. Ressalta-se a importância de seguir as orientações relativas à compatibilidade com o protocolo FTP. Para análises específicas dos dados da RAIS, a utilização do software R é aconselhada.


### <a name="c4"></a>1.4. Receita Federal Dados Abertos

A fonte de dados da Receita Federal disponibiliza informações sob diversas categorias, incluindo Arrecadação, Benefícios e Renúncias Fiscais, Cadastros, Carga Tributária, Comércio Exterior, Contencioso Administrativo, Convênios, Créditos Ativos, Distribuição de Renda, Fiscalização, Grandes Números do IRPF, Mercadorias Apreendidas, Órgãos e Municípios, Parcelamentos, ReceitaData, Restituição e Ressarcimento. Esses dados  são representados em formato texto e podem ser processados por máquina, sendo disponibilizados sob licença aberta que permite sua livre utilização, consumo ou cruzamento. O Plano de Dados Abertos (PDA) do Ministério da Fazenda, agora Ministério da Economia, formaliza a estratégia de divulgação, sendo a última edição aprovada para o biênio 2023-2025, apresentando 10 novos conjuntos de dados a serem abertos. O relatório final do PDA/ME para o biênio 2021-2022 destaca a abertura de 42 bases de dados.


### <a name="c5"></a>1.5. Dados Abertos MEC

A fonte de dados proveniente do Ministério da Educação disponibiliza informações sobre diversos programas educacionais no Brasil. Os conjuntos de dados estão disponíveis nos formatos CSV e XML, com conjuntos específicos abrangendo anos diferentes. Por exemplo, o conjunto Escolas com plano de atendimento aprovado no Programa Mais Educação abrange os anos de 2014 a 2019, fornecendo detalhes sobre o número de escolas, alunos, e valores recebidos. A frequência de atualização é anual. Outras fontes, como ProUni, Pronatec, e FIES, apresentam informações semelhantes, com detalhes sobre bolsas de estudo, instituições de ensino superior, e financiamento estudantil. O Pronatec, em particular, fornece atualizações mensais, bimestrais, semestrais e anuais, dependendo do conjunto de dados específico. A cobertura geográfica é nacional, e as fontes abrangem diferentes períodos, com frequência de atualização anual, semestral ou específica para determinados eventos ou processos seletivos.

O conjunto de dados Escolas com plano de atendimento aprovado no Programa Mais Educação apresenta informações sobre o número de escolas municipais e estaduais que tiveram seus planos de atendimento do Programa Mais Educação aprovados. Os dados estão disponíveis nos formatos CSV e XML, abrangendo os anos de 2014 a 2019. O conjunto fornece detalhes, como a quantidade de alunos por escola, valores totais recebidos por adesão e a cobertura geográfica inclui todos os municípios brasileiros com beneficiários do Programa Mais Educação. A frequência de atualização é anual.

A fonte de dados do Programa Universidade para Todos (ProUni) oferece informações detalhadas sobre as bolsas de estudo integrais e parciais concedidas em instituições privadas de ensino superior. Os dados, disponíveis nos formatos CSV, abrangem o período de 2010 a 2016. Eles são segmentados por região, unidade federativa, município, instituição de ensino superior, curso, modalidade de ensino, turno e tipo de bolsa. A frequência de atualização é anual.

A fonte de dados do Programa Nacional de Acesso ao Ensino Técnico e Emprego (Pronatec) fornece uma lista abrangente de instituições da Rede Federal de Educação Profissional, Científica e Tecnológica. Os dados incluem detalhes como nome, município, data de autorização de funcionamento, quantidade de matrículas, novas matrículas e concluintes por iniciativa do Pronatec. A fonte abrange os anos de 2011 a 2016, com atualizações mensais, bimestrais, semestrais e anuais, dependendo do conjunto de dados específico.

A Plataforma Nilo Peçanha (PNP) é um ambiente virtual que coleta, valida e dissemina estatísticas oficiais da Rede Federal de Educação Profissional, Científica e Tecnológica. O conjunto de dados inclui informações como microdados de matrículas, servidores e eficiência acadêmica. A cobertura temporal é até o ano de 2021, com atualizações em outubro de 2022. Os dados estão disponíveis no formato CSV.

A fonte de dados do Fundo de Financiamento Estudantil (FIES) disponibiliza informações sobre os valores das semestralidades dos cursos ofertados por mantenedoras de instituições de ensino superior. Os dados abrangem o segundo semestre de 2019, com relatórios de resultados e inscrições até 2021. A cobertura geográfica inclui todos os municípios brasileiros com instituições participantes e candidatos inscritos no FIES. A frequência de atualização é anual.

A fonte de dados do Sistema de Seleção Unificada (SISU) disponibiliza dados relacionados às inscrições realizadas nos processos seletivos do SISU no formato CSV.


### <a name="c6"></a>1.6. Dados Abertos INEP

O Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP) é uma autarquia federal brasileira que desempenha um papel central na coleta e análise de dados educacionais. Os microdados fornecidos pelo INEP são fundamentais para compreender a complexidade do sistema educacional do Brasil em seus vários níveis. Incluindo informações detalhadas sobre escolas de Educação Básica, alfabetização nas séries iniciais e aspectos da educação superior, estes dados são cruciais para análises e avaliações profundas. Eles permitem que pesquisadores e formuladores de políticas avaliem a distribuição de recursos, a qualidade do ensino e identifiquem áreas que necessitam de melhorias. Esses dados também são essenciais no desenvolvimento de políticas educacionais eficazes, orientando decisões que impactam o progresso educacional, social e econômico do país.

### <a name="c7"></a>1.7. Open Data SUS

O Ministério da Saúde disponibiliza fontes de dados por meio do OPENDATASUS Estatísticas, composta por 31 conjuntos de dados relacionados à saúde no Brasil. Dentre esses conjuntos, destacam-se o Registro de Ocupação Hospitalar COVID-19, gerenciado pela Secretaria de Atenção Especializada em Saúde (SAES), que acompanha as internações durante a pandemia. Além disso, a vigilância da Síndrome Gripal é efetuada pela Secretaria de Vigilância em Saúde e Ambiente (SVSA), com notificações disponíveis para 2020, 2021 e 2022. Outros conjuntos incluem dados sobre a Campanha Nacional de Vacinação contra Covid-19, Saúde Indígena, Hospitais e Leitos, SRAG (Síndrome Respiratória Aguda Grave) em diferentes anos, SISAGUA relacionado à água, e informações sobre Unidades Básicas de Saúde (UBS) e Cadastro Nacional de Estabelecimentos de Saúde (CNES). Os formatos dos conjuntos variam entre PDF, CSV, API, ODT e ZIP.


### <a name="c7"></a>1.8. Conjunto de dados de Códigos Postais Mundiais

A fonte de dados consiste em um banco de dados global contendo Códigos Postais de países de todo o mundo. Os conjuntos de dados representam cada país e incluem informações como Número do Código Postal, Nome do Local, Geolocalização, Precisão da Geolocalização e Código/Nome do Administrador. Os dados são disponibilizados em formato de string e podem ser acessados por meio de APIs REST ou GraphQL, permitindo fácil integração em várias aplicações. O banco de dados é licenciado sob a Creative Commons Attribution 4.0 License. Os conjuntos de dados individuais variam em tamanho, refletindo a diversidade de países incluídos. A última atualização foi registrada em 26 de fevereiro de 2020, e o serviço oferece suporte a consultas específicas, como listar Códigos Postais na Dinamarca ou contar todos os Códigos Postais na Suíça. Os desenvolvedores podem utilizar o serviço gratuitamente até 10 mil solicitações por mês e têm a flexibilidade de clonar e modificar o banco de dados conforme necessário.

