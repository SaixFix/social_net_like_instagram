class TestSearch:

    def test_single_candidate_status(self, test_client):
        """ Проверяем при запросе по ключевому слову нужный статус-код """
        response = test_client.get('/search/?s=все', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса кандидата не корректный"
