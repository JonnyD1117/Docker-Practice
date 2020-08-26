from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/<name>')
def Iron(name):
    if name == "Jeremy":
        return "Jeremy Irons is a great actor"
    else: 
        return "Eh ~ He is just OK."

@app.route("/")
def home(): 
    name = "Futurama"
    return render_template("index.html", content=name, r=2)





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)