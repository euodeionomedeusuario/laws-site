from flask import render_template, redirect, request

from flask_mail import Message
from laws import mail
from laws import db

from laws import app

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/messages/", methods=["POST"])
def send_message():
	email = request.form.get("email")
	phone = request.form.get("phone")
	message = request.form.get("message")

	msg = Message(
		'Mensagem no Site LAWS',
		sender='lawsclassroom@gmail.com',
		recipients=
		['lawsclassroom@gmail.com'])
	msg.html="E-mail - {0}<br>Telefone - {1}<br>Mensagem<br>{2}".format(email, phone, message)
	mail.send(msg)
	return redirect("/")


@app.route("/subscribers/", methods=["POST"])
def register_subscribers():
	name = request.form.get("name")
	email = request.form.get("email")

	db.subscribers.insert({"name": name, "email": email})

	return redirect("/")
