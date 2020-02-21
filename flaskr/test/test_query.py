from unittest import TestCase

from src.database.DBconnector import *


class TestQuery(TestCase):
    def test_query(self):
        db = DBconnector()
        db.insert_new_highscore("test", 1000, [1, 2, 3, "4"])
        r = db.get_highscore()
        assert r[0][0] == "test"
        assert r[0][1] == 1000

    def test_get_submission_ranking(self):
        db = DBconnector()
        res = db.get_submission_ranking(1)
        print(res)