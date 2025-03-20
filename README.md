<h1 align="left">Plano de Teste</h1>

###

<h2 align="left">1. Introdução</h2>

###

<p align="left">A obesidade e o baixo peso podem impactar significativamente a saúde das pessoas, tornando essencial a conscientização sobre o Índice de Massa Corporal (IMC). Para auxiliar nesse processo, desenvolvemos a Calculadora de IMC, uma aplicação que permite aos usuários inserirem seus dados de peso e altura para obter o valor do IMC e sua respectiva classificação.<br><br>Este documento tem como objetivo especificar os requisitos funcionais e não funcionais do sistema, garantindo que ele atenda às expectativas dos usuários e funcione de maneira eficiente. Além disso, a documentação serve como base para o planejamento e execução dos testes de software, assegurando a qualidade e confiabilidade da aplicação.<br><br>A Calculadora de IMC deve ser simples, intuitiva e acessível, permitindo que qualquer usuário consiga utilizá-la sem dificuldades. O foco está na precisão dos cálculos, na clareza das informações exibidas e na responsividade do sistema para diferentes dispositivos.</p>

###

<h2 align="left">2.	Requisitos a Testar</h2>

###

<p align="left">Nesta seção, são apresentados os requisitos testados durante o desenvolvimento da Calculadora de IMC. Foram considerados tanto os requisitos funcionais que descrevem o comportamento esperado do sistema, quanto os requisitos não funcionais, que garantem a qualidade e eficiência da aplicação.</p>

###

<h2 align="left">2.1 Requisitos Funcionais</h2>

###

<p align="left">Identificador | Nome do Requisito<br>RF1 - O sistema deve permitir a entrada de valores numéricos para peso e altura.<br>RF2 - O sistema deve calcular o IMC corretamente.<br>RF3 - O sistema deve exibir a classificação correspondente ao IMC calculado.</p>

###

<h2 align="left">2.2 Requisitos Não Funcionais</h2>

###

<p align="left">Identificador | Nome do Requisito<br>RNF1 - O sistema deve responder em menos de 1s<br>RNF2 - O layout deve ser responsivo</p>

###

<h2 align="left">3.	Tipos de Teste</h2>

###

<p align="left">3.1 Teste de Unidade<br>Os testes de unidade foram realizados para verificar o comportamento correto das funções individuais do sistema. O foco principal foi garantir que o cálculo do IMC fosse feito corretamente para diferentes entradas.<br><br>3.2 Teste de Integração<br>O teste de integração foi utilizado para validar a comunicação entre os diferentes componentes do sistema, garantindo que a interface do usuário consegue receber, processar e exibir corretamente os dados calculados.<br><br>3.3 Teste de Sistema<br>Este teste avaliou o funcionamento global da aplicação, verificando se a calculadora de IMC atende aos requisitos estabelecidos.<br><br>3.4 Teste de Aceitação<br>O teste de aceitação foi realizado para garantir que o sistema atende às expectativas dos usuários finais.<br><br>3.5 Teste de Regressão<br>Sempre que alterações foram feitas no código, os testes de regressão garantiram que as funcionalidades já implementadas continuavam funcionando corretamente.<br><br>3.6 Teste de Desempenho<br>Este teste foi aplicado para medir o tempo de resposta da calculadora e garantir que o sistema funciona de maneira eficiente.</p>

###

<h2 align="left">4. Recursos</h2>

###

<p align="left">Esta seção apresenta os recursos necessários para a execução dos testes do projeto Calculadora de IMC, abrangendo o ambiente de teste, incluindo hardware e software, bem como as ferramentas utilizadas para a automação dos testes.</p>

###

<h2 align="left">4.1 Ambiente de Teste - Software e Hardware</h2>

###

<p align="left">Os testes foram conduzidos em um ambiente que reflete as configurações típicas de uso, garantindo compatibilidade e desempenho adequado.<br><br>Hardware:<br>Processador: Intel Core i5 10ª geração ou superior / AMD Ryzen 5 ou superior.<br>Memória RAM: Mínimo de 8GB.<br>Armazenamento: SSD com pelo menos 256GB de espaço disponível.<br>Resolução de tela: Testes realizados em telas Full HD (1920x1080) e menores para validação da responsividade.<br><br>Software:<br>Sistema Operacional:<br>Windows 10/11.<br>Linux (Ubuntu 22.04 LTS).<br>macOS Monterey ou superior.<br><br>Navegadores utilizados para testes de compatibilidade:<br>Google Chrome (versão mais recente).<br>Mozilla Firefox (versão mais recente).<br>Microsoft Edge (versão mais recente).<br><br>Tecnologias empregadas no desenvolvimento:<br>Front-end: HTML, CSS, JavaScript.<br>Back-end: Python.<br>Bibliotecas: Pytest (para testes automatizados).</p>

###

<h2 align="left">4.2 Ferramentas de Teste</h2>

###

<p align="left">A validação do funcionamento correto do sistema foi realizada por meio das seguintes ferramentas:</p>

###

<p align="left">Ferramente | Finalidade<br><br>Pytest - Utilizado para a execução de testes automatizados, garantindo a correta funcionalidade do cálculo do IMC.<br><br>Selenium - Aplicado para testes de interface, verificando interações do usuário com o sistema.<br><br>DevTools (Chrome/Firefox) - Recurso utilizado para testes de responsividade e análise de erros via console.<br><br>JMeter - Empregado para testes de desempenho, medindo o tempo de resposta do sistema.</p>

###

<h2 align="left">5. Conclusão</h2>

###

<p align="left">O desenvolvimento da Calculadora de IMC envolveu diversas etapas, desde a definição dos requisitos até a realização dos testes para garantir a qualidade do sistema. Durante esse processo, especificamos os requisitos funcionais e não funcionais, detalhamos o ambiente e as ferramentas utilizadas para os testes e elaboramos um plano de testes abrangente, cobrindo diferentes tipos de validação, como testes de unidade, integração, sistema, aceitação, regressão e desempenho.<br><br>A implementação dos testes automatizados com Pytest permitiu verificar a precisão do cálculo do IMC, assegurando que a função responsável pela operação matemática retornasse valores corretos. Além disso, os testes de integração confirmaram que os inputs do usuário eram corretamente processados pelo sistema.<br><br>No entanto, enfrentamos desafios significativos na etapa de testes de sistema, onde ocorreram seis falhas ao longo do processo. Esses erros estavam relacionados à exibição incorreta da classificação do IMC e inconsistências na validação de entrada. Com base nos resultados, ajustamos o código, aprimoramos a validação dos dados e refinamos a interface para garantir que a experiência do usuário fosse intuitiva e sem falhas.<br><br>Por fim, a execução dos testes manuais e automatizados resultou em um sistema mais robusto e confiável. A documentação desse processo serve como um registro detalhado das estratégias utilizadas e das correções aplicadas, possibilitando futuras melhorias na aplicação. O projeto demonstrou a importância da metodologia de testes para assegurar a qualidade do software, destacando como cada fase contribui para um produto final mais estável e eficiente.</p>

###
