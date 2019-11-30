from flask import Flask, jsonify, redirect, url_for, render_template, request, flash, escape, g
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime
import time

import colors
from rfc3339 import rfc3339

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)
prevYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)


# Define what to do when a user hits the index route
@app.route("/", methods=['GET'])
def home():
    return redirect(url_for('static', filename='index.html'))


@app.route("/api/v1.0/precipitation")
def precip():
    # Build the query.
    prevYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precip_results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prevYear).all()

    # Convert the query results to a Dictionary using date as the key and prcp as the value.
    all_precip_stats = []
    for date, precipitation in precip_results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["precipitation"] = precipitation
        all_precip_stats.append(precip_dict)

    # Return the JSON representation of your dictionary.
    return jsonify(all_precip_stats)


@app.route("/api/v1.0/stations")
def stations():
    # Build the query.
    station_results = session.query(
        Measurement.station, func.count(Measurement.station)).group_by(
            Measurement.station).order_by(
                func.count(Measurement.station).desc()).all()

    # Convert the query results to a Dictionary.
    all_station_stats = []
    for station, reports in station_results:
        station_dict = {}
        station_dict['station'] = station
        station_dict['reports'] = reports
        all_station_stats.append(station_dict)

    # Return a JSON list of stations from the dataset.
    return jsonify(all_station_stats)


@app.route("/api/v1.0/tobs")
def tobs():
    activeStations = session.query(
        Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    topStation = str([station[0] for station in activeStations[:1]])
    topStation = "".join(e for e in topStation if e.isalnum())
    # Build the query for the dates and temperature observations from a year from the last data point.
    tobs_results = session.query(Measurement.date, Measurement.tobs).\
        filter_by(station=topStation).filter(
            Measurement.date >= prevYear).all()

    # Convert the query results to a Dictionary.
    all_tobs_stats = []
    for date, tobs in tobs_results:
        tobs_dict = {}
        tobs_dict['date'] = date
        tobs_dict['tobs'] = tobs
        all_tobs_stats.append(tobs_dict)

    # Return a JSON list of Temperature Observations (tobs) for the previous year.
    return jsonify(all_tobs_stats)


# ---------------------------------------------------
app.secret_key = 'testestest'


@app.route('/search', methods=['GET'])
def render_search():
    return render_template('datesearch.html')


@app.route("/search", methods=['POST'])
def form():
    app.logger.info('form(): %s', request)
    try:
        if request.method == "POST":
            results = start_end(request.form['start_date'],
                                request.form['end_date'])
            return render_template('datesearch.html', results=results)

        return render_template('datesearch.html')
    except Exception as e:
        app.logger.error('error: %s', e)
        return render_template('datesearch.html', error=e)



#def method_name():
#    pass




def start_end(start_date, end_date):
    app.logger.info('start_end(): %s', request)

    def calc_temps_se(start_date, end_date):
        return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start_date).filter(
                Measurement.date <= end_date).all()

    # Build the query.
    se_results = calc_temps_se(start_date, end_date)
    # Convert the query results to a Dictionary.
    all_se_stats = []
    for se_min, se_avg, se_max in se_results:
        se_dict = {}
        se_dict['min_temp'] = se_min
        se_dict['avg_temp'] = se_avg
        se_dict['max_temp'] = se_max
        all_se_stats.append(se_dict)

    return all_se_stats


@app.route("/api/v1.0/<start_date>")
def start_only(start_date):
    def calc_temps_s(start_date):
        return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()
    # Build the query.
    s_results = calc_temps_s(start_date)
    # Convert the query results to a Dictionary.
    all_s_stats = []
    for s_min, s_avg, s_max in s_results:
        s_dict = {}
        s_dict['min_temp'] = s_min
        s_dict['avg_temp'] = s_avg
        s_dict['max_temp'] = s_max
        all_s_stats.append(s_dict)
    # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    return jsonify(all_s_stats)

@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end2(start_date, end_date):
    app.logger.info('start_end(): %s', request)

    def calc_temps_se(start_date, end_date):
        return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start_date).filter(
                Measurement.date <= end_date).all()

    # Build the query.
    se_results = calc_temps_se(start_date, end_date)
    # Convert the query results to a Dictionary.
    all_se_stats = []
    for se_min, se_avg, se_max in se_results:
        se_dict = {}
        se_dict['min_temp'] = se_min
        se_dict['avg_temp'] = se_avg
        se_dict['max_temp'] = se_max
        all_se_stats.append(se_dict)

    return jsonify(all_se_stats)

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# debugging stuff
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
