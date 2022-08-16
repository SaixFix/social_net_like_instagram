from flask import Blueprint, jsonify
from app.dao.posts_dao import PostsDAO
import logging

endpoint_blueprint = Blueprint('endpoint_blueprint', __name__, template_folder='templates')

# создаем DAO
posts_dao = PostsDAO("./data/data.json")

# Создаем логирование
logging.basicConfig(filename="api.log", level=logging.INFO, encoding="utf-8",
                    format=f'%(asctime)s %(levelname)s : %(message)s')


@endpoint_blueprint.route('/api/posts/')
def api_endpoint_page():
    """
    Страница возвращает полный список постов в виде JSON-списка
    """
    logging.info("Запрос")
    data = posts_dao.get_all()
    return jsonify(data)


@endpoint_blueprint.route('/api/posts/<int:post_id>')
def api_endpoint_post_page(post_id):
    """
    Страница возвращает пост по номеру в виде JSON-словаря
    """
    logging.info("Запрос")
    data = posts_dao.get_post_by_pk(post_id)
    return jsonify(data)
