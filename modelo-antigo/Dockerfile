# Usa uma imagem base do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia o código da aplicação para o container
COPY . .

# Expõe a porta usada pela aplicação (se aplicável)
EXPOSE 5000

# Comando para rodar a aplicação e redirecionar logs
CMD ["python", "train_random_forest.py", ">>", "./resources/output.txt"]
