from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Todo Page
@app.route('/todo')
def todo():

    task = request.args.get('task')

    return render_template('todo.html', task=task)

app.run(debug=True)
