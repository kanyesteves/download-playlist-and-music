Backup README

# Documentação do projeto para download de videos do youtube

Documentação do projeto para download de videos do youtube. 

## Introdução

Certifique-se de ter python instalado na sua maquina. O passo a passo que voce vai fazer para rodar o app é baseado em sistemas operacionais do tipo Unix. 

### Baixando repositório

- Crie o diretório para clonar o repositório. Abra o terminal e rode o comando:

        $ mkdir appDownload && cd appDownload/

- Clone o repositório no diretório.

        $ git clone https://github.com/kanyesteves/download-playlist-and-music.git

### Criando o ambiente virtual para desenvolvimento

- Rode o comando abaixo para criar e rodar o ambiente virutal.

        $ python3 -m venv downloadMusic && source downloadMusic/bin/activate

### Instalando dependências do projeto

- Após rodar criar o ambiente virtual, atualize o gerenciador de pacotes do Python, PIP.

        $ pip3 install --upgrade pip

- Instale as dependências do projeto.

        $ pip install -r requirements.txt

### Rodando projeto

- Com o comando abaixo suba o servidor com o applicativo.

        $ cd src/ && streamlit run download_musics.py

### Daqui pra frente e com voces !! 

