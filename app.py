from flask import Flask, render_template, url_for, redirect
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

@app.route('/posts')
def posts():
    return render_template('posts.html')


@app.route('/project/<project>')
def project(project):
    if Path("./static/project/" + project + ".md").is_file():
        file = open('./static/project/' + project + ".md", 'r')
        string = '<base target="_blank"> '
        string += markdown.markdown(
            file.read(), extensions=["fenced_code"]
        )
        return render_template('project.html', title=project, content=string)
    else:
        return redirect(url_for('projects'))


@app.route('/post/<post>')
def post(post):
    if Path("./static/posts/" + post + ".md").is_file():
        file = open('./static/posts/' + post + ".md", 'r')
        string = '<base target="_blank"> '
        string += markdown.markdown(
            file.read(), extensions=["fenced_code"]
        )
        return render_template('post.html', title=project, content=string)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
