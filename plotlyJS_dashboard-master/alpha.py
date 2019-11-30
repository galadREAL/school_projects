ascii = '''
#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8
#?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&
#@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #

                   @@@@@@      @@@@@@@       @@@@@@       @@@@@@      @@@@@@@
                  @@@@@@@      @@@@@@@@     @@@@@@@@     @@@@@@@@     @@@@@@@@
                  !@@          @@!  @@@     @@!  @@@     @@!  @@@     @@!  @@@
                  !@!          !@!  @!@     !@!  @!@     !@!  @!@     !@!  @!@
                  !!@@!!       @!@@!@!      @!@!@!@!     @!@!@!@!     @!@!!@!
                   !!@!!!      !!@!!!       !!!@!!!!     !!!@!!!!     !!@!@!
                       !:!     !!:          !!:  !!!     !!:  !!!     !!: :!!
                      !:!      :!:          :!:  !:!     :!:  !:!     :!:  !:!
                  :::: ::       ::          ::   :::     ::   :::     ::   :::
                  :: : :        :            :   : :      :   : :      :   : :

# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*
#?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&
#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8
'''

print(ascii)

#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
# *                                                                                               * #
#? * * * * * * * * * * * * *  * * / Dashboarding with Plotly.js: Setup / * * * * * * * * * * * * * *@
# *                                                                                               * #
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@
#? * * * * * * * * * * * * * * * / Dependencies + Decleration Methods / * * * * * * * * * * * * * * *@
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @

#* Dependencies: SQL Alchemy *#
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

#* Dependencies: Flask Web Framework *#
from flask import Flask, jsonify, render_template, g, request
from flask_sqlalchemy import SQLAlchemy

#* Dependencies: Misc. & Debugging *#
import pandas as pd
import colors
import time
import datetime
from rfc3339 import rfc3339
app = Flask(__name__)

#* Inits needed for Flask framework *#
def inits():
    '''
        inits() initializes and returns aliases for each table in our SQLite database, as well as a
    our session engine to query it later on.
    '''
    engine = create_engine("sqlite:///data/bellybutton.sqlite")
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Metadata = Base.classes.sample_metadata
    Samples = Base.classes.samples
    session = Session(engine)
    return Metadata, Samples, session



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@
#? * * * * * * * * * * * * * * * * * / Initialization Of Constants / * * * * * * * * * * * * * * * * @
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @

Metadata, Samples, session = inits()



#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
# *                                                                                               * #
#? * * * * * * * * * * * * * * * * * * * / Method Library / * * * * * * * * * * * * * * * * * * * * @
# *                                                                                               * #
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @
#? * * * * * * *  * * * * * * / Returning all Available Sample Names / * * * * * * * * * * * * * * *@
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@

def get_names():
    '''
        get_names() converts a short SQL Alchemy query into its raw and unwrapped counterpart. Next,
    Pandas executes the query with the help of a bound session, and then puts the output into a new
    DataFrame. We then list out and assign to a variable the values within the DataFrame by column
    before returning it to the main.
    '''
    names_sql_statement = session.query(Samples).statement
    df = pd.read_sql_query(names_sql_statement, session.bind)
    dump = list(df.columns)[2:]
    return dump



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @
#? * * * * * * * * * / Returning all Required Metadata Fields for Specified Sample / * * * * * * * *@
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@

def get_single_metadata(sample):
    '''
        get_single_metadata() receives the user selected sample, and then queries the SQLite
    database's table "Metadata" for all fields listed in the "sel" list for just it. The output is assigned to
    a variable "dump" and then returned to the main.
    '''
    sel = [
        Metadata.sample,
        Metadata.ETHNICITY,
        Metadata.GENDER,
        Metadata.AGE,
        Metadata.LOCATION,
        Metadata.BBTYPE,
        Metadata.WFREQ,
    ]
    results = session.query(*sel).filter(Metadata.sample == sample).all()
    dump = {}
    for field in results:
        dump["sample"] = field[0]
        dump["ETHNICITY"] = field[1]
        dump["GENDER"] = field[2]
        dump["AGE"] = field[3]
        dump["LOCATION"] = field[4]
        dump["BBTYPE"] = field[5]
        dump["WFREQ"] = field[6]
    return dump



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @
#? * * * * * * * * / Returning all Available Identity Values for Specified Sample / * * * * * * * * @
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@

def get_single_identities(sample):
    '''
        get_single_identities() recieves the user selected sample, and then queries the SQLite
    database's table "Samples" for both fields available to put into a DataFrame. Next the user's
    selected sample is filtered from the raw DataFrame, and the DataFrame is then sorted by the
    sample's values descending, and limited to the first 10 entries. It is finally returned to the
    main after a new element of all of the sample's values are casted to a list.
    '''
    sample_sql = session.query(Samples).statement
    df = pd.read_sql_query(sample_sql, session.bind)
    sample_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]
    sample_data_slice = sample_data.sort_values(by=sample, ascending=False).head(10)
    dump = {
        "otu_ids": sample_data_slice.otu_id.values.tolist(),
        "sample_values": sample_data_slice[sample].values.tolist(),
        "otu_labels": sample_data_slice.otu_label.tolist()
    }
    return dump



#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
# *                                                                                               * #
#? * * * * * * * * * * * * * * * * * * / Flask Web Framewerkz / * * * * * * * * * * * * * * * * * * @
# *                                                                                               * #
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@
#? * * * * * * * * * * * * * * * * / Route Hooking Infrastructure / * * * * * * * * * * * * * * * * *@
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @

@app.route("/")
def index():
    '''
        index() renders the index.html template.
    '''
    return render_template("index.html")


@app.route("/names")
def names_dump():
    '''
        names_dump() executes get_names() and returns the output as a json.
    '''
    names = get_names()
    return jsonify(names)


@app.route("/metadata/<sample>")
def metadata_dump(sample):
    '''
        metadata_dump() receives the user's selected sample and executes get_single_metadata() with
    it. It returns the output as a json.
    '''
    metadata = get_single_metadata(sample)
    return jsonify(metadata)


@app.route("/samples/<sample>")
def identities_dump(sample):
    '''
        identities_dump() receives the user's selected sample and executes get_single_identities()
    with it. It returns the output as a json.
    '''
    identities = get_single_identities(sample)
    return jsonify(identities)



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@
#? * * * * * * * * * * * * * * * * * * * / Debugging Stuffs / * * * * * * * * * * * * * * * * * * * *@
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @

@app.before_request
def start_timer():
    g.start = time.time()


@app.after_request
def log_request(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response
    ############################################
    now = time.time()
    duration = round(now - g.start, 2)
    dt = datetime.datetime.fromtimestamp(now)
    timestamp = rfc3339(dt, utc=True)
    ############################################
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]
    args = dict(request.args)
    ############################################
    log_params = [('method', request.method, 'blue'),
                  ('path', request.path, 'blue'),
                  ('status', response.status_code, 'yellow'),
                  ('duration', duration, 'green'),
                  ('time', timestamp, 'magenta'), ('ip', ip, 'red'),
                  ('host', host, 'red'), ('params', args, 'blue')]
    ############################################
    request_id = request.headers.get('X-Request-ID')
    if request_id:
        log_params.append(('request_id', request_id, 'yellow'))
    ############################################
    parts = []
    for name, value, color in log_params:
        part = colors.color("{}={}".format(name, value), fg=color)
        parts.append(part)
    line = " ".join(parts)
    ############################################
    app.logger.info(line)
    ############################################
    return response


if __name__ == "__main__":
    app.run(debug=True)