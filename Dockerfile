# Usa uma imagem leve do Python
FROM python:3.10-slim

# Cria um diretório no container
WORKDIR /main

# Copia os arquivos do projeto
COPY . .

# Instala as dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Exponha a porta do Streamlit
EXPOSE 8501

# Comando para rodar o app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
