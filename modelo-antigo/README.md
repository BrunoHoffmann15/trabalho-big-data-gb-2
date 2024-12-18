# Executando modelo antigo em um container

- Primeiro, build a imagem docker através do comando:

```sh
docker-compose build
```

- Em seguida, execute a imagem utilizando o comando:

```sh
docker-compose up
```

- A partir disso, é necessário esperar, depois de algum tempo será possível observar os logs da aplicação no terminal contendo as métricas de execução.

Exemplo:

```txt
app-1  | Iniciando Preparação dos dados.
app-1  | Preparação dos dados finalizada, tempo de espera: 0.7130687236785889 segundos.
app-1  | Começando treinamento.
app-1  | Treinamento finalizado, tempo de espera: 33.79442477226257 segundos.
app-1  | Executando modelo sobre os dados de testes
app-1  | Modelo sobre os dados de testes executado, tempo de espera: 1.0231773853302002 segundos.
app-1  | Verificando métricas!
app-1  | Métricas verificadas, tempo de espera: 0.015330791473388672 segundos.
app-1  | Acurácia: 67.76222222222222%
app-1  | Precisão: 31.345565749235476%
app-1  | F1-Score: 7.81597509055093%
app-1  | Recall: 4.464609800362976%
app-1 exited with code 0
```