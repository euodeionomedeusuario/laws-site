# Site do LAWS
## Introdução
Esta é a aplicação do site do LAWS / UFMA

## Apps
### MongoDB
[MongoDB](https://www.mongodb.com/) é um software de banco de dados orientado a documentos gratuito, de código aberto e multiplataforma escrito em C ++. Classificado como um programa de banco de dados NoSQL, o MongoDB usa documentos semelhantes ao JSON com esquemas.

### Materialize CSS
[Materialize](http://materializecss.com/) é um CSS framework moderno e responsivo baseado no Material Design do Google.

## Libraries
### Flask
[Flask](http://flask.pocoo.org/) é um microframework para Python baseado em Werkzeug, Jinja 2 e boas intenções. E antes que você pergunte: É licenciado pela BSD! 

### Pymongo
[PyMongo](https://api.mongodb.com/python/current/) é uma distribuição Python que contém ferramentas para trabalhar com o MongoDB e é a maneira recomendada de trabalhar com o MongoDB a partir do Python.

### Flask Mail
[Flask Mail](https://pythonhosted.org/Flask-Mail/) é uma extensão que fornece uma interface simples para configurar o SMTP com seu aplicativo Flask e para enviar mensagens de seus modos de exibição e scripts.

## Install
Clone o repositório

git clone https://github.com/alanaecp/laws-site.git

Entre na pasta

cd /laws-site

Crie um ambiente virtual

virtualenv nome_do_ambiente -p python3

Ative o ambiente virtual

source nome_do_ambiente/bin/activate

Baixe as dependências

pip3 install -r requirements.txt

Execute o app

gunicorn run:app

