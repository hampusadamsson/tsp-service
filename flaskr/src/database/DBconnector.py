import datetime

import sqlalchemy as db
from sqlalchemy import func, and_

from src.Configuration import Configuration


class DBconnector():
    def __init__(self):
        # engine = db.create_engine('dialect+driver://user:pass@host:port/db')
        db_path = Configuration().path_to_db
        engine = db.create_engine('sqlite:///{}'.format(db_path))
        self.connection = engine.connect()
        metadata = db.MetaData()

        self.highscore = db.Table('highscore', metadata,
                           db.Column('Id', db.Integer(), primary_key=True, autoincrement=True),
                           db.Column('name', db.String(255), nullable=False),
                           db.Column('datetime', db.String(255), nullable=False),
                           db.Column('score', db.Float(), nullable=False),
                           db.Column('solution', db.String(1080), )
                           )

        metadata.create_all(engine)

    def insert_new_highscore(self, name, score, solution):
        solution = [int(s) for s in solution]
        dateandtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        query = db.insert(self.highscore).values(name=name,
                                          score=score,
                                          datetime=dateandtime,
                                          solution=str(solution))
        self.connection.execute(query)
        return self.get_submission_ranking(score)

    def get_highscore(self):
        results = db.select([self.highscore.columns.name,
                             self.highscore.columns.score,
                             self.highscore.columns.datetime]).order_by(self.highscore.columns.score).limit(100)
        return self.connection.execute(results).fetchall()

    def get_submission_ranking(self, score):
        results = db.select([func.count(self.highscore.columns.name)],
                            and_(self.highscore.columns.score < score)
                          )
        res = self.connection.execute(results).fetchall()
        rank = res[0][0]+1
        return rank
