# Documentação de Prototipação em Baixa Fidelidade com Wireframes

## 1. Introdução

Antes da construção de um sistema de dashboard para a visualização de dados e infográficos, por exemplo, é importante a utilização de uma ferramenta de prototipação que possibilite ajustes ágeis que não representam grande impacto no tempo e retrabalho de mudanças, que afetariam a qualidade da entrega do projeto. Com isso, protótipos feitos com wireframes são úteis para usuários do sistema apontarem possíveis problemas e apresentarem feedbacks que podem incorporar na construção posterior de design do sistema. Nesse contexto, os protótipos criados atuam como um guia esquemático que delineia a distribuição de elementos-chave como caixas de texto, botões, imagens, mas sem aprofundamentos gráficos.

## 2. Wireframes Desenvolvidos

Duas páginas foram criadas via wireframe, projetadas de acordo com o impacto mapeado na experiência e necessidade do usuário. Na primeira página, destinada ao acesso inicial de um usuário autenticado, foram priorizados elementos que fornecem uma visão imediata de informações críticas e detalhadas. O design desta página é orientado pela estratégia de destacar visualmente o geomapa de dados de vendas, gráficos de vendas por canais e consumo por categoria, além de rankings para dados de vendas e canais. Esses elementos prioritários foram escolhidos para orientar o usuário rapidamente às métricas-chave, facilitando a tomada de decisões estratégicas.

Por outro lado, a segunda página, desenvolvida para complementar a primeira, atuando como um suporte, oferece uma visualização mais abrangente. Com três filtros distintos, como região, canal e categoria no elemento principal, um gráfico de percentual dos dados usados na ingestão e uma tabela dos dados, essa página foi concebida para aprofundar a análise e proporcionar uma perspectiva que assegure a integridade dos dados. 

Juntas, essas páginas formam uma experiência que equilibra o acesso de informações prioritárias com profundidade analítica e também a validação necessária para a compreensão dos dados presentes nos infográficos. 

Mais informações sobre a escolha da posição dos elementos e técnicas utilizadas e feedbacks utilizados para elaborar e ajustar os protótipos wireframe das páginas podem ser verificados no tópico 3. Técnicas Aplicadas. A seguir os protótipos desenvolvidos:

