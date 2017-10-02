from flask import Flask, render_template, request

app = Flask(__name__)

# Base address/url
@app.route("/")
def index():
	return "Hello Hackers"

# Extension of url after the '/'
@app.route("/crisforno")
def hi():
	return "Hi, I'm Fris Corno"

# Rendering HTML file
@app.route("/greet")
def greet():
	return render_template("greet.html")

# Default method is GET, otherwise specify POST
@app.route("/checkin", methods=["GET", "POST"])
def checkin():
	# if you add <form>action="", method="POST" ~~~ </form> in html file
	if request.method == "POST":
		print(request.form["name"])

	# not necessary, just extra stuff
	main_greeting = "Hey everyone"

	return render_template("checkin.html", var1=main_greeting)

"""
Look up Heroku Flask

Heroku - great tool for getting hosted website with flask
"""
