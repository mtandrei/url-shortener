from flask import render_template, flash, redirect, request, url_for
from url import app, db
from url.models import URLMap
from urllib2 import urlopen
import random

ALLOWED_CHARS = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
DEFAULT_LENGTH = 7


@app.route('/', methods=['POST', 'GET'])
def index():
    """Handles URL input and webpage rendering

    On GET: Renders homepage.

    On POST: Expects a form that contains short_url and long_url to create a
    database record of a mapping between the two.
    """
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        # Grab fields from user form
        long_url = request.form['long_url']
        short_url = request.form['short_url']

        # Verify whether the long_url exists
        long_url = validate_url(long_url)

        # If it doesn't exist, return to homepage with error code
        if long_url == "":
            return render_template('index.html', error=1)

        # If user did not specify custom short_url, generate one randomly
        if short_url == "":
            short_url = gen_random_string()

        # Create and add database record of mapping
        url = URLMap(long_url=long_url, short_url=short_url)
        db.session.add(url)
        db.session.commit()

        # Return successful POST request to homepage
        return render_template('index.html', url=short_url)

    # If bad request, render error page
    return render_template('error.html')


@app.route('/<url>', methods=['GET'])
def red(url):
    """Redirects user from short_url to long_url

    :Parameters:
     - 'url': Short URL used to query for and redirect to long URL

    On GET: Grabs URL Mapping from database and routes accordinly
    """

    if request.method == 'GET':
        url_map = URLMap.query.filter_by(short_url=url).first()

       # If mapping does not exist, render error page
       if url_map is None:
            return render_template('error.html')

        # Returns successful redirect to long_url
        return redirect(url_map.long_url)

    # If bad request, render error page
    return render_template('error.html')


def gen_random_string(len=DEFAULT_LENGTH, allowed_chars=ALLOWED_CHARS):
    """Generates random string

    :Parameters:
     - 'len': Length of random string to generate
     - 'allowed_chars': Characters used in generation

    :Returns:
     String of length len of random characters strictly bounded by allowed_chars
    """
    return ''.join(random.choice(allowed_chars) for i in range(len))


def validate_url(long_url):
    """Checks whether long_url exists. Reformats URL if necessary.

    :Parameters:
     - 'long_url': Long URL to be validated.

    :Returns:
     If valid URL, returns correctly formatted URL. Else, returns empty string.
    """
    # Check format of URL.
    if not long_url.startswith('http://') and not long_url.startswith('https://'):
        long_url = 'http://' + long_url

    # If opening URL fails or return code is above 400, URL is not valid
    try:
        ret = urlopen(long_url)
        if ret.code >= 400:
            long_url = ""
    except:
        long_url = ""

    return long_url
