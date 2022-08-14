from flask import Blueprint, request, render_template
import logging
from app.dao.posts_dao import PostsDAO
#создаем блюпринт
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

#создаем DAO
posts_dao = PostsDAO("./data/data.json")


@main_blueprint.route('/')
def main_page():
    """
    Главная страница
    """
    posts = posts_dao.get_all()
    return render_template('index.html', posts=posts)

#
# @main_blueprint.route('/search')
# def search_page()
