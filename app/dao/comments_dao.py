import json


class CommentsDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self) -> list[dict]:
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_comments_by_post_id(self, post_id: int) -> list[dict]:
        """
        возвращает коментарии определенного поста или ошибку если такого пользователя нет или цу него нет постов
        """
        all_comments = self.load_data()
        comments = []

        for comment in all_comments:
            current_comment = comment['post_id']
            if current_comment == post_id:
                comments.append(comment)

        if len(comments) == 0 or type(post_id) != int:
            raise ValueError("такого поста нет или у него нет комментариев")
        else:
            return comments
