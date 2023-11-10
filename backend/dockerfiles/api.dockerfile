FROM python:3.11

# Criar um usuário "Chickie" e definir seu shell padrão
RUN useradd -ms /bin/bash chickie

# Atualizar o pip e instale o setuptools
RUN pip install --upgrade pip && pip install --upgrade setuptools

# Definir o diretório de trabalho para a aplicação
WORKDIR /home/chickie/chickie

# Alterar para o usuário "chickie"
USER chickie

# Copiar os arquivos de requisitos para o diretório de trabalho do contêiner
COPY ./requirements/api.txt requirements/api.txt

# Instale as dependências do aplicativo
RUN pip install --no-cache-dir -r ./requirements/api.txt

# Adicionar o diretório ".local/bin" ao PATH
ENV PATH="/home/chickie/.local/bin:${PATH}"

# Copiar os arquivos de configuração para o diretório correto
COPY ./config/.secrets.toml ./config/.secrets.toml
COPY ./config/settings.toml ./config/settings.toml

# Copiar todo o restante dos arquivos do contexto para o diretório de trabalho do contêiner
COPY . .    

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED 1
ENV PYTHONBREAKPOINT 0
ENV TERM xterm-256color

CMD [ "uvicorn", "asgi:app", "--host", "0.0.0.0", "--port", "80" ]
