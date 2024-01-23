## Sumário

[1. Persona](#c1)

[2. Mapa de Jornada do Usuário](#c2)

[3. User Story](#c3)

<br>


# <a name="c1"></a>1. Persona
As personas são representações detalhadas, porém fictícias, dos clientes ideais que a solução busca atender, além de ocupar um papel crucial ao compreender e orientar projetos e soluções. Tendo em vista nosso atual projeto, que envolve o desenvolvimento de uma consultoria de marketing e vendas baseada em Big Data, criamos dois diferentes tipos de personas  para facilitar a compreensão, de forma visual, dos usuários que utilizarão nossa solução: a gerente de Marketing e Vendas e o Analista de Dados.

Essas personas são criadas com base nos setores-chave que garantem a eficácia da solução. Onde, cada uma delas contém características, comportamentos e preferências alinhados com o contexto da Integration. Além de ajudar a equipe a visualizar os usuários finais, essas personas também são utilizadas para definir estratégias e recursos que atendam às carências e expectativas de cada perfil.


![Persona 1](https://github.com/2023M8T4Inteli/grupo4/blob/dev/assets/Persona_Gerente_Marketing_Vendas.jpg) <br>
Figura 01: Persona - Gerente Marketing e Vendas  <br>
Fonte: Elaboração própria

![Persona 2](https://github.com/2023M8T4Inteli/grupo4/blob/dev/assets/Persona_Analista.jpg) <br>
Figura 02: Persona - Analista de Dados  <br>
Fonte: Elaboração própria
# <a name="c2"></a>2. Mapa de Jornada do Usuário
Para melhor ilustrar as etapas do relacionamento do usuário com um produto ou uma solução, abordando a experiência antes, durante e após o seu uso, em relação a um cenário específico. A dinâmica do usuário com a solução é importante para registrar a interação do usuário ao longo do tempo, identificando pontos integrados na narrativa, permitindo a compreensão dessa interação, destacando os pontos de atenção.

Duas jornadas foram elaboradas, para cada persona, a fim de contextualizar os eventos que ocorrem desde o recebimento da solicitação, descrita no cenário, até o momento em que desempenham suas funções.

![Persona 1](https://github.com/2023M8T4Inteli/grupo4/blob/dev/assets/Jornada_Usuario_Marketing_Vendas.jpg) <br>
Figura 3: Jornada do usuário de Ana Mercadante <br>
Fonte: Autoria própria

![Persona 2](https://github.com/2023M8T4Inteli/grupo4/blob/dev/assets/Jornada_Usuario_Desenvolvimento.jpg) <br>
Figura 4: Jornada do usuário de Vinicius Monteiro <br>
Fonte: Autoria própria

# <a name="c3"></a>3. User Story

## User Story 1: Configuração de Ambiente AWS pela Equipe de TI

**Persona:** Equipe de TI

**História:** Como membro da equipe de TI, desejo configurar o ambiente AWS e seus componentes, a fim de estabelecer a infraestrutura para armazenar, processar e manter os dados do projeto de maneira segura e eficiente.

**Critério de avaliação: Configuração da Infraestrutura AWS**

- **1.1 Condição de Aceite**: A infraestrutura da AWS está configurada e pronta para uso.
- **1.2 Condição de Recusa**: A infraestrutura da AWS não está configurada ou não está pronta para uso.

<i>Teste de Aceitação - Critério 1: Configuração de Ambiente AWS</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** A infraestrutura AWS foi configurada com todos os componentes funcionando conforme esperado, e a equipe de TI pode acessar e utilizar o ambiente para processar e armazenar dados.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: Problemas críticos na configuração da infraestrutura AWS, como falhas de implementação, configurações incorretas ou incapacidade de acessar o ambiente AWS.
  

<i>Teste de Aceitação - Critério 2: Verificação de Acesso ao Ambiente AWS</i>
- **2.1 {Aceito}**
  - **Explicação do Aceito:** A equipe de TI pode acessar o ambiente AWS com as credenciais fornecidas e realizar ações básicas, como listar serviços disponíveis.
- **2.2 {Recusado}**
  - **Explicação do Recusado:** A equipe de TI não consegue acessar o ambiente AWS com as credenciais fornecidas ou enfrenta dificuldades técnicas que impedem o acesso

<i>Teste de Aceitação - Critério 3: Funcionamento dos Componentes Essenciais</i>

- **3.1 {Aceito}**
  - **Explicação do Aceito:** Todos os componentes essenciais, como servidores, bancos de dados e serviços de armazenamento, estão funcionando conforme esperado.
- **3.2 {Recusado}**
  - **Explicação do Recusado:** Alguns dos componentes essenciais estão com problemas ou não estão funcionando conforme esperado

<i>Teste de Aceitação - Critério 4: Teste de Resiliência e Redundância</i>
- **4.1 {Aceito}**
  - **Explicação do Aceito:** A infraestrutura AWS passou em testes de resiliência e redundância, garantindo a disponibilidade contínua dos serviços.
- **4.2 {Recusado}**
  - **Explicação do Recusado:** A infraestrutura AWS não passou nos testes de resiliência e redundância, demonstrando vulnerabilidades na disponibilidade dos serviços.

**Notas :** Esta user story é o primeiro passo para as demais user stories, especialmente a User Story 2 (Ingestão de Dados no Datalake com Ênfase na Segurança).


| **Prioridade** | **Estimativa** | **Relação** |
|----------|----------|----------|
| Alta | 4 dias | N/A |


<br><br>

## User Story 2: Ingestão de Dados no Datalake com Ênfase na Segurança

**Persona:** Analista de Dados

**História:** Como equipe de Dados,  desejo realizar a ingestão de dados no datalake da AWS S3, com foco na segurança e controle de acesso, para garantir a integridade dos dados, a confidencialidade das informações e a segregação dos dados sensíveis.

**Critério de avaliação:** Ingestão de dados no Datalake

- **1.1 Condição de Aceite**: Os dados foram corretamente ingetados no datalake AWS S3 com medidas de segurança adequadas, incluindo confidencialidade, integridade e controle de acesso.
- **1.2 Condição de Recusa**: A ingestão de dados não foi realizada de forma segura, ou as medidas de segurança, confidencialidade e controle de acesso não foram aplicadas conforme necessário, ou houve risco de exposição de dados sensíveis.

<i>Teste de Aceitação - Critério 1: Ingestão de Dados no Datalake </i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** Os dados foram ingetados mantendo a integridade dos mesmos, com medidas de segurança aplicadas, e o acesso é controlado, no datalake AWS S3.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: Problemas críticos na ingestão de dados, como dados incorretos, perda de integridade ou falta de medidas de segurança adequadas, confidencialidade ou controle de acesso.
  
<i>Teste de Aceitação - Critério 2: Confidencialidade de Dados</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** Os dados foram ingetados com confidencialidade no datalake AWS S3, garantindo que informações sensíveis não sejam acessíveis sem autorização adequada.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: Os dados foram ingetados sem confidencialidade, com risco de exposição de informações sensíveis.
  
<i>Teste de Aceitação - Critério 3: Controle de Acesso ao Docker e VPC</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** O Docker e a infraestrutura de acesso ao datalake foram configurados dentro de uma VPC (Virtual Private Cloud) com acesso controlado, garantindo que somente usuários autorizados tenham acesso aos dados.
- **1.2 {Recusado}**
  - **Explicação do Recusado**:  O Docker e a infraestrutura não foram configurados dentro de uma VPC, colocando em risco a segurança e a confidencialidade dos dados, permitindo acesso não autorizado.

**Notas:** Esta história se concentra na ingestão de dados iniciais para testes.


| **Prioridade** | **Estimativa** | **Relação** |
|----------|----------|----------|
| Alta | 14 dias | User Story 1 |


<br><br>

## User story 3 - Análise Inicial dos Dados

**Persona:** Analista de Dados

**História:** Como analista de dados desejo realizar uma análise inicial dos dados no datalake recém-ingestado, a fim de compreender a qualidade e relevância dos dados para as futuras análises.

**Critério de avaliação:** Análise Inicial dos Dados


- **1.1 Condição de Aceite**:  O analista de dados concluiu a análise inicial, documentando a qualidade dos dados com métricas de integridade, precisão, consistência, e sua relevância para as futuras análises.
- **1.2 Condição de Recusa**: Problemas críticos na análise dos dados, falta de documentação da qualidade dos dados ou falta de relevância dos dados para análises futuras.

<i>Teste de Aceitação - Critério 1: Análise de Qualidade dos Dados </i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** A análise inicial dos dados foi documentada com métricas de qualidade dos dados, incluindo integridade, precisão e consistência.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: Problemas críticos na análise de qualidade dos dados, como métricas inaceitáveis de integridade, precisão ou consistência.
  
  <i>Teste de Aceitação - Critério 2:Relevância dos Dados para Análises Futuras </i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** Os dados analisados foram considerados relevantes para análises futuras, com base na documentação da equipe de Análise de Dados.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: Os dados analisados não são relevantes para análises futuras, conforme documentado pela equipe de Análise de Dados.
  
  <i>Teste de Aceitação - Critério 3: Documentação da Análise</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** A análise inicial dos dados foi devidamente documentada, incluindo as métricas de qualidade dos dados, sua quantidade e a avaliação de relevância para análises futuras do projeto.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: Falta de documentação adequada da análise inicial dos dados, dificultando a avaliação de qualidade e relevância.
  
**Notas :** Esta história se concentra na análise estatística inicial dos dados para identificação de tendências.


| **Prioridade** | **Estimativa** | **Relação** |
|----------|----------|----------|
| Média | 7 dias | User Story 1 -  User Story 2 - |


<br><br>

## User Story 4 - Análise e Visualização Preliminar de Dados Governamentais e de CNPJ no Datalake para Identificar Necessidades de Tratamento ETL

**Persona:** Analista de Dados

**História:** Como analista de dados, desejo implementar uma visualização que permita a análise preliminar de todos os dados já recebidos no datalake, incluindo dados governamentais e de CNPJ, a fim de identificar a necessidade de tratamento ETL.

**Critério de avaliação:** Análise e Visualização Preliminar de Dados

- **1.1 Condição de Aceite**: A visualização preliminar foi implementada no datalake, permitindo a análise de todos os dados já recebidos, identificando as necessidades de tratamento ETL.
- **1.2 Condição de Recusa**: Problemas críticos na implementação da visualização preliminar que não permitam a análise dos dados ou a identificação das necessidades de tratamento ETL.

<i>Teste de Aceitação - Critério 1: Implementação da Visualização Preliminar de Dados </i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** A visualização preliminar foi implementada conforme especificado, permitindo a análise de todos os dados já recebidos no datalake.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: Problemas críticos na implementação da visualização preliminar impedem a análise dos dados.
  
  <i>Teste de Aceitação - Critério 2: Identificação de Necessidades de Tratamento ETL</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** A análise preliminar dos dados identificou as necessidades de tratamento ETL, conforme necessário.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: A análise preliminar não foi capaz de identificar adequadamente as necessidades de tratamento ETL devido a problemas na implementação.
  
  <i>Teste de Aceitação - Critério 3: Insights Iniciais para Relações de Dados</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** A análise preliminar dos dados forneceu insights iniciais sobre como os dados podem ser relacionados para calcular as métricas desejadas, como quantidade de vendas por tempo, quantidade de domicílio por região e quantidade de consumo por região/tempo.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: Falta de insights iniciais sobre a relação entre os dados devido a problemas na implementação da visualização preliminar.
  
**Notas:** Queremos obter insights iniciais para compreender como esses dados podem ser relacionados para calcular métricas como quantidade de vendas por tempo, quantidade de domicílio por região e quantidade de consumo por região/tempo, conforme requisitado pelo cliente.


| **Prioridade** | **Estimativa** | **Relação** |
|----------|----------|----------|
| Média | 9 dias | User Story 1 - User Story 2 - User Story 3 |

<br><br>


## User Story 5 - Importação de Dados Governamentais no Datalake via Pacote Python

**Persona:** Analista de Dados

**História:** Como analista de dados, desejo implementar um processo de importação de dados governamentais no datalake usando um pacote Python para enriquecer nossos dados com fontes governamentais.

**Critério de avaliação:** 

- **1.1 Condição de Aceite**:  O processo de importação de dados governamentais foi implementado e os dados governamentais estão disponíveis no datalake.
- **1.2 Condição de Recusa**: Problemas críticos na implementação do processo ou indisponibilidade dos dados governamentais no datalake.

<i>Teste de Aceitação - Critério 1: Implementação do Processo de Importação de Dados Governamentais</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** O processo de importação de dados governamentais foi implementado e os dados estão disponíveis no datalake.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: Problemas críticos na implementação do processo e/ou falta de disponibilidade dos dados governamentais no datalake.
  
  <i>Teste de Aceitação - Critério 2: Qualidade dos Dados Importados</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** Os dados governamentais importados mantêm a qualidade e integridade necessárias para uso nas análises de dados.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: Os dados importados apresentam problemas críticos de qualidade ou integridade, tornando-os inadequados para análise.
  
**Notas:** O critério de tempo ainda será adicionado com o que deve ser esperado como resposta, visto que o time ainda não sabe qual o tempo adequado de resposta do processamento dos dados dentro de um Datalake AWS S3. 

| **Prioridade** | **Estimativa** | **Relação** |
|----------|----------|----------|
| Alta | 14 dias | User Story 1 - User Story 2 - User Sotry 3|

<br><br>

## User Story 6 - Implementação de Filtros para o Cubo de Dados

**Título:** 

**Persona:** Analista de Dados

**História:** Como analista de dados, desejo implementar filtros para o cubo de dados, proporcionando aos usuários a capacidade de refinar e personalizar a visualização de dados de acordo com suas necessidades.

**Critério de avaliação:** 

- **1.1 Condição de Aceite**: Os filtros foram implementados corretamente, permitindo que os usuários refinem a visualização de dados de acordo com suas necessidades de forma prática e eficiente.
- **1.2 Condição de Recusa**: Problemas críticos na implementação dos filtros e/ou falta de funcionalidade esperada

<i>Teste de Aceitação - Critério 1: Implementação dos Filtros no Cubo de Dados</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** Os filtros foram implementados corretamente e oferecem uma experiência positiva aos usuários. Os usuários podem refinar a visualização de dados com facilidade e eficiência, atendendo às suas necessidades.
- **1.1.2 {Aceitação Adicional}**
  - Critério de Aceitação Adicional: O analista de dados consegue aplicar filtros de forma intuitiva utilizando SQL e retornando os resultados da filtragem precisos e a performance da aplicação não é prejudicada.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: Problemas críticos na implementação dos filtros e/ou falta de funcionalidade esperada. Os filtros não funcionam conforme o esperado, o analista têm dificuldade em usá-los ou a performance da aplicação é prejudicada.
  
**Notas:** A implementação de filtros visa melhorar a usabilidade e a capacidade de personalização da visualização de dados no cubo. Os filtros devem ser intuitivos, eficazes e não devem prejudicar a performance da aplicação. O sucesso da implementação é determinado pela capacidade dos usuários de refinar a visualização de dados de acordo com suas necessidades de forma prática e eficiente.

| **Prioridade** | **Estimativa** | **Relação** |
|----------|----------|----------|
| Alta | 7 dias | User Story 1 - User Story 4 - User Story 5|



<br><br>


## User story 7 - Plataforma de Visualização com Infográfico

**Persona:** Analista de Dados

**História:** Como analista de dados, desejo criar uma plataforma de visualização que inclui um infográfico, desenvolvida no Grafana, para apresentar os dados coletados no cubo de dados de forma acessível e informativa para o Analista de Marketing e Vendas, que pode não possuir letramento digital.

**Critério de avaliação:** Plataforma de Visualização Criada

- **Condição de Aceite**: A plataforma de visualização foi desenvolvida com êxito e inclui o infográfico com os dados apropriados.
- **1.2 Condição de Recusa**: Problemas críticos no desenvolvimento da plataforma e/ou falta do infográfico esperado.

<i>Teste de Aceitação - Critério 1: Desenvolvimento da Plataforma de Visualização</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** A plataforma de visualização foi desenvolvida conforme especificado e inclui o infográfico com dados relevantes. O Analista de Marketing e Vendas é capaz de acessar e compreender facilmente as informações apresentadas, mesmo que não tenha letramento digital.
- **1.1.2 {Aceitação Adicional}**
  - **Explicação do Aceito Adicional:** A plataforma deve ser acessível por um público não tecnicamente qualificado, e o infográfico deve comunicar efetivamente as informações do cubo de dados de maneira informativa.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: Problemas críticos no desenvolvimento da plataforma ou falta do infográfico esperado. A plataforma não foi desenvolvida conforme as especificações ou o infográfico não atende às necessidades do Analista de Marketing e Vendas.
  
  <i>Teste de Aceitação - Critério 2: Acessibilidade para Usuários Não Tecnicamente Qualificados</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** A plataforma é acessível e compreensível para usuários não tecnicamente qualificados, como o Analista de Marketing e Vendas. A interface e o infográfico são intuitivos e fáceis de usar.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: A plataforma não é acessível ou compreensível para usuários não tecnicamente qualificados. O Analista de Marketing e Vendas enfrenta dificuldades ao utilizar a plataforma ou ao interpretar o infográfico.
  
  <i>Teste de Aceitação - Critério 3: Compreensão dos Dados pelo Infográfico</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** O infográfico comunica as informações do cubo de dados de forma informativa. O Analista de Marketing e Vendas consegue entender facilmente os dados apresentados.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: O infográfico não comunica as informações do cubo de dados e/ou não permite que o Analista de Marketing e Vendas compreenda os dados apresentados.
  
**Notas :** 

| **Prioridade** | **Estimativa** | **Relação** |
|----------|----------|----------|
| Alta | N+T (Quantidade de trabalho + Tempo) - Necessário ver com a Integration | User Story 6|
<br><br>

## User story 8 - Acesso Restrito para o Analista de Marketing e Vendas

**Persona:** Analista de Marketing e Vendas

**História:** Como Analista de Marketing e Vendas, desejo que meu acesso à plataforma de visualização seja restrito, permitindo-me apenas visualizar o infográfico. Isso garantirá que não possa criar ou acessar o cubo de dados ou análises estatísticas feitas no Ensemble.

**Critério de avaliação:** Acesso Restrito à Plataforma de Visualização

- **1.1 Condição de Aceite**: O Analista de Marketing e Vendas não tem permissão para criar ou acessar o cubo de dados ou análises estatísticas avançadas.
- **1.2 Condição de Recusa**: O Analista de Marketing e Vendas tem acesso irrestrito à plataforma.

  <i>Teste de Aceitação - Critério 1:  Verificação de Acesso Restrito</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** O Analista de Marketing e Vendas não tem permissão para criar e/ou acessar o cubo de dados e/ou análises estatísticas avançadas, tendo acesso somente à visualização do infográfico.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: O Analista de Marketing e Vendas possui acesso irrestrito, permitindo a criação e/ou acesso ao cubo de dados e/ou análises estatísticas avançadas.


**Notas :** 

| **Prioridade** | **Estimativa** | **Relação** |
|----------|----------|----------|
|  Alta |  7 dias | N/A |

<br><br>

## User story 9 - Visualização de Variáveis para Análise do Analista de Marketing e Vendas
**Persona:** Analista de Marketing e Vendas

**História:** Como Analista de Marketing e Vendas, desejo ter a capacidade de visualizar todas as variáveis disponíveis no cubo de dados, incluindo quantidade de vendas por tempo, quantidade de domicílio por região e quantidade de consumo por região/tempo, para que eu possa cruzá-las de acordo com as necessidades da análise.

**Critério de avaliação:** Visualização de Variáveis que estão contidas no Cubo de Dados

- **1.1 Condição de Aceite**: O Analista de Marketing e Vendas consegue visualizar todas as variáveis disponíveis no cubo de dados, incluindo quantidade de vendas por tempo, quantidade de domicílio por região e quantidade de consumo por região/tempo.
- **1.2 Condição de Recusa**:  O Analista de Marketing e Vendas não consegue visualizar todas as variáveis e/ou enfrenta problemas críticos na visualização.

  <i>Teste de Aceitação - Critério 1: Verificação de Visualização de Variáveis no Cubo de Dados</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** O Analista de Marketing e Vendas consegue ver as variáveis disponíveis para cruzamento de forma clara e acessível na plataforma de visualização do Grafana.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: O Analista de Marketing e Vendas não consegue identificar as variáveis disponíveis para cruzamento e/ou a apresentação das variáveis não está clara na plataforma.
  
**Notas:** 

| **Prioridade** | **Estimativa** | **Relação** |
|----------|----------|----------|
|  Alta | 7 dias  | User Sotry 8|

<br><br>

## User story 10 - Tempo de Resposta Rápido para a Aplicação
**Persona:** Analista de Marketing e Vendas

**História:** Como Analista de Marketing e Vendas, desejo que a aplicação tenha um tempo de resposta rápido para que eu possa realizar análises de dados de forma eficiente.

**Critério de avaliação:** 

- **1.1 Condição de Aceite**: A aplicação responde de forma quase instantânea às solicitações do Analista de Marketing e Vendas, garantindo que análises de dados possam ser realizadas de maneira eficiente e sem atrasos perceptíveis.
- **1.2 Condição de Recusa**: A aplicação apresenta atrasos perceptíveis e não atende ao requisito de resposta quase instantânea, prejudicando a eficiência do Analista de Marketing e Vendas em suas análises de dados.
  
  <i>Teste de Aceitação - Critério 1: Verificação do Tempo de Resposta da Aplicação</i>
- **1.1 {Aceito}**
  - **Explicação do Aceito:** O Analista de Marketing e Vendas realiza uma solicitação na aplicação para acessar e analisar dados. A aplicação responde de forma quase instantânea e o analista consegue realizar análises de dados de maneira eficiente e sem frustrações devido a atrasos na resposta.
- **1.2 {Recusado}**
  - **Explicação do Recusado**: O Analista de Marketing e Vendas realiza uma solicitação na aplicação para acessar e analisar dados. No entanto, a aplicação não responde de forma quase instantânea e apresenta atrasos perceptíveis.
  
**Notas:** Para garantir o tempo de resposta rápido, será implementada uma tabela OLAP entre o cubo de dados e a análise estatística Ensemble. Essa abordagem acelera o consumo de dados, permitindo que a aplicação seja ágil e atenda às expectativas do Analista de Marketing e Vendas.

| **Prioridade** | **Estimativa** | **Relação** |
|----------|----------|----------|
| méida | 3 dias  | User Story 8 - User Soty 9|

<br><br>
