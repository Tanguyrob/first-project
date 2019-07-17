# -*- coding: utf-8 -*

from flask import Flask, render_template, request
import paramiko


app = Flask(__name__)


@app.route("/")
def hello2():
    return render_template("home.html", message = "Hello 2")

@app.route("/a")
def fonction_suivante():
    return render_template("welcome.html")
    

@app.route("/suite", methods= ['GET' , 'POST'])
def page3():
    #if request.method == 'POST':
    text = request.form.get("text")
    print(text)
    processed_text = text.upper()
    return render_template("page_suivante.html", message = processed_text)
    
@app.route("/fin")
def last_function():
    return render_template("home.html", message = "vous êtes de retour sur la page 1".upper())

@app.route("/achat")
def achat():
    return " branche achat validée"

@app.route("/vente")
def vente():
    return " branche vente validée"

def paramiko_test():
    #créer instance de connexion
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

if __name__ == '__main__':
    app.run()