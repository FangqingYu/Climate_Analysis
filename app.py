import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
#################################################
#Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>")


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list precipitation of the past year by date"""

    # query for the last day
    last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    len_months = 12
    # convert result to datetime format
    last_day = datetime.datetime.strptime(last_day, "%Y-%m-%d")
    # calculate start day
    start_day =  last_day + relativedelta(months=-len_months)
    start_day = "{:%Y-%m-%d}".format(start_day)

    # Design a query to retrieve the last 12 months of precipitation data and plot the results
    results = session.query(Measurement.date, Measurement.prcp).\
                        filter(Measurement.date >= start_day ).\
                        order_by(Measurement.date).all()
    
    prcp_by_date = []
    for record in results:
        prcp_dict = {}
        prcp_dict["date"] = record.date
        prcp_dict["precipitation"] = record.prcp
        prcp_by_date.append(prcp_dict)
    
    return jsonify(prcp_by_date)


@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations"""

    results =  session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    stations = []
    for result in results:
        station_dict = {}
        station_dict["station"] = result.station
        station_dict["name"] = result.name
        station_dict["latitude"] =  result.latitude
        station_dict["longitude"] =  result.longitude
        station_dict["elevation"] = result.elevation
        stations.append(station_dict)
    
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of temperature observations (tobs) for the previous year"""
     # query for the last day
    last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    len_months = 12
    # convert result to datetime format
    last_day = datetime.datetime.strptime(last_day, "%Y-%m-%d")
    # calculate start day
    start_day =  last_day + relativedelta(months=-len_months)
    start_day = "{:%Y-%m-%d}".format(start_day)

    # Design a query to retrieve the last 12 months of temperature data and plot the results
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= start_day ).\
        order_by(Measurement.date).all()
    
    temps = []
    for result in results:
        temp_dict = {}
        temp_dict["station"] = result.station
        temp_dict["name"] = result.name
        temp_dict["latitude"] =  result.latitude
        temp_dict["longitude"] =  result.longitude
        temp_dict["elevation"] = result.elevation
        temps(station_dict).append(temp_dict)
    
    return jsonify(temps)


@app.route("/api/v1.0/<start>")
def temp_stats(start):
    """Return tmin, tavg, tmax for all dates greater than start date supplied by the user, or a 404 if not."""

    dates_ =  session.query(Measurement.date)
    dates = [x[0] for x in dates_]
    if start not in dates:
        return jsonify({"error": f"Date {start} not found."}), 404

    else:
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).all()

        temp_stats = [
            {"tmin": results[0][0]},
            {"tavg": results[0][1]},
            {"tavg": results[0][2]}
            ]
        return jsonify(temp_stats)


@app.route("/api/v1.0/<start>/<end>")
def temp_range_stats(start, end):
    """Returen tmin, tavg, tmax for all dates between start date and end date supplied by the user, or a 404 if not."""

    dates_ =  session.query(Measurement.date)
    dates = [x[0] for x in dates_]
    if start not in dates:
        return jsonify({"error": f"Date {start} not found."}), 404
    
    else:
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).filter(Measurement.date <= end).all()

        temp_stats = [
            {"tmin": results[0][0]},
            {"tavg": results[0][1]},
            {"tavg": results[0][2]}
        ]
        return jsonify(temp_stats)


    
