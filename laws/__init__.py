from flask import Flask
from flask_mail import Mail
from pymongo import MongoClient

app = Flask(__name__)

app.config.update(
        DEBUG=True,
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME = 'lawsclassroom@gmail.com',
        MAIL_PASSWORD = '@lawsclassroom'
        )

app.config["SECRET_KEY"] = "SECRET_KEY"

mail=Mail(app)

client = MongoClient('mongodb://localhost:27017/')

db = client.lawssitedb

from laws.controllers import routes
