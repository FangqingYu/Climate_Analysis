# Climate_Analysis
-Climate analysis and exploration on Honolulu, Hawaii using Python, SQLAlchemy and SQLAlchemy ORM. Data published online in JSON format via Flask, a web framework and server provider written in Python.

# Part 1 - Climate App

Data were published via FLASK (file app.py) based on SQLAlchemy queries. Users are allow to enter their desired start and end data in the to obtain climate data.

## Routes
* /api/v1.0/precipitation
  * Convert the query results to a Dictionary using date as the key and prcp as the value.
  
* /api/v1.0/stations
  * Return a JSON list of stations from the dataset.
  
* /api/v1.0/tobs
  * query for the dates and temperature observations from a year from the last data point.
  *  Return a JSON list of Temperature Observations (tobs) for the previous year.
  
* /api/v1.0/<start> and /api/v1.0/<start>/<end>
  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range
  * When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
  * When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
  

# Part 2 - Climate Analysis and Exploration

* climate_analysis.ipynb

* Climated data of Honolulu, Hawaii over the course of an arbitary date range were retrieved from database using SQLAlchemy queries on criteria selected

* Data were then loaded into Pandas and graphed by Matplotlib selected date range in Honolulu, Hawaii

## Precipitation Analysis

Precipitation data from the past 12 months were queried and displayed as a line chart to display variation

## Station Analysis

Statistics of different observationa stations were calculated and compared to find the average precipitation by station and most active station.


## Temperature Analysis

* The temperature data over the defined date range is graphed as a boxplot to show distribution
* Daily normals (min, max, and average) for every day of the data range is graphed as an area plot 







