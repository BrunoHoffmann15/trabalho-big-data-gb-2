Nomes: Bel Cogo e Bruno da Siqueira Hoffmann

# Trabalho Grau B - Spark

## Como executar o ambiente Spark?

Execute o comando abaixo para gerar a imagem docker.

```sh
docker build . -t da-spark-image
```

Execute o comando abaixo, contendo a quantidade de workers que você deseja para realizar a operação. Assim, será criado o ambiente.

```sh
docker-compose up --scale spark-worker=3
```

A partir disso é possível executar a UI do master, com as informações dos workers:

```sh
http://localhost:9090/
```

Também é possível verificar a UI de logs:

```sh
http://localhost:18080/
```

Para rodar o treinamento:
```sh
docker exec da-spark-master spark-submit --master spark://spark-master:7077 --deploy-mode client ./apps/train_script.py
```

## Referências

https://www.youtube.com/watch?v=FteThJ-YvXk

https://medium.com/@MarinAgli1/setting-up-a-spark-standalone-cluster-on-docker-in-layman-terms-8cbdc9fdd14b