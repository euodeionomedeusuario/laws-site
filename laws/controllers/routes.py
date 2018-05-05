from flask import render_template, redirect, request

from laws import app

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/messages/", methods=["post"])
def send_message():
	email = request.form.get("email")
	phone = request.form.get("phone")
	message = request.form.get("message")

	print(email)
	print(phone)
	print(message)

	return redirect("/")
