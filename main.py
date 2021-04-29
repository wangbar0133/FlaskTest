from flask import Flask, render_template, request, redirect, session, make_response

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def root():
    return render_template('root.html')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route('/create/', methods=['POST', 'GET'])
def create():
    return render_template('create.html',
                           username ="username",
                           password="password")


@app.route('/user/', methods=['POST', 'GET'])
def user():
    return render_template('user.html',
                           username="username",
                           coin_count="coin_count")


@app.route('/tran/', methods=['POST', 'GET'])
def tran():
    return render_template("tran.html")


if __name__ == '__main__':
    app.run(debug=True)
