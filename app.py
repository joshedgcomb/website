import os

from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template('404.html')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
