from flask import Flask, render_template

app = Flask(__name__)

myList = [
    [1, "Welcome", "Welcome to my website! This is currently a test blog post, so check back later to see more :)"],
    [2, "You have found me", "go away"]]


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
    if myList.__len__() > int(post):
        title = myList[int(post)][1];
        content = myList[int(post)][2];
        return render_template('post.html', title=title, content=content)
    else:
        return render_template('post.html')


if __name__ == '__main__':
    app.run()
