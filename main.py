from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# サンプルのブログ記事
blog_posts = [
    {"title": "初めての投稿", "content": "これは最初のブログ投稿です。"},
    {"title": "Flaskでブログ作成", "content": "Flaskを使用してブログを作成しています。"},
]

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = blog_posts[post_id - 1]
    return render_template('post.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = {"title": title, "content": content}
        blog_posts.append(new_post)
        return redirect(url_for('index'))
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
