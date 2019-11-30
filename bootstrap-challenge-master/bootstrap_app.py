
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#* Dependencies *#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
import pandas as pd
import numpy as np
import colors

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify, redirect, url_for, request, g

import time
import datetime
from rfc3339 import rfc3339

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#* SQLAlchemy Use Dependencies *#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
engine = create_engine(
    "mysql+mysqlconnector://nicolespaar:nicolespaar@127.0.0.1:3306/comments")

Base = automap_base()
Base.prepare(engine, reflect=True)

Comment = Base.classes.comments
ChannelMetadata = Base.classes.channelMetadata
Rating = Base.classes.ratings
ShootMetadata = Base.classes.shootMetadata
ShootTag = Base.classes.shootTags
ShootPerformer = Base.classes.shootPerformers
ChannelTag = Base.classes.channelTags

session = Session(engine)

app = Flask(__name__)

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#* Route Hooks *#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
@app.route('/')
def Landing():
    return redirect(url_for('static', filename='index.html'))


@app.route('/plots')
def Plots():
    return redirect(url_for('static', filename='plots.html'))


@app.route('/comps')
def Comps():
    return redirect(url_for('static', filename='comps.html'))


@app.route('/data')
def Data():
    #df = pd.read_csv('Polished_Weather_Data.csv')
    # df.to_html('datatable.htm')
    #testtable = df.to_html()
    return redirect(url_for('static', filename='data.html'))

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


@app.route('/temps')
def temps():
    return redirect(url_for('static', filename='temps.html'))


@app.route('/humidity')
def humidity():
    return redirect(url_for('static', filename='humidity.html'))


@app.route('/clouds')
def clouds():
    return redirect(url_for('static', filename='clouds.html'))


@app.route('/winds')
def winds():
    return redirect(url_for('static', filename='winds.html'))

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#* WeatherPy Operations *#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#* Debugging *#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
@app.before_request
def start_timer():
    g.start = time.time()


@app.after_request
def log_request(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response

    now = time.time()
    duration = round(now - g.start, 2)
    dt = datetime.datetime.fromtimestamp(now)
    timestamp = rfc3339(dt, utc=True)

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]
    args = dict(request.args)

    log_params = [('method', request.method, 'blue'),
                  ('path', request.path, 'blue'),
                  ('status', response.status_code, 'yellow'),
                  ('duration', duration, 'green'),
                  ('time', timestamp, 'magenta'), ('ip', ip, 'red'),
                  ('host', host, 'red'), ('params', args, 'blue')]

    request_id = request.headers.get('X-Request-ID')
    if request_id:
        log_params.append(('request_id', request_id, 'yellow'))

    parts = []
    for name, value, color in log_params:
        part = colors.color("{}={}".format(name, value), fg=color)
        parts.append(part)
    line = " ".join(parts)

    app.logger.info(line)

    return response


if __name__ == "__main__":
    app.run(debug=True)

# You must use bootstrap. This includes using the bootstrap navbar component for the header
# on every page, the bootstrap table component for the data page, and the bootstrap grid
# for responsiveness on the comparison page.

# You must deploy your website to GitHub pages, with the website working on a live, publicly
# accessible URL as a result.

# Be sure to use a CSS media query for the navigation menu.

# Be sure your website works at all window widths/sizes.
