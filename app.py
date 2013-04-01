import os

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {'author': {'nickname': "Steve"},
         'body': 'Fuck you, Josh'},
        {'author': {'nickname': "Josh"},
         'body': 'Steve is an asshole!'}
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
