## Iniciando o ambiente
python3 -m venv words_env 
source words_env/bin/activate

## Instalando as dependências
pip install -r requirements.txt


## Com Dockerfile.Global
docker build -t book-wordcloud -f Dockerfile.Global .
docker run book-wordcloud