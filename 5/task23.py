# todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов
#
# #========================================
# Flask маршруты для страниц
# Вот пример добавления маршрутов во Flask для страниц "О компании", "Контакты" и "Список постов":

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Главная страница"""
    return render_template('index.html')


@app.route('/about')
def about():
    """Страница 'О компании'"""
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    """Страница 'Контакты'"""
    return render_template('contacts.html')


@app.route('/posts')
def posts():
    """Страница 'Список постов'"""
    # Пример данных — обычно берутся из базы данных
    posts_list = [
        {'id': 1, 'title': 'Первый пост', 'text': 'Содержимое первого поста'},
        {'id': 2, 'title': 'Второй пост', 'text': 'Содержимое второго поста'},
        {'id': 3, 'title': 'Третий пост', 'text': 'Содержимое третьего поста'},
    ]
    return render_template('posts.html', posts=posts_list)


if __name__ == '__main__':
    app.run(debug=True)
