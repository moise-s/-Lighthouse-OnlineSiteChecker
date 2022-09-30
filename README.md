## Módulo 2: Fundamentos da Computação

Para rodar o projeto, primeiro clone o repositório. Usando o terminal digite:

```
git clone https://github.com/moise-s/-Lighthouse-OnlineSiteChecker.git
```

Usando git bash, crie um ambiente virtual para rodar o projeto:

```
python -m venv venv
```

Agora, ative o ambiente virtual:

```
source venv/bin/activate
```

Instale os pacotes necessários para rodar o programa:

```
pip3 install -r requirements.txt
```

Para rodar o programa, basta digitar as instruções, seguido de um ou mais websites, separados por `espaço`:

```
python -m sitechecker -u uol.com.br indicium.tech
```

Há também comando `help`. Para acessar, digite o seguinte:

```
python -m sitechecker -h
```

### ToDo proposto

1. Ampliar a função acima para permitir a inclusão de arquivos com listas de URLs no CLI passando um caminho --file path/to/file.csv. Para rodar, basta digitar o seguinte para um arquivo de TXT já no repositório:

```
python -m sitechecker -f sites.txt
```

E, para o arquivo em CSV:

```
python -m sitechecker -f sites.csv
```

2. Criar um script em Bash que permite rodar esse verificador a partir de uma periodicidade pré-definida (por exemplo, a cada 24 horas). Ver CRON.

Não foi possível completar a task 2 até o presente momento. Voltarei a este projeto mais tarde para sua conclusão.

### Créditos

Essa foi uma atividade proposta pela equipe Indicium, através do programa Lighthouse:

```
https://bitbucket.org/indiciumtech/aula_python_20_09/src/master/
```
