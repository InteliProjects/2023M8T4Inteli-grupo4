# Script Ensable - framework CRISP-DM

<img width="428" alt="image" src="https://github.com/2023M8T4Inteli/grupo4/assets/99211976/e45cb5bf-7699-4530-a048-7831b3b3aef6">


## 1. Entendimento do Negócio
Neste projeto, o foco é no uso de Big Data para fornecer insights valiosos para uma consultoria de marketing. O objetivo é analisar o Índice de Pobreza Multidimensional não Monetária (IPM-NM) para identificar padrões e tendências que podem ser úteis no planejamento de estratégias de marketing. Essa análise permite uma compreensão mais aprofundada das condições socioeconômicas de diferentes regiões, o que é crucial para direcionar campanhas de marketing de maneira eficaz e responsável.

## 2. Entendimento dos Dados
Os dados são derivados da Pesquisa de Orçamentos Familiares do IBGE, refletindo uma vasta gama de variáveis socioeconômicas. Em um contexto de marketing, esses dados oferecem uma visão profunda sobre diferentes segmentos da população, permitindo uma segmentação de mercado mais precisa e estratégias de marketing direcionadas. Variáveis como moradia, saúde, educação, padrão de vida, entre outras, são cruciais para entender as necessidades e preferências dos diferentes grupos.

## 3. Preparação dos Dados
A preparação dos dados envolve a importação e combinação de conjuntos de dados de diferentes períodos, seguido por uma seleção criteriosa de características que são mais relevantes para os objetivos de marketing. A qualidade e a relevância dos dados são críticas em Big Data, pois influenciam diretamente a precisão dos insights gerados. A segmentação dos dados em conjuntos de treino e teste é uma etapa chave para garantir a validade do modelo desenvolvido.

## 4. Modelagem
A escolha do algoritmo Random Forest para a modelagem é uma decisão estratégica, dado o seu desempenho robusto em grandes conjuntos de dados e sua capacidade de lidar com variáveis não-lineares e interações complexas. O modelo é treinado com o conjunto de dados de treino, e sua eficácia é avaliada no conjunto de teste. A avaliação do modelo inclui métricas como MSE, MAE e R², que são essenciais para garantir que as previsões sejam confiáveis e úteis para fins de marketing.

## 5. Avaliação
A fase de avaliação concentra-se em interpretar as métricas de desempenho do modelo. Essas métricas fornecem insights sobre a precisão e a confiabilidade das previsões, que são fundamentais para aplicar os resultados no planejamento de estratégias de marketing. Um modelo bem ajustado que pode prever com precisão o IPM-NM pode ser uma ferramenta valiosa para entender as necessidades e preferências dos diferentes segmentos do mercado.

## 6. Desdobramento ou Implantação
A visualização dos resultados, incluindo gráficos de dispersão e de resíduos, ajuda a interpretar as previsões do modelo e a comunicar esses insights de forma eficaz para os stakeholders. A análise da importância das variáveis ajuda a identificar quais fatores são mais influentes no IPM-NM, proporcionando uma base para estratégias de marketing mais focadas e direcionadas. Além disso, a análise de correlação entre as diferentes variáveis pode revelar insights sobre como diferentes aspectos socioeconômicos interagem e influenciam as decisões de compra e comportamentos do consumidor.
