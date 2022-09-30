from flask import Flask, render_template

app = Flask(__name__)  # name is passed as it is used to find the root node

@app.route("/")
def home():
    username = "Your Mom amongus"
    suggestions = [
        {"task": "Sandwich", "desc":"Pls am hungri"},
        {"task": "Do nothing","desc": "Why live?"}
        ]
    return render_template("main.html", username=username, suggestions=suggestions) 

if __name__ == "__main__":
    app.run(debug = True)
