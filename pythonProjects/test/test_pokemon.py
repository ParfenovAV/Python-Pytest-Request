import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '22e465133abff771c451311117703012'
HEADER = {  'Content-type': 'application/json',  'trainer_token': TOKEN}
TRAINER_ID=18386

def test_status_cod():
    response =requests.get(url=f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200


def test_name():
    response_name=requests.get(url=f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_name.json()["data"][0]["trainer_name"] == 'ParfenovAndrey'


@pytest.mark.parametrize('key, value', )