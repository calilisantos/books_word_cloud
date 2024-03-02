## Iniciando o ambiente
python3 -m venv words_env 
source words_env/bin/activate

## Instalando as dependências
pip install -r requirements.txt


## [Depreciado com a mudança de versão do pyspark] Com Dockerfile.Global
docker build -t book-wordcloud -f Dockerfile.Global .
docker run book-wordcloud

# Com docker-compose
docker-compose down -v
docker-compose up --build 
[Importante atualizar o valor de JAVA_HOME do container java no arquivo docker-compose.yml se necessário.]