from unittest import TestCase

from src.database.con import *


class TestQuery(TestCase):
    def test_query(self):
        drop_table()
        create_database()
        insert_new_highscore("test", 1000, [1, 2, 3, "4"])
        res = get_highscore()
        r = json.loads(res)
        assert r[0][0] == "test"
        assert r[0][1] == 1000

