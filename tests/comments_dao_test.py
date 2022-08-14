from app.dao.comments_dao import CommentsDAO

import pytest


@pytest.fixture()
def comments_dao():
    comments_dao_instance = CommentsDAO("./data/comments.json")
    return comments_dao_instance


# ожидаемые ключи
keys_should_be = {'post_id', 'commenter_name', 'comment', 'pk'}


class TestCommentsDAO:

    def test_load_data(self, comments_dao):
        """
        проверяем читается ли файл
        """
        data = comments_dao.load_data()
        assert type(data) == list, "возвращается не список"
        assert len(data) > 0, "возвращается пустой список"
        assert set(data[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_comments_by_post_id(self, comments_dao):
        """
        проверяет возвращается ли список коментариев при поиске по id
        """
        comments = comments_dao.get_comments_by_post_id(1)
        assert comments != ValueError, "такого поста нет или у него нет комментариев"

