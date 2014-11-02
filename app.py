from flask import Flask, redirect, render_template, request, make_response
import pymongo

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/") #Register page, login page, 
def index():
    return render_template("index.html")

@app.route("/new-user",methods=["GET","POST"]):
def create():
	if request.method == "GET":

		resp = make_response(render_template("index.html")) #Send the "create new user" page

	if request.method == "POST": #look for post requests of new users
		username = request.form["username"]
		password = request.form["password"]
		school = request.form["school"]
		grade = request.form["grade"]

		#Store it in mongo

		#Send the response page


if __name__ == "__main__":
    app.debug=True
    app.run()