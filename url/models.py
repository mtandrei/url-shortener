from url import db


class URLMap(db.Model):
    """ Sets up MySQL table for URLMap objects

        URLs are mapped such that shortened URLs must be unique, but long URLs
        do not. The same shortened URL cannot map to multiple actual long URLs.

        :Parameters:
         - 'db.Model': Inherited superclass for URLMap from SQLAlchemy

        :Fields:
         - '__tablename__': MySQL table name definition
         - 'short_url': Unique identifier; used to redirect to long_url
         - 'long_url': The URL to shorten
    """
    __tablename__ = 'urls'
    short_url = db.Column(db.String(20), primary_key=True, index=True)
    long_url = db.Column(db.String(500), index=True)
