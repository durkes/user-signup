from flask import Flask, request, redirect

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
            </div>

            <div class="ffield">
                <label for"password">Password:</label>
                <input type="password" name="password" value="{2}" />
            </div>

            <div class="ffield">
                <label for"verify">Verify Password:</label>
                <input type="password" name="verify" value="{4}" />
            </div>

            <div class="ffield">
                <label for"email">Email (optional):</label>
                <input type="text" name="email" value="{6}" />
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

    return form_html.format(username, "", password, "", verify, "", email, "")

@app.route("/welcome")
def welcome_page():
    username = request.args.get('username')
    return welcome_html.format(username)

app.run()
