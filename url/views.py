from flask import render_template, flash, redirect, request, url_for
from url import app, db
from url.models import URLMap
from urllib2 import urlopen
import random 

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        longURL = request.form['longURL']
        shortURL = request.form['shortURL']
        # Try adding prefix
        if not longURL.startswith('http://') and not longURL.startswith('https://'):
            longURL = 'http://' + longURL

        ret = urlopen(longURL)
        if ret.code >= 400:
            return render_template('index.html', error=error)# ERROR

        if shortURL == "":
            shortURL = get_random_string()

        url = URLMap(longURL=longURL, shortURL=shortURL)
        db.session.add(url)
        db.session.commit()
        flash("Your shortened URL is " + url_for('red', url=shortURL, _external=True))
        return render_template('index.html', url=url)

@app.route('/<url>', methods=['GET'])
def red(url):
    if request.method == 'GET':
        url_map = URLMap.query.filter_by(shortURL=url).first()
        if url_map is None:
            return render_template('error.html')
        return redirect(url_map.longURL)


def get_random_string(length=7,allowed_chars='abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    return ''.join(random.choice(allowed_chars) for i in range(length))
