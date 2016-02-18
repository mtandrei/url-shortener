from url import db

class URLMap(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    longURL = db.Column(db.String(500), index=True, unique=True)
    shortURL = db.Column(db.String(20), index=True, unique=True)

    def __repr__(self):
        return '<Long URL: %r, Short URL: %r>' % (self.longURL, self.shortURL)


