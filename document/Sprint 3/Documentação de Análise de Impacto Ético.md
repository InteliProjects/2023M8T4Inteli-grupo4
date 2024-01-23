## Sumário

[Documentação de Ánálise de Impacto Ético](#c0)

[Introdução](#c1)

[1. Privacidade e Proteção de Dados](#c2)

[2. Equidade e Justiça](#c3)

[3. Transparência e Consentimento Informado](#c4)

[4. Responsabilidade Social](#c5)

[5. Viés e Discriminação](#c6)

[Conclusão](#c7)

[Referência Bibliográfica](#c8)


# <a name="c0"></a>Documentação de Análise de Impacto Ético

Big Data tornou-se uma ferramenta fundamental em diversos setores, permitindo análises complexas e tomadas de decisão baseadas em dados. Seu uso abrange desde a personalização de serviços até avanços na medicina e na conservação ambiental. Contudo, junto com seus benefícios, surgem desafios éticos e sociais que precisam ser abordados.

Neste documento serão abordados os impactos deste projeto, destacando a sua influência em cinco dimensões, discutindo as formas escolhidas para mitigar os impactos negativos, e promover os aspectos positivos para a sociedade.

## <a name="c1"></a>Introdução

Dentro dos conjuntos de dados de Big Data podem estar inclusos informações sensíveis, que possibilitam a identificação, de forma direta ou indireta, do indivíduo a quem o dado pertence, expondo nome, residência e rotinas pessoais, e isso pode ser exposto de forma intencional, ou não (White et al., 2019). Isso envolve a coleta, armazenamento e o uso desses dados, provocando uma reação de implementar a regulamentação e governança desses dados, de forma a proteger os dados contra acesso não autorizado e uso indevido, definindo também a quem o dado pertence e implicações legais sobre o uso, o armazenamento e a coleta dos dados. 

Porém, segundo Tene e Polonetsky (2013), a proteção desses dados se torna cada vez mais difícil, a partir do momento em que estes dados são compartilhados entre diversas plataformas e empresas ao redor do mundo, carregando informações como saúde, finanças, consumo e o comportamento online dos indivíduos, provocando uma preocupação sobre a perda sobre o controle e o rastreamento do uso desses dados.

Por isso é importante destacar que, para o público em geral, além da segurança sobre os dados, é necessária a confiança sobre o armazenamento e uso desses dados, visto que diversas empresas e órgãos governamentais sofrem vazamentos dos dados, e o indivíduo pode pensar que o dado pertence a ele, quando na verdade o dado pode legalmente pertencer à empresa que o coletou, a depender do país e os termos de uso sobre a plataforma ou software em que o usuário inseriu os dados (White et al., 2019).

## <a name="c2"></a>1. Privacidade e Proteção de Dados

Os desafios e implicações de privacidade e proteção de dados diferem em relação à fonte e o tipo de dado utilizado por um sistema, e devem considerar aspectos legais e práticas éticas para lidar com dados sensíveis e não sensíveis. Visando garantir a conformidade dos dados com regulamentações de privacidade e a categorização adequada, foi considerado o tratamento de acordo com a fonte dos dados utilizados:

Os Dados Públicos são predominantemente coletados e gerenciados pelo governo, não estando sujeitos a restrições de direitos autorais, patentes ou marcas registradas, onde restrições de privacidade, controle e segurança devem ser regulamentadas por estatutos, sendo que os dados públicos têm propensão para serem abertos, mas isso não inclui informações pessoais sob custódia estatal ou detalhes particulares de empresas ou organizações específicas (Possamai, 2016), podendo estes serem armazenados e utilizados de forma livre considerando a privacidade e a proteção da informação.

Da mesma forma, Dados de CNPJ, que envolverem informações associadas a registros de empresas, não são considerados dados pessoais para efeitos da Lei, segundo a LGPD, porém conferem um tipo de dado estratégico da empresa parceira, sendo necessário assegurar a sua integridade, garantindo a segurança ao ser armazenado no banco de dados da solução.

Já os Dados provenientes da API do Parceiro configuram dados estritamente sensíveis, contendo dados confidenciais dos clientes da empresa de consultoria, requerendo uma abordagem específica em termos de segurança, privacidade e conformidade.

Uma regra de negócio envolve a remoção dessas informações após o consumo por ferramentas de análises de dados, reduzindo o risco de exposição ou acesso não autorizado, aumentando a confiança dos clientes sobre os serviços prestados pela empresa. Essa remoção é uma estratégia de tratamento realizada por scripts, definidos na arquitetura projetada, que garantem que as informações não permaneçam armazenadas após determinados ciclos do seu uso e consumo.

## <a name="c3"></a>2. Equidade e Justiça

Segundo Taylor (2017), a partir do avanço tecnológico, populações que antes eram digitalmente invisíveis passaram a ter dados relevantes para pesquisadores e formação de novas políticas públicas, porém esse avanço é limitado devido a dificuldade na equidade da utilização e tratamento dos dados, ou seja, mesmo com representação nas bases de dados, alguns grupos e comunidades seguem sendo prejudicados com dados desproporcionais e insuficientes.

Embora Big Data ofereça oportunidades, é crucial considerar e mitigar possíveis disparidades. Isso inclui garantir acesso igualitário à tecnologia e aos benefícios derivados dela, bem como identificar e corrigir vieses que poderiam resultar em tratamento injusto ou desigual entre grupos sociais.

As disparidades entre regiões e classes sociais frequentemente se refletem nos conjuntos de dados disponíveis. Essas diferenças podem surgir devido a variados níveis de acesso à tecnologia, infraestrutura digital e fatores socioeconômicos. Regiões ou comunidades com infraestrutura digital precária podem estar sub-representadas nos conjuntos de dados, levando a uma menor visibilidade nas análises de dados.

Uma medida aplicada para mitigar isso é implementar uma maior granularidade dos resultados gerados, que se refere à capacidade de analisar informações em níveis mais detalhados e específicos. Isso pode envolver a segmentação dos dados por características demográficas, geográficas ou outros fatores relevantes. Ao realizar análises mais granulares, é possível identificar padrões, necessidades e desafios específicos enfrentados por diferentes regiões, grupos étnicos, faixas etárias ou classes sociais, garantindo que as análises abordem as necessidades específicas de cada grupo ou região.

## <a name="c4"></a>3. Transparência e Consentimento Informado

Enfoque na importância da transparência na coleta, uso e compartilhamento de dados no contexto do Big Data.
Explicação sobre o consentimento informado e seu papel na construção de relações de confiança com os usuários.
Práticas recomendadas para garantir a transparência e obtenção adequada do consentimento.

Embora a transparência envolva a clareza e acessibilidade das informações fornecidas sobre como os dados são coletados, usados e compartilhados com a permissão concedida sobre o uso de seus dados, ferramentas baseadas em dados nem sempre podem ser completamente transparentes, dependendo da complexidade técnica da solução e os algoritmos utilizados (Varley-Winter e Shah, 2016).

Nesse sentido, a confiança passa a ser um pilar relevante para estabelecer um entendimento sobre as práticas de coleta, tratamento, armazenamento e uso dos dados, a partir de uma governança dos dados, de forma a assegurar que as partes envolvidas entendam os processos, dados necessários, e os dados utilizados no sistema e do serviço prestado, com políticas de privacidade detalhadas e cláusulas de consentimento explícitas.

## <a name="c5"></a>4. Responsabilidade Social

A responsabilidade social se refere ao compromisso das organizações em agir de maneira ética e sustentável, considerando não apenas o lucro, mas também os impactos sociais, ambientais e comunitários de suas ações, minimizando impactos negativos e alinhando-se a metas de desenvolvimento sustentável.

É importante considerar os impactos mais amplos do uso de Big Data, englobando avaliar os efeitos do projeto sobre comunidades, práticas sustentáveis e buscar contribuir para metas de desenvolvimento social e ambiental, fazendo parte de uma responsabilidade social, podendo ser alinhada aos Objetivos de Desenvolvimento Sustentável (ODS) da ONU.

Mesmo com dados categorizados como não sensíveis, o uso de dados pode ter um efeito negativo sobre a sociedade, perpetuando a estratificação social, com a exclusão de indivíduos que, ao usarem softwares e participarem de atividades com registros online e cederem seus dados em troca do uso e participação, não recebem benefícios provenientes dos dados analisados. Empresas podem, por exemplo, precificar produtos e serviços no limite de pagamento de usuários, usando análise de dados para obter uma maior margem de lucro, porém essas mesmas empresas raramente estão dispostas a compartilhar a riqueza gerada com os dados dos indivíduos com os próprios indivíduos que geraram esses dados (Tene e Polonetsky, 2013).

Nesse sentido, considerando o setor da empresa e os dados coletados e ingeridos, o impacto na ODS de Fome Zero e Agricultura Sustentável pode ser considerável, promovendo ações que podem identificar e auxiliar comunidades carentes com vulnerabilidade alimentar. E ainda por promover uma nutrição mais saudável para essas comunidades, também promoveria positivamente o objetivo de Saúde de Qualidade, melhorando a segurança alimentar e reduzindo doenças relacionadas à alimentação. Já com o incentivo de práticas mais sustentáveis e na gestão de resíduos com uma cadeia de suprimentos ética no setor de alimentos, também afetaria positivamente o objetivo de Consumo e Produção Responsáveis.

Em contrapartida, com a utilização dos dados de forma a ignorar o aspecto equitativo, pode ferir o objetivo de Redução das Desigualdades, aumentando a disparidade na cadeia alimentar, marginalizando grupos sociais vulneráveis, podendo inclusive afetar pequenos produtores.

## <a name="c6"></a>5. Viés e Discriminação

Viés e discriminação estão relacionados à possibilidade de algoritmos e sistemas tomarem decisões que prejudiquem determinados grupos, resultando em um tratamento desigual devido a distorções nos dados ou nos tratamentos realizados.

Hargittai (2020) ressalta que rastros comportamentais em redes sociais de indivíduos de classes sociais mais privilegiadas possuem maior probabilidade de estarem mais presentes nos conjuntos de dados em relação a indivíduos de comunidades mais periféricas, enviesando os dados comportamentais nessas amostras. Isso reforça que análises realizadas com essas bases acabam privilegiando tipos de indivíduos com base em sua classe social, ou seja, uma parte da população, e por isso é importante estar ciente sobre quais vozes estão representadas nos conjuntos de dados.

Para mitigar esses viéses e discriminação nos conjuntos de dados, uma prática comum que poderia ser implementada seria o balanceamento dos dados, visando equilibrar as amostras e garantir uma representação mais justa. No entanto, ao balancear excluindo ou criando dados novos pode prejudicar análises gerais, comprometendo a integridade e distorcendo as relações presentes nos dados originais. Assim, a implementação de filtros que permitem uma análise mais granular torna-se uma possibilidade viável, sem comprometer a integridade dos dados.

Filtros com granularidade permitem a seleção de dados com base em critérios específicos, possibilitando uma análise em cenários selecionados, mas isso não impede que o usuário do sistema, por vieses próprios, selecione recortes por regiões que intencionalmente excluem populações periféricas, com a finalidade de favorecer indivíduos mais privilegiados, ressaltando a importância de uma equipe diversa para a utilização do sistema implementado com Big Data.

## <a name="c7"></a>Conclusão

A discussão sobre a utilização de Big Data na análise e tomada de decisões e o impacto na sociedade abrange diversas dimensões éticas e sociais, desde a privacidade e proteção dos dados, transparência na utilização e armazenamento de informações, até viéses e discriminação que favorecem indivíduos enquanto prejudica outros. Isso ressalta a necessidade de implementar regulamentações que protegem os usuários e promovem um uso ético dos dados, com responsabilidade e visando não apenas o lucro das empresas, mas benefícios para a sociedade como um todo.

Entretanto, é importante ressaltar que o impacto de medidas regulatórias também podem impactar negativamente o desenvolvimento acadêmico a longo prazo. Schroeder e Cowls (2014) indicam que as implicações éticas para a privacidade e a segurança dos dados são diferentes em pesquisas acadêmicas, que visam um conhecimento generalizado, e pesquisas aplicadas, que buscam explorar os dados para fins comerciais e influenciar o comportamento político ou social dos indivíduos por exemplo. O limite do valor dos dados possui pesos diferentes, já que restrições na utilização dos dados impactam a demanda por conjuntos de dados em larga escala para pesquisas acadêmicas, utilizadas para melhor desenvolver o conhecimento científico-social a longo prazo, provocando uma redução nos ganhos das pesquisas acadêmicas, e pesquisas aplicadas não sofrem esse impacto para usos comerciais ou não acadêmicos, por serem reduzidos ou coletados pela própria empresa ou órgão governamental.

Driscoll e Walker (2014) ressaltam ainda que pesquisas acadêmicas realizadas com Big Data enfrentam dificuldades no processo de coleta, gerando dados não estruturados de baixa qualidade, resultando em perdas irreversíveis dos mesmos, impondo barreiras que limitam o progresso de tais pesquisas, onde empresas privadas conseguem recursos para acessar e manipular esses dados para benefício próprio.

## <a name="c8"></a>Referências Bibliográficas

Driscoll, K., & Walker, S. (2014). "Working Within a Black Box: Transparency in the Collection and Production of Big Twitter Data." International Journal of Communication.

Hargittai, E. (2020). "Potential Biases in Big Data: Omitted Voices on Social Media." Social Science Computer Review.

Monleón-Getino, A. (2015). "El impacto del Big Data en la Sociedad de la Información: Significado y Utilidad." Universidad de Barcelona.

Possamai, A. J. (2016). "Dados Abertos no Governo Federal Brasileiro: Desafios de Transparência e Interoperabilidade." Dissertação (Mestrado em Ciência Política), Instituto de Filosofia e Ciências Humanas, Programa de Pós-Graduação em Ciência Política, Universidade Federal do Rio Grande do Sul.

Schroeder, R., & Cowls, J. (2014). "Big Data, Ethics, and the Social Implications of Knowledge Production." Oxford Internet Institute.

Taylor, L. (2017). "What is data justice? The case for connecting digital rights and freedoms globally." Big Data & Society.

Tene, O., & Polonetsky, J. (2013). "Big Data for All: Privacy and User Control in the Age of Analytics." Northwestern Journal of Technology and Intellectual Property.

Varley-Winter, O., & Shah, H. (2016, December 28). "The Opportunities and Ethics of Big Data: Practical Priorities for a National Council of Data Ethics.", Royal Statistical Society.

White, G., Ariyachandra, T., & White, D. (2019). "Big Data, Ethics, and Social Impact Theory – A Conceptual Framework." The Journal of Management and Engineering Integration, 12(1), 9. Xavier University.
