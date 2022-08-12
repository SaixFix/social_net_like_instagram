import json


class PostsDao:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_all(self):
        posts = self.load_data()
        return posts

    def get_posts_by_user(self, user_name):
        all_posts = self.load_data()
        user_posts = []
        name_lower = user_name.lower()

        for post in all_posts:
            current_post = post['poster_name'].lower()
            if current_post == name_lower:
                user_posts.append(post)


find_post = PostsDao("./data/data.json")
print(find_post.get_all())

