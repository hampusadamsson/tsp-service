import json
from unittest import TestCase

from src.Configuration import Configuration
from src.application import app
from src.game.tsp.tsp import Tsp


class TestSubmitSolution(TestCase):
    def test_post(self):
        tsp = Tsp(Configuration().problem)
        with app.test_client() as client:
            data = dict(user="dummy", solution=json.dumps(list(range(len(tsp.solution)))))
            res = client.post('/submitSolution', data=data)
        res = json.loads(res.data.decode('utf8'))
        print(res)
        assert int(res['distance']) > 1


    def test_highscore(self):
        with app.test_client() as client:
            client.set_cookie('localhost', 'username', 'FlaskTest1')
            res = client.get('/getHighscore')
        res = json.loads(res.data.decode('utf8'))
        assert res[0][0] == 'test1'
