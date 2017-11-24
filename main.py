from flask import Flask, request, redirect
import re

app = Flask(__name__)
app.config['DEBUG'] = True

welcome_html = """
<html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h2>Welcome, {0}.</h1>
    </body>
</html>
"""

form_html = """
<!DOCTYPE html>

<html>
    <head>
        <title>User Signup</title>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 14px sans-serif;
                border-radius: 10px;
            }}
            h2 {{
                margin: 0;
                margin-bottom: 20px;
                padding: 0;
                font: 26px sans-serif;
            }}
            .ffield {{
                display: block;
                margin: 10px 0;
            }}
            label {{
                width: 120px;
                display: inline-block;
            }}
            input {{
                margin: 0;
                width: 200px;
            }}
            .error {{
                color: red;
            }}
            button {{
                margin-top: 12px;
                padding: 6px;
            }}
        </style>
    </head>
    <body>
        <form method="post" action="/signup">
            <h2>Sign up</h1>

            <div class="ffield">
                <label for"username">Username:</label>
                <input type="text" name="username" value="{0}" />
                <span class="error">{1}</span>
            </div>

            <div class="ffield">
                <label for"password">Password:</label>
                <input type="password" name="password" value="{2}" />
                <span class="error">{3}</span>
            </div>

            <div class="ffield">
                <label for"verify">Verify Password:</label>
                <input type="password" name="verify" value="{4}" />
                <span class="error">{5}</span>
            </div>

            <div class="ffield">
                <label for"email">Email (optional):</label>
                <input type="text" name="email" value="{6}" />
                <span class="error">{7}</span>
            </div>

            <div class="ffield">
                <label></label>
                <button type="submit">Submit</button>
            </div>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return redirect("/signup")

@app.route("/signup")
def signup_page():
    return form_html.format("", "", "", "", "", "", "", "", "")

@app.route("/signup", methods=['POST'])
def signup_page2():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    error = False
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if len(username) < 3:
        error = True
        username_error = "Must be at least 3 chars"

    if re.match("^[\w-]*$", username) == None:
        error = True
        username_error = "Only use alphanumeric chars"

    if len(password) < 3:
        error = True
        password_error = "Must be at least 3 chars"

    if re.match("^[\S-]*$", password) == None:
        error = True
        password_error = "Do not use spaces"

    if verify != password:
        error = True
        verify_error = "Passwords don't match"

    if len(email) > 0 and re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) == None:
        error = True
        email_error = "Invalid email address"

    if error == False:
        return redirect("/welcome?username=" + username)

    return form_html.format(username, username_error, password, password_error, verify, verify_error, email, email_error)

@app.route("/welcome")
def welcome_page():
    username = request.args.get('username')
    return welcome_html.format(username)

app.run()
