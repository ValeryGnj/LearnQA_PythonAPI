import pytest
import requests

class TestFirstApi:
    names = [
        ('Valery'),
        ('Vitaliy'),
        ('Semen'),
        ('')
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name": name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, 'Wrong status code'

        response_dict = response.json()
        assert "answer" in response_dict, "Where is no field 'answer' in response"

        if len(name) == 0:
            expected_responce_text = 'Hello, someone'
        else:
            expected_responce_text = f"Hello, {name}"
            
        actual_response_text = response_dict['answer']
        assert expected_responce_text == actual_response_text, 'Actual text is not correct'

