from models.user import db

class Day(db.Model):
    __tablename__ = "day"
    id = db.Column(db.Integer, primary_key = True)
    textcontent = db.Column(db.Text)

    # connect day to user
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, textcontent, user_id):
        self.textcontent = textcontent
        self.user_id = user_id


class Week(db.Model):
    __tablename__ = "week"
    id = db.Column(db.Integer, primary_key = True)
    textcontent = db.Column(db.Text)

    # connect day to user
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, textcontent, user_id):
        self.textcontent = textcontent
        self.user_id = user_id


class Month(db.Model):
    __tablename__ = "month"
    id = db.Column(db.Integer, primary_key = True)
    textcontent = db.Column(db.Text)

    # connect day to user
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, textcontent, user_id):
        self.textcontent = textcontent
        self.user_id = user_id


class Year(db.Model):
    __tablename__ = "year"
    id = db.Column(db.Integer, primary_key = True)
    textcontent = db.Column(db.Text)

    # connect day to user
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, textcontent, user_id):
        self.textcontent = textcontent
        self.user_id = user_id


class Decade(db.Model):
    __tablename__ = "decade"
    id = db.Column(db.Integer, primary_key = True)
    textcontent = db.Column(db.Text)

    # connect day to user
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, textcontent, user_id):
        self.textcontent = textcontent
        self.user_id = user_id