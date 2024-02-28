# Use uma imagem base do OpenJDK 11.0.21
FROM adoptopenjdk/openjdk11:jdk-11.0.21_9-alpine-slim AS openjdk

# Define o diretório de trabalho como /app
WORKDIR /app

# Define a versão do Spark
ARG SPARK_VERSION=3.5.0
# https://www.apache.org/dyn/closer.lua/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
# https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz
# https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
# Baixa e extrai o Apache Spark
RUN wget -qO- "https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz" | tar xvz -C /opt && \
    mv "/opt/spark-$SPARK_VERSION-bin-hadoop3" /opt/spark

# Define as variáveis de ambiente do Spark e do Java
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV JAVA_HOME=/opt/java/openjdk
ENV PYTHONPATH=/app

# Use a imagem base do Python 3.10
FROM python:3.10
# Copia os arquivos necessários para o diretório de trabalho
COPY requirements.txt .
COPY tox.ini .
COPY src ./src
COPY test ./test
COPY utils ./utils

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Define o comando padrão para iniciar o aplicativo
CMD ["streamlit", "run", "src/main.py"]
