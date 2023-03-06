from flask import Flask, render_template

app = Flask(__name__)

#TODO: criar a 1ª pagina do site

# route to homepage -> mrsaturnino.com/
# function
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/users/<user_name>")
def users(user_name):
    return render_template("users.html", user_name=user_name)


#TODO: colocar a página no ar
if __name__ == "__main__":
    app.run(debug=True)

    # heroku server
