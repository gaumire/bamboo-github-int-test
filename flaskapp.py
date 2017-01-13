

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello_world():
    return render_template('hello.html')


@app.route('/user/<username>')
def show_user(username):
    return 'User %s' % username


@app.route('/users/')
def show_users():
    return 'Users listed here'


if __name__ == '__main__':
    app.run(debug=True)
