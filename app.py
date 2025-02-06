from flask import Flask, render_template, url_for, send_from_directory
import os

app = Flask(__name__)

# Serve static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# Define routes for each template
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/opensource')
def opensource():
    return render_template('opensource.html')

@app.route('/books')
def books():
    return render_template('books.html')


if __name__ == '__main__':
    app.run(debug=True)