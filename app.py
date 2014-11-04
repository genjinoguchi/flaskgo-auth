from flask import Flask, redirect, render_template, request, make_response, abort
from pymongo import Connection

app = Flask(__name__)
app.config.from_object(__name__)


conn = Connection()
db = conn["zabariistheman"]
print "db init"



@app.route("/") #info page.
def index():
    return render_template("index.html")

@app.route("/home") #must be logged in to view this page
def home():
    username = request.cookies.get('username')
    password = request.cookies.get('password')

    authenticated = ""

    #Authenticate using mongodb
    if db.users.find({"username": username,"password":password}).count()==1:
        authenticated=db.users.find({"username": username,"password":password})[0]["username"]

    if authenticated:
        return render_template("home.html",loggedin="logged in as: "+authenticated)
    else:
        return render_template("login-register.html",error="You need to be logged in to view this page.")
    


@app.route("/login-register")
def login_register():
    if request.method == "GET":
        return render_template("login-register.html",error="")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "GET":
        return redirect("http://localhost:5000/login-register")
    if request.method == "POST": #look for post requests of new users
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        
        error = ""
        #Store the information in mongo
        if (db.users.find({"username": username,"password":password}).count()==0):
            db.users.insert({"username":username,"password":password})
            print "username: "+username
            print "password: "+password
        else:
            error="There is already an account under this username."
        if error=="":
            resp = make_response(redirect("http://localhost:5000/home"))
            resp.set_cookie("username",username)
            resp.set_cookie("password",password) #such hackable
            return resp
        else:
            return render_template("login-register.html",error=error)


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return redirect("http://localhost:5000/login-register")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        error = ""
        #Verify information with mongo. If there is an error, set error to a string describing it.
        if not db.users.find({"username": username,"password":password}).count()==1:
            error="Invalid username or password."
        if error=="":
            resp = make_response(redirect("http://localhost:5000/home"))
            resp.set_cookie("username",username)
            resp.set_cookie("password",password)
            return resp
        else:
            return render_template("login-register.html",error=error)


@app.route("/logout")
def logout():
    resp = make_response(render_template("login-register.html",error="You have successfully logged out."))
    resp.set_cookie("username","")
    resp.set_cookie("password","")
    return resp


if __name__ == "__main__":
    app.debug=True
    app.run()
