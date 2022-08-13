from app.dao.posts_dao import PostsDAO

import pytest


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO("./data/data.json")
    return posts_dao_instance


# ожидаемые ключи
keys_should_be = {'poster_name', 'poster_avatar', 'pic',
                  'content', 'views_count', 'likes_count', 'pk'}


class TestPostsDAO:

    def test_get_all(self, posts_dao):
        """
        проверяем верный ли список возвращается
        """
        posts = posts_dao.get_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_post_by_pk(self, posts_dao):
        """
        проверяем верный ли пост возвращается при запросе по pk
        """
        post = posts_dao.get_post_by_pk(1)
        assert (post['pk'] == 1), "возвращается неправильный кандидат"
        assert set(post.keys()) == keys_should_be, "неверный список ключей"

    def test_get_posts_by_user(self, posts_dao):
        """
        проверяем верный ли список постов возвращается при запросе по имени
        """
        user_by_pk = posts_dao.get_post_by_pk(1)
        posts_by_name = posts_dao.get_posts_by_user(user_by_pk['poster_name'])
        assert posts_by_name != ValueError, "такого пользователя нет или у него нет постов"

    def test_search_for_posts(self, posts_dao):
        """
        проверяем верный ли список постов возвращается при запросе по ключевому слову
        """
        posts = posts_dao.search_for_posts('на')
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"






