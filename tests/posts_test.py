class TestPosts:

    def test_single_post_status(self, test_client):
        """ Проверяем при запросе по номеру поста нужный статус-код """
        response = test_client.get('/posts/1', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса кандидата не корректный"
