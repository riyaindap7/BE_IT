from flask import Flask, request

app = Flask(__name__)

@app.route('/login_page', methods=['POST'])
def login():
    uname = request.form['uname']
    password = request.form['pass']
    if uname == "Riya" and password == "R123":
        return "Welcome %s!" % uname
    else:
        return "Invalid username or password."

if __name__ == '__main__':
    app.run(debug=True)
