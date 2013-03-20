from flask import Flask, request, url_for
app = Flask(__name__)

app.secret_key = 'vzjknvfdkjbdfz/.,.;#vszd.dfz'

@app.route('/')
@app.route('/<name>/')
def index(name=None):
    if name is None:
        return "Visit %s!" % url_for('index', name='your-name-here', _external=True)
    else:
        return "Hello %s!" % name

if __name__ == '__main__':
    app.run(debug=True)