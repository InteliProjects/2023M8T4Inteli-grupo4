# Documento de Especificações do Projeto: Sistema de Big Data para Engenharia de Dados e Geração de Infográficos

### 1. Introdução

Este documento tem como objetivo delimitar as capacidades, limitações e características fundamentais do sistema em desenvolvimento, estabelecendo um melhor entendimento do escopo do projeto, evitando ambiguidades e garantindo uma visão unificada entre os participantes do grupo e com os parceiros do projeto.

## 1.1 Matriz de 4 Quadrantes:

Com essa finalidade em mente, uma matriz com quatro quadrantes é criada, contendo os seguintes conteúdos:

- É: Neste quadrante, delineamos tudo aquilo que o produto é, destacando as características essenciais que o definem.

- Não é: Este quadrante estabelece limites claros, esclarecendo tudo aquilo que o produto não é. Ao fazê-lo, definimos áreas específicas que não serão abordadas no projeto.


A partir desses dois quadrantes já é possível delimitar um pouco o escopo do sistema, restando os outros dois quadrantes:

- Faz: Ao concentrar-nos no que o produto faz, é possível identificar as primeiras funcionalidades da solução, material importante para discutir com ao Product Owner do projeto.

- Não faz: Identificando o que o produto não faz, comunicamos de forma inequívoca que determinados aspectos não fazem parte do escopo do projeto.

Esta abordagem não apenas economiza tempo ao evitar retrabalhos, mas também contribui para um entendimento compartilhado e alinhado entre todos os envolvidos no desenvolvimento da solução.

---

## 3. O que o Sistema É:

### 3.1 Ferramenta de Suporte à Tomada de Decisão:
 É uma ferramenta projetada para auxiliar na tomada de decisões, oferecendo insights a partir da análise de grandes volumes de dados.

### 3.2 Personalizável e Configurável:
Oferece opções de personalização para atender às necessidades específicas do usuário, permitindo configurações conforme os requisitos da análise.

### 3.3 Solução para Armazenamento de Dados:
É uma solução eficaz para o armazenamento e recuperação eficiente de grandes conjuntos de dados, facilitando análises.

### 3.4 Compatível com Diversos Bancos de Dados:
É compatível com uma variedade de bancos de dados, proporcionando flexibilidade na escolha da infraestrutura de armazenamento a depender do tipo de dado.

### 3.5 Ambiente Escalável e Adaptável:
É projetado para operar em ambientes escaláveis, adaptando-se dinamicamente às necessidades do projeto e ao volume crescente de dados.

---

## 4. O que o Sistema Não É:

### 4.1 Plataforma de Desenvolvimento de Modelos de Machine Learning:
Não é uma plataforma de desenvolvimento de modelos de machine learning. O foco está na análise e visualização dos dados, não na criação de algoritmos preditivos complexos.

### 4.2 Sistema de Segurança Independente:
Não atua como um sistema de segurança independente. A implementação de medidas de segurança deve ser feita em conjunto com práticas recomendadas de segurança de dados a partir da plataforma cloud em que os dados foram inseridos.

### 4.3 Ferramenta de Análise de Linguagem Natural (NLP):
Não realiza análise avançada de linguagem natural. A interpretação contextual dos dados requer ferramentas especializadas.

### 4.4 Substituto para Processos de Garantia de Qualidade Manuais:
Não substitui processos de garantia de qualidade manuais. A validação e verificação contínua dos dados são responsabilidades essenciais do usuário.

### 4.5 Solução Única para Todas as Fontes de Dados:
Não é uma solução universal para todas as fontes de dados. Requer configurações específicas para integrar eficientemente com diferentes tipos de fontes.

---

## 5. O que o Sistema Faz:

### 5.1 Pipeline de Engenharia de Dados Eficiente:
Desenvolve um pipeline para a coleta, transformação e carga (ETL) de dados, garantindo a integridade, qualidade e segurança do processo.

### 5.2 Geração Automática de Infográficos:
Automatiza a criação de infográficos a partir dos dados consolidados, facilitando a interpretação visual dos insights pelos usuários.

### 5.3 Armazenamento em Cubo de Dados:
  Constrói um cubo de dados para armazenamento, permitindo consultas durante as análises com variáveis pré definidas.

### 5.4 Adaptação Dinâmica à Escala:
Opera em ambientes escaláveis, adaptando-se dinamicamente à demanda de dados diferentes e usuários.

### 5.5 Integração com Ferramentas de Visualização Externas:
  - Facilita a integração com ferramentas externas de visualização para análises personalizadas.

---

## 6. O que o Sistema Não Faz:

### 6.1 Análise Preditiva Avançada:
Não realiza análises preditivas avançadas. O foco está na apresentação e interpretação de dados históricos.

### 6.2 Implementação de Algoritmos de Machine Learning:
Não oferece suporte direto à implementação de algoritmos de machine learning. Recomenda-se a integração com plataformas dedicadas nesses casos.

### 6.3 Verificação Automatizada de Qualidade de Dados:
Não inclui uma ferramenta de verificação automatizada de qualidade de dados. A validação precisa ser configurada conforme as necessidades específicas do projeto, sendo esses adicionados pelo usuário desenvolvedor no momento de ingestão dos dados.

### 6.4 Manipulação Direta de Fontes Externas Complexas:
Não manipula diretamente fontes externas complexas sem configuração prévia. A complexidade das fontes pode requerer personalizações específicas.

### 6.5 Ferramenta de Business Intelligence Completa:
Não substitui uma plataforma completa de business intelligence. Enquanto oferece recursos visuais, outras funcionalidades podem necessitar integração com ferramentas especializadas.

---

# 7. Referências

LUIZALABS. Lean Inception: Como desenvolver produtos em um processo de co-criação (Parte 2). Medium, 2018. Disponível em: https://medium.com/luizalabs/lean-inception-como-desenvolver-produtos-em-um-processo-de-co-cria%C3%A7%C3%A3o-parte-2-22818a8e60aa

