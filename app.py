from flask import Flask, jsonify
import datetime as dt #1. May syntax error... I don''t know what I did wrong. huhuhu,
from sqlalchemy.ext.automap import automap_base #2. May ibang bug pa ba once tumakabo ang app.py?
from sqlalchemy.orm import Session
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

base = automap_base()
base.prepare(engine, reflect=True)
precip = base.classes.measurement
stats = base.classes.station

app = Flask(__name__)
@app.route("/")
def home():
     print("Server received request for 'Home' page...") #3. Paano ko magagawa na name instead of path ang nakadisplay sa page? 
         return (
          f"Available Routes:<br/>"
          f"/api/v1.0/precipitation<br/>"
          f"/api/v1.0/stations<br/>"
          f"/api/v1.0/tobs<br/>"
          f"/api/v1.0/pi/v1.0/<start><br/>"
          f"/api/v1.0/<start>/<end>"
     )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(precip.date, precip.prcp).all()
    session.close()
    inches = list(np.ravel(results))

    return jsonify(inches)

@app.route("/api/v1.0/stations")
def stations():
     session = Session(engine)
     results = session.query(stats.name).all()
     session.close()
     names = list(np.ravel(results))

    return jsonify(names)

@app.route("/api/v1.0/tobs")
def tobs():
     mostactive=session.query(precip.station, func.count(precip.tobs)).\
    group_by(precip.station).\
    order_by(func.count(precip.tobs).desc()).()first
     latest = session.query(precip.date).order_by(precip.date.desc()).first()]
     lastyear = dt.date(2017, 8, 23) - dt.timedelta(days=365)
     session = Session(engine)
     results = session.query(precip.date, precip.tobs).\
     filter(precip.station == mostactive).\
     filter(precip.date >= lastyear).all()
     session.close()
     temps = list(np.ravel(results))

    return jsonify(temps)

@app.route("/api/v1.0/<start>") #4. Kailangan ko na each date between start and end ito, tama ba na solution ito?  
def start():
     print("Server received request for 'Variable Start' page...")
     mostactive=session.query(precip.station, func.count(precip.tobs)).\
    group_by(precip.station).\
    order_by(func.count(precip.tobs).desc()).()first
     startdate=input("Give a start date (yyyy-mm-dd:")
     results = session.query(precip.station, func.min(precip.tobs), func.max(precip.tobs), func.avg(precip.tobs)).\
    filter(precip.station == mostactive).all().\
    filter(precip.date >= startdate).all()
    session.close()
#     varstart = list(np.ravel(results)) #5. necessary ba yung longer code sa baba, o ito na lang?
    all_temp = []
    for date, tobs in results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["tobs"] = tobs
        all_temp.append(temp_dict)
     for x in all_temp:
        search_term = x["date"]
        if search_term == start:
            return jsonify(session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
                filter(measurement.date >= start).all())
    return jsonify({"error": "Date not found."}), 404

    return jsonify(varstart)

@app.route("/api/v1.0/<start>/<end>")
def end():
     print("Server received request for 'Variable Period' page...")
     mostactive=session.query(precip.station, func.count(precip.tobs)).\
    group_by(precip.station).\
    order_by(func.count(precip.tobs).desc()).()first
     startdate=input("Give a start date (yyyy-mm-dd):")
     enddate=input("Give an end date (yyyy-mm-dd):")
     results = session.query(precip.station, func.min(precip.tobs), func.max(precip.tobs), func.avg(precip.tobs)).\
    filter(precip.station == mostactive).all().\
    filter(precip.date >= startdate).filter(precip.date <= enddate).all()
    session.close()
#     varperiod = list(np.ravel(results)) 
    all_temp = []
    for date, tobs in results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["tobs"] = tobs
        all_temp.append(temp_dict)
     for x in all_temp:
        search_term = x["date"]
        if search_term == start:
            return jsonify(session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
                filter(measurement.date >= start).all())
    return jsonify({"error": "Date not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)


