from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.sqlite'
app.config['SQLALCHEMY_ECHO'] = True

from database9 import *

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        person = Person(request.form['name'], request.form['age'])
        db.session.add(person)
        db.session.commit()
    people = Person.query.order_by(Person.name).all()
    return render_template('index9.html', people=people)

@app.route('/person/<int:id>/')
def person(id):
    person = Person.query.filter(Person.id == id).first()
    return render_template('person9.html', person=person)

@app.route('/person/delete/<int:id>/')
def delete(id):
    Person.query.filter(Person.id == id).delete()
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/person/edit/<int:id>/', methods=['POST', 'GET'])
def edit(id):
    person = Person.query.filter(Person.id == id).first()

    if request.method == 'POST':
        person.name = request.form['name']
        person.age = request.form['age']
        db.session.commit()

    return render_template('edit9.html', person=person)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
