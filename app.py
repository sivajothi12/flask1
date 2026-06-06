from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', name="Sivajothi")
@app.route('/about')
def about():
    return render_template('about.html', message="This is the About Page")
@app.route('/contact')
def contact():
    return render_template('contact.html', email="sivajothi@example.com")
if __name__ == '__main__':
    app.run(debug=True)
