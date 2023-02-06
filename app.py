from flask import Flask, render_template
from flaskext.markdown import Markdown
import markdown.extensions.fenced_code
from pathlib import Path

app = Flask(__name__)
Markdown(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/post/<post>')
def post(post):
    if Path("./static/markdown/" + post + ".md").is_file():
        file = open('./static/markdown/' + post + ".md", 'r')
        string = markdown.markdown(
            file.read(), extensions=["fenced_code"]
        )
        return render_template('post.html', title=post, content=string)
    else:
        return render_template('post.html')


if __name__ == '__main__':
    app.run()
