from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

adminUsername = "lucapolito"
adminPassword = "Q45fh.89sjT"


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (username == adminUsername) and (password == adminPassword):
            return render_template("homepage.html", username=adminUsername)
    return render_template("index.html", css_url = url_for("static", filename="styleHome.css"))

@app.route("/homepage", methods=('GET', 'POST'))
def homepage():
    return render_template("homepage.html", css_url = url_for("static", filename="styleHomePage.css"))


if __name__ == '__main__':
    app.run(debug=True)
