from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Articles(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False, unique=True)
    lead = db.Column(db.String)
    body = db.Column(db.String)
    time = db.Column(db.DateTime)
    author = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __init__(self, author, title, slug, lead, body, time):
        self.author = author
        self.title = title
        self.slug = slug
        self.lead = lead
        self.body = body
        self.time = time

    def get_articles_by_author(self):
        return self.query.filter_by(author=self.author)

    def get_articles_by_title(self):
        return self.query.filter_by(title=self.title)


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)
    author = db.relationship(
        'Articles',
        primaryjoin=(Articles.author == id),
        backref='article')

    def __init__(self, id, name, bio):
        self.id = id
        self.name = name
        self.bio = bio


class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    ip = db.Column(db.String)
    method = db.Column(db.String)
    status = db.Column(db.String)
    time = db.Column(db.DateTime)

    def __init__(self, id, ip, method, status, time):
        self.id = id
        self.ip = ip
        self.method = method
        self.status = status
        self.time = time


Articles.authors = db.relationship(
    'Author',
    backref='authors')
