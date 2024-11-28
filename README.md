Nomes: Bel Cogo e Bruno da Siqueira Hoffmann

# Trabalho 2 - GB - Ciência de Dados e Big Data

- Objetivo do Projeto: Fazer o treinamento do modelo proposto no GA através da ferramenta Spark, utilizando um ambiente distribuído (simulado via containers docker);

## Mudanças Necessárias

### Dataset
- Para ter um melhor aproveitamento do desempenho do Spark, foi veirificado a necessidade de aumentar a quantidade de dados. Hoje, o dataset continha apenas 1500 dados. A partir disso foi utilizado o modelo CTGAN, sendo ele um `GAN-based Deep Learning data synthesizer`, que gera dados a partir dos dados já existentes.

Assim foi possível aumentar a quantidade de dados de 1500 para 150000.

### Mudanças no código
Além disso, foram necessários mudanças de código para possibilitar a execução dentro da ferramenta Spark. É possível verificar esse script no arquivo `modelo-spark/src/train_script.py`.

## Estrutura de Pastas
A estrutura de pasta ficou dividida da seguinte forma:
- `modelo-spark/`: estrutura contendo as configurações necessária para executar o script dentro da ferramenta spark;
- `modelo-antigo`: estrutura contendo as configurações necessária para executar o script original dentro de um container;
- `modelo-geração-dados`: estrutura contendo o script para gerar mais dados;

Você pode verificar o trabalho no repositório: https://github.com/BrunoHoffmann15/trabalho-big-data-gb-2

## Comparativo de Execuções
Um dos objetivos do nosso trabalho era fazer um comparativo entre a execução em um container simples (simulando uma máquina) e um cluster de containers (simulando o ambiente spark). Para o caso do ambiente spark foram utilizados 7 containers workers, 1 container master e 1 container history. A partir disso, foi executado ambos os casos, e verificado as seguintes métrica:

- Execução da Preparação dos Dados:
  - Um container: 0.71 segundos;
  - Cluster: 84.44 segundos;

- Execução do Treinamento:
  - Um container: 33.79 segundos;
  - Cluster: 100.13 segundos;

- Execução da Validação:
  - Um container: 1 segundo;
  - Cluster: 0.33 segundos;

- Execução das Métricas:
  - Um container: 0.01 segundo;
  - Cluster: 32.03 segundos;

## Como executar os projetos?

- Para executar o modelo antigo, é necessário executar os comandos presentes no `modelo-antigo/README.md`;

- Para executar o modelo com spark, é necessário executar os comandos presentes no `modelo-spark/README.md`;

## Referências

https://www.youtube.com/watch?v=FteThJ-YvXk

https://medium.com/@MarinAgli1/setting-up-a-spark-standalone-cluster-on-docker-in-layman-terms-8cbdc9fdd14b