from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# @app.route('/admin')
# def admin():
#     return "Admin Page"

# @app.route('/user')
# def user():
#     return "User Page"

# @app.route('/student/<name>')
# def student(name):
#     if name == 'admin':
#         return redirect(url_for('admin'))
#     if name == 'user':
#         return redirect(url_for('user'))
#     return f"Student Page for {name}"

@app.route('/')
# def home():
#     return render_template('login.html')

# @app.route('/login', methods=['GET'])
# def login():
#     uname = request.args.get('uname')
#     passwrd = request.args.get('pass')
#     if uname == "Priya1" and passwrd == "Priya1":
#         return f"Welcome {uname}"
#     return "Invalid username or password"

# @app.route('/login',methods = ['POST'])  
# def login():  
#       uname=request.form['uname']  
#       passwrd=request.form['pass']  
#       if uname=="Nishar" and passwrd=="Nishar":  
#           return "Welcome %s" %uname 

# templates
def message():  
      return "<html><body><h1>Hi, welcome to the  website</h1></body></html>" 

if __name__ == '__main__':
    app.run(debug=True)
