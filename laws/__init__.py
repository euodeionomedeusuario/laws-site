from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config.update(
        DEBUG=True,
        #EMAIL SETTINGS
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME = 'lawsclassroom@gmail.com',
        MAIL_PASSWORD = '@lawsclassroom'
        )
        
app.config["SECRET_KEY"] = "SECRET_KEY"

mail=Mail(app)

from laws.controllers import routes
