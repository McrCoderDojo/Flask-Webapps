from flask import Flask, request, session, redirect, url_for
app = Flask(__name__)

app.secret_key = 'vzjknvfdkjbdfz/.,.;#vszd.dfz'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['myname']
        return '<a href="%s">Go to page 2</a>' % url_for('page2')
    else:
        return '''
        <form name="myform" method="post">
            <p>Your Name: <input type="text" name="myname"></p>
            <p><input type="submit"></p>
        </form>
        '''

@app.route('/page2/')
def page2():
    if 'name' in session:
        return 'Hello %s!' % session['name']
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)