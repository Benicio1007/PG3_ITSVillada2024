import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
API_URL = "https://jsonplaceholder.typicode.com/posts"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'create':
            return redirect(url_for('create_post'))
        elif action == 'update':
            return redirect(url_for('update_post'))
        elif action == 'search_by_id':
            return redirect(url_for('search_by_id'))
        elif action == 'search_logical':
            return redirect(url_for('search_logical'))
        elif action == 'show_table':
            return redirect(url_for('show_table'))

    response = requests.get(API_URL)
    if response.status_code == 200:
        posts = response.json()
        return render_template('index.html', posts=posts)
    else:
        return "Hubo un error al recuperar las publicaciones."

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        user_id = request.form['user_id']
        post_data = {
            'title': title,
            'body': body,
            'userId': int(user_id)
        }
        response = requests.post(API_URL, json=post_data)
        if response.status_code == 201:
            return redirect(url_for('index'))
        else:
            return "Hubo un error al crear la publicación."
    return render_template('create_post.html')

@app.route('/update', methods=['GET', 'POST'])
def update_post():
    if request.method == 'POST':
        post_id = request.form['post_id']
        title = request.form['title']
        body = request.form['body']
        put_data = {
            'id': int(post_id),
            'title': title,
            'body': body,
        }
        response = requests.put(f"{API_URL}/{post_id}", json=put_data)
        if response.status_code == 200:
            return redirect(url_for('index'))
        else:
            return "Hubo un error al actualizar la publicación."
    return render_template('update_post.html')

@app.route('/search_by_id', methods=['GET', 'POST'])
def search_by_id():
    if request.method == 'POST':
        post_id = request.form['post_id']
        response = requests.get(f"{API_URL}/{post_id}")
        if response.status_code == 200:
            post = response.json()
            return render_template('show_post.html', post=post)
        else:
            return "No se encontró ninguna publicación con ese ID."
    return render_template('search_by_id.html')

@app.route('/search_logical', methods=['GET', 'POST'])
def search_logical():
    if request.method == 'POST':
        keyword = request.form['keyword']
        response = requests.get(API_URL)
        if response.status_code == 200:
            posts = response.json()
            filtered_posts = [post for post in posts if keyword.lower() in post['title'].lower() or keyword.lower() in post['body'].lower()]
            return render_template('index.html', posts=filtered_posts)
        else:
            return "Hubo un error al recuperar las publicaciones."
    return render_template('search_logical.html')

@app.route('/show_table')
def show_table():
    response = requests.get(API_URL)
    if response.status_code == 200:
        posts = response.json()
        return render_template('index.html', posts=posts)
    else:
        return "Hubo un error al recuperar las publicaciones."

if __name__ == "__main__":
    app.run()
