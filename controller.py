from flask import Flask, request, render_template
import usersUtility

app = Flask(__name__, static_url_path='/static/')

@app.route("/register",methods=['GET'])
def renderRegister():
    return render_template("register.jinja")

@app.route("/login",methods=['GET'])
def renderLogin():
    return render_template("login.jinja")

@app.route("/login",methods=['POST'])
def userLogin():
    email = request.form['email']
    passwd = request.form['passwd']

    return usersUtility.userLogin(email,passwd)

@app.route("/register",methods=['POST'])
def emailRegister():
    email = request.form['email']
    username = request.form['username']
    passwd = request.form['passwd']
    
    return usersUtility.userRegister(email, username, passwd), usersUtility.valid_mail_characters(email)



