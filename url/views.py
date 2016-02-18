from flask import render_template, flash, redirect, request
from url import app, db
from url.models import URLMap
from urllib2 import urlopen

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        longURL = request.form['longURL']
        shortURL = request.form['shortURL']
        ret = urlopen(longURL)
        if ret.code >= 400:
            # try adding http
            longURL = 'http://' + longURL
            ret = urlopen(longURL)
            if ret.code >= 400:
                return render_template('index.html', error=error)# ERROR

        url = URLMap(longURL=longURL, shortURL=shortURL)
        db.session.add(url)
        db.session.commit()
        flash("loL!!!!")
        return render_template('index.html', url=url)

@app.route('/<url>', methods=['GET'])
def red(url):
    if request.method == 'GET':
        url_map = URLMap.query.filter_by(shortURL=url).first()
        youareel = url_map.longURL
        #return youareel
        return redirect(youareel)


def url_to_json(url):
    return {'id': url.id,
            'longURL': url.longURL,
            'shortURL': url.shortURL }
