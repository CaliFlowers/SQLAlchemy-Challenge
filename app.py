
from flask import Flask, jsonify, request
import datetime as dt 
from sqlalchemy.ext.automap import automap_base 
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,  func, inspect
import numpy as np

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
    prcp = session.query(precip.date, precip.prcp).all()
    session.close()

    Date = {}
    Precipitation = {}
    results = []
    for x in prcp:
        results.append({
            "Date" : x[0], 
            "Precipitation" : x[1]
            })

    return jsonify(results)

@app.route("/api/v1.0/stations")
def stations():
     session = Session(engine)
     results = session.query(stats.name).all()
     session.close()
     names = list(np.ravel(results))
     session = Session(engine)
     results = session.query(stats.name).all()
     session.close()
     names = list(np.ravel(results))

     return jsonify(names)

@app.route("/api/v1.0/tobs")
def tobs():
     session = Session(engine)
     mostactive=session.query(precip.station, func.count(precip.tobs)).\
    group_by(precip.station).\
    order_by(func.count(precip.tobs).desc()).first()
     latest = session.query(precip.date).order_by(precip.date.desc()).first()
     lastyear = dt.date(2017, 8, 23) - dt.timedelta(days=365)
     results = session.query(precip.date, precip.tobs).\
     filter(precip.station == 'USC00519281').\
     filter(precip.date >= lastyear).all()
     session.close()
     temps = list(np.ravel(results))

     return jsonify(temps)

@app.route("/api/v1.0/<start>") 
def start():
     print("Server received request for 'Variable Start' page...")
     mostactive=session.query(precip.station, func.count(precip.tobs)).\
    group_by(precip.station).\
    order_by(func.count(precip.tobs).desc()).first
     results = session.query(precip.station, func.min(precip.tobs), func.max(precip.tobs), func.avg(precip.tobs)).\
    filter(precip.station == mostactive).all().\
    filter(precip.date >= startdate).all()
     latest = session.query(precip.date).\
    order_by(precip.date.desc()).first
     lastyear = dt.date(2017, 8, 23) - dt.timedelta(days=365)
     session = Session(engine)
     results = session.query(precip.date, precip.tobs).filter(precip.station == 'USC00519281').filter(precip.date >= lastyear).all()
     session.close()
     temps = list(np.ravel(results)) 

     return jsonify(temps)

@app.route("/api/v1.0/data")  
def start_date(date):

    """Start Date.
    Args:
        date (str): A date string in the format '%m-%d'
        
    Returns:
        A list of tuples containing the daily normals, tmin, tavg, and tmax
    
    """
   

    sel = [func.min(precip.tobs), func.avg(precip.tobs), func.max(precip.tobs)].all()

    results = session.query(*sel).filter(func.strftime("%m-%d", precip.date) >= date).all()

    print(start_date(date))
    session.close()
#    
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
    order_by(func.count(precip.tobs).desc()).first
     startdate=input("Give a start date (yyyy-mm-dd):")
     enddate=input("Give an end date (yyyy-mm-dd):")
     results = session.query(precip.station, func.min(precip.tobs), func.max(precip.tobs), func.avg(precip.tobs)).\
    filter(precip.station == mostactive).all().\
    filter(precip.date >= startdate).filter(precip.date <= enddate).all()
@app.route("/api/v1.0/start_end")
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    start_date = request.args.get("start_date", None)
    end_date = request.args.get("end_date", None)
   
    return session.query(func.min(precip.tobs), func.avg(precip.tobs), func.max(precip.tobs)).\
        filter(precip.date >= start_date).filter(precip.date <= end_date).all()
    print(calc_temps(start_date, end_date))  
    session.close()

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