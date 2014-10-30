from flask import Flask, redirect, render_template, request
import pymongo

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.debug=True
    app.run()


