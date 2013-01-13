import os
from flask import Flask
from flask import render_template
from flask_flatpages import FlatPages

DEBUG = False
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

def _get_posts():
    posts = []
    for path, page in pages._pages.items():
        if path.startswith('posts'):
            posts.append(page)
    return posts

@app.route("/")
def index():
    return static_page('home')

@app.route("/blog/")
def blog():
    posts = _get_posts()
    page = pages.get_or_404('blog')
    return render_template('blog.html', page=page, posts=posts)

@app.route('/<path:path>/')
def static_page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
