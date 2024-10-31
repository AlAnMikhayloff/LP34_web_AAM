from webapp.db import db


class UserDataSet(db.Model):
    id_name = db.Column(db.Integer, primary_key=True)
    Name_of_the_feature = db.Column(db.String(50), index=True, unique=True)
    Frequency_of_manifestation_of_the_feature_of_candidate_1 = db.Column(db.String(10))
    Frequency_of_manifestation_of_the_feature_of_candidate_2 = db.Column(db.String(10))
    Probability_of_manifestation_of_the_feature_in_candidate_1 = db.Column(db.String(5))
    Probability_of_manifestation_of_the_feature_in_candidate_2 = db.Column(db.String(5))

    def __repr__(self):
        return '<News {} {}>'.format(self.title, self.url)
