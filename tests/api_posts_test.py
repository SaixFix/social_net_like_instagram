# ожидаемые ключи
keys_should_be = {'poster_name', 'poster_avatar', 'pic',
                  'content', 'views_count', 'likes_count', 'pk'}


class TestAPI:
    """
    Проверяем возвращается ли верный тип данных и нужные ключи
    """
    def test_api_type(self, test_client):
        response = test_client.get('/api/posts/', follow_redirects=True)
        get_response = response.get_json()
        assert type(get_response) == list, "Возвращает не список"
        assert (get_response[0].keys()) == keys_should_be, "неверный список ключей"

    def test_api_single(self, test_client):
        response = test_client.get('/api/posts/1', follow_redirects=True)
        get_response = response.get_json()
        assert type(get_response) == dict, "Возвращает не словарь"
        assert (get_response.keys()) == keys_should_be, "неверный список ключей"
