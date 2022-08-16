import json


class PostsDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self) -> list[dict]:
        """
        читаем из json файла
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_all(self) -> list[dict]:
        """
        возвращает все посты
        """
        posts = self.load_data()
        return posts

    def get_posts_by_user(self, user_name) -> list:
        """
        возвращает посты определенного пользователя или ошибку если такого пользователя нет или цу него нет постов
        """
        all_posts = self.load_data()
        user_posts = []
        name_lower = user_name.lower()

        for post in all_posts:
            current_post = post['poster_name'].lower()
            if current_post == name_lower:
                user_posts.append(post)

        if len(user_posts) == 0 or type(user_name) != str:
            raise ValueError("такого пользователя нет или у него нет постов")
        else:
            return user_posts

    def search_for_posts(self, query: str) -> list:
        """
        возвращает список постов по ключевому слову
        """
        all_posts = self.load_data()
        posts_list = []
        query_lower = query.lower()

        for request in all_posts:
            request_lower = request['content'].lower()
            if query_lower in request_lower:
                posts_list.append(request)

        return posts_list

    def get_post_by_pk(self, pk) -> dict:
        """
        возвращает один пост по его идентификатору
        """
        all_posts = self.load_data()

        for post in all_posts:
            if pk == post['pk']:
                return post

