from Flask import flask, redirect, render_template, request
import pygoogle

app = Flask(__name__)
app.config.from_object(__name__)




if __name__ == "__main__":
    app.debug=True
    app.run()


