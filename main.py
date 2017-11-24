from flask import Flask, request, redirect
import re
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return redirect("/signup")

@app.route("/signup")
def signup():
    template = jinja_env.get_template('signup_form.html')
    return template.render()

@app.route("/signup", methods=['POST'])
def signup_post():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    error = False
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if len(username) < 3 or len(username) > 20:
        error = True
        username_error = "Must be between 3-20 chars"

    if re.match("^[\w-]*$", username) == None:
        error = True
        username_error = "Only use alphanumeric chars"

    if len(password) < 3 or len(password) > 20:
        error = True
        password_error = "Must be between 3-20 chars"

    if re.match("^[\S-]*$", password) == None:
        error = True
        password_error = "Do not use spaces"

    if verify != password:
        error = True
        verify_error = "Passwords don't match"

    if len(email) > 20:
        error = True
        email_error = "Cannot be longer than 20 chars"

    if len(email) > 0 and re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) == None:
        error = True
        email_error = "Invalid email address"

    if error == False:
        return redirect("/welcome?username=" + username)

    template = jinja_env.get_template('signup_form.html')
    return template.render(username=username,
        username_error=username_error,
        password_error=password_error,
        verify_error=verify_error,
        email=email,
        email_error=email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    template = jinja_env.get_template('welcome.html')
    return template.render(username=username)

app.run()
