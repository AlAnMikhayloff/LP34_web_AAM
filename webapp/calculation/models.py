from datetime import datetime

from webapp.db import db


class UserDataSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_the_feature = db.Column(db.String(50), index=True, unique=True)
    frequency_1 = db.Column(db.String(10))
    frequency_2 = db.Column(db.String(10))
    probability_1 = db.Column(db.String(5))
    probability_2 = db.Column(db.String(5))
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True,
    )

    def __repr__(self):
        return '<UserDataSet {} {} {}>'.format(self.name_of_the_feature, self.probability_1, self.probability_2)
