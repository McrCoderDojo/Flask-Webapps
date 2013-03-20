from flask import Flask, request, url_for, render_template
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return render_template('template8.html', name=request.form['myname'])
    else:
        return '''
        <form name="myform" method="post">
            <p>Your Name: <input type="text" name="myname"></p>
            <p><input type="submit"></p>
        </form>
        '''


if __name__ == '__main__':
    app.run(debug=True)