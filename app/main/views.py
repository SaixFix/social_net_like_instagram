from flask import Blueprint, request, render_template
import logging
from app.dao.posts_dao import PostsDAO
from app.dao.comments_dao import CommentsDAO
#создаем блюпринт
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

#создаем DAO
posts_dao = PostsDAO("./data/data.json")
comments_dao = CommentsDAO("./data/comments.json")


@main_blueprint.route('/')
def main_page():
    """
    Главная страница
    """
    posts = posts_dao.get_all()
    return render_template('index.html', posts=posts)


@main_blueprint.route('/posts/<int:postid>')
def post_page(postid):
    """
    Страница одного поста
    """
    comments = comments_dao.get_comments_by_post_id(postid)
    post = posts_dao.get_post_by_pk(postid)
    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route('/search/')
def search_page():

    s = request.args['s']
    posts = posts_dao.search_for_posts(s)
    return render_template('search.html', posts=posts, request=request)




