from datetime import datetime

from webapp.db import db


class UserDataSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_the_feature = db.Column(db.String(50))
    n_samples = db.Column(db.String(10))
    n_features = db.Column(db.String(10))
    applicant = db.Column(db.String(5))
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True,
    )

    def __repr__(self):
        return '<UserDataSet {} {} {} {}>'.format(
                                                  self.name_of_the_feature,
                                                  self.n_samples,
                                                  self.n_features,
                                                  self.applicant,
                                                 )