![Wireframe 1](https://github.com/2023M8T4Inteli/grupo4/blob/dev/assets/Wireframe_Web1.png) <br>
Figura 01: Wireframe Web 1  <br>
Fonte: Elaboração própria

![Wireframe 2](https://github.com/2023M8T4Inteli/grupo4/blob/dev/assets/Wireframe_Web2.png) <br>
Figura 02: Wireframe Web 2  <br>
Fonte: Elaboração própria

Visando melhor atender a necessidade do cliente, também foi feita a versão mobile do wireframe das páginas:

![Wireframe 3](https://github.com/2023M8T4Inteli/grupo4/blob/dev/assets/Wireframe_Mobile1.png) <br>
Figura 03: Wireframe Mobile 1  <br>
Fonte: Elaboração própria

![Wireframe 4](https://github.com/2023M8T4Inteli/grupo4/blob/dev/assets/Wireframe_Mobile2.png) <br>
Figura 04: Wireframe Mobile 2  <br>
Fonte: Elaboração própria

![Wireframe 5](https://github.com/2023M8T4Inteli/grupo4/blob/dev/assets/Wireframe_Mobile3.png) <br>
Figura 05: Wireframe Mobile 3  <br>
Fonte: Elaboração própria

Observação: A visualização do Wireframe Mobile ficou reduzida por questões de espaço, mas o arquivo original pode ser acessado [AQUI](https://app.moqups.com/InJEUgJ6Sd2CN11iqjJgNt2xtHRaTV99/view/page/a7f76f924), tanto o wireframe Mobile quanto o desenvolvido para Web.

## 3. Técnicas Aplicadas

Os wireframes desenvolvidos tiveram uma abordagem centrada na usabilidade e na interpretação dos dados, onde a escolha do design foi fundamentada em técnicas e feedbacks recebidos, aplicados de forma diferente a cada elemento, de acordo com a sua importância e dependência de outros dados, que serão descritos a seguir:

### 3.1. Ênfase na Prioridade dos Dados:
O espaço destinado a dados que devem estar presentes assim que o usuário acessar o sistema deve representar o primeiro elemento que usuário irá naturalmente olhar, seguindo o princípio da visão em "Z" das páginas web, justificando o geomapa com dados de vendas como elemento prioritário, refletindo a importância estratégica dessas informações para o usuário do sistema. 
A partir deste elemento, foi pontuada a necessidade da função de granularidade dos elementos mostrados, apresentando também uma flexibilidade por filtros que podem ser implementados no geomapa real implementado no sistema.

### 3.2. Organização de Informações para Análise Cruzada:
A análise de dados pode se beneficiar com a criação de um dashboard, dispondo elementos que podem se complementar, um ao lado do outro. Os espaços menores adjacentes destinados aos gráficos de vendas por canais e consumo por categoria e os rankings de vendas por categoria e canal estão dispostos em uma organização que facilita a comparação e análise cruzada dessas métricas. 
Um feedback recebido sobre ambos grupos de elementos foi aumentar a flexibilidade do que é mostrado, adicionando a possibilidade de trocar as variáveis que são mostradas, já adiantando próximos passos ao evoluir o protótipo feito em wireframe a um nível de maior fidelidade. 

### 3.3. Dados comparativos por Rankeamento de Variáveis:
A inclusão de dois rankings proporcionam uma rápida visualização por desempenho em termos de vendas e canais, priorizando informações para a verificação dos elementos que apresentam maior performance em relação aos demais, trazendo possíveis pontos de atenção que devem ser priorizados a partir de uma grandeza de tamanho, volume ou quantidade.
A adição de filtros para trocar a variável utilizada para a criação do ranking foi descrita anteriormente.

### 3.4. Visualização Total com Opção de Filtros:
Com o segundo wireframe representando a segunda página do sistema, a prioridade dos dados visualizados é reduzida, mas devem complementar os dados apresentados na primeira página. A necessidade de uma visão total de um tipo de elemento é representada como o primeiro elemento visível para o usuário na segunda página, com a visualização dos parceiros, que foi projetado considerando a necessidade de explorar esses dados de maneira a verificar a situação desses elementos, que a partir dos principais filtros por região, canal e categoria, foram apontados como feedback para a personalização da visualização pelo usuário.

### 3.5. Status dos Dados Utilizados:
Ainda na segunda página, para assegurar o usuário dos dados utilizados para a criação dos elementos da primeira página é foi planejado um espaço que apresente dados sobre a integridade dos dados presentes nos infográficos gerados, e isso é representado com o percentual dos dados e um filtro dos dados que informam o usuário sobre os dados que foram usados na ingestão dos dados, promovendo maior confiabilidade e balizando decisões tomadas com a segurança dos dados que estão em uso.

### 3.6. Telas Menores e Gestos Típicos de Dispositivos Móveis:
No wireframe que representa a primeira página, por apresentar os elementos com maior prioridade de visualização, foi mantida uma configuração de manter os elementos mais relevantes de serem visualizados primeiro no topo da página, funcionando de maneira independente em relação aos demais e parear os elementos menores por dependência, em no máximo dois. Com isso, os gráficos que podem proporcionar uma análise cruzada permanecem um ao lado do outro em telas menores, bem como os dados de ranking.

Já na segunda página de wireframe, cada elemento deve estar posicionado na mesma coluna, um abaixo do outro, favorecendo a visualização de cada elemento de forma independente, pois eles não se complementam diretamente a ponto de proporcionar uma análise cruzada, como na primeira página.

### 3.7. Reduzir a Utilização de Texto:
Foi utilizado um header de tamanho reduzido, considerando a importância de comunicar ao usuário, por exemplo, quando aqueles dados foram atualizados ou quando os infográficos presentes na página foram gerados, para o acompanhar as versões de gráficos gerados, trazendo maior confiabilidade nas análises e decisões tomadas. Pela relevância da informação, este header foi colocado acima de todos os gráficos na primeira página, podendo sofrer alterações de acordo com o avanço da prototipação em fidelidades mais altas.

É importante também destacar que todos os elementos do protótipo podem sofrer ajustes e alterações de acordo com a evolução do protótipo em níveis de maior fidelidade e com base em testes de usabilidade, bem como feedbacks do parceiro e usuário.

## 4. Incorporação de Feedbacks
Após a apresentação dos wireframes, foram recebidos feedbacks pelo parceiro e pelo professor, que estão sendo incorporados na evolução dos protótipos e irão ser demonstrados nas próximas entregas. Os feedbacks recebidos foram:
- Sempre tentar cruzar dados de categoria e canal, para que o usuário possa ter uma visão mais completa dos dados;
- Incluir um filtro de data para que o usuário possa selecionar o período de tempo que deseja visualizar;
- Sobre a questão de região, foi dito que quanto mais granularidade, melhor, pois o usuário pode querer visualizar dados de uma região específica;
- No painel, devemos incluir uma combinação de gráficos, tabelas e KPIs. Em vez do ranking, poderíamos usar alguns KPIs.

## 5. Referência

ZHANG, M. Speeding Up The Prototyping Of Low-Fidelity User Interface Wireframes. 2022 - Research Compliance Certification. Disponível em: https://oaktrust.library.tamu.edu/bitstream/handle/1969.1/196603/ZHANG-FINALTHESIS-2022.pdf?sequence=1&isAllowed=y

LI, J., YANG, J., HERTZMANN, A., ZHANG, J., XU, T. Layoutgan: Generating Graphic Layouts With Wireframe Discriminators. 2019 - Beijing Institute of Technology. Disponível em: https://arxiv.org/pdf/1901.06767.pdf
