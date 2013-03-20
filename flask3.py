from flask import Flask
app = Flask(__name__)

app.secret_key = 'vzjknvfdkjbdfz/.,.;#vszd.dfz'

@app.route('/<name>/')
def index(name):
    return "Hello %s!" % name

if __name__ == '__main__':
    app.run(debug=True)