
By: Tamera Brown, Talent Path: D2

## Overview

This project predicts the fare amount (inclusive of tolls) for a taxi ride in New York City given the pickup and dropoff locations. 




## Technology Stack

* [Jupyter Notebook](https://jupyter.org/) 

* [Python](https://www.python.org/)

* [Scikit-learn](https://scikit-learn.org/stable/)

* [Postgres](https://www.postgresql.org/)

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)

  

## Data

This dataset include data from NYC Taxi Rides found on [Kaggle](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction/overview) which contains 55M rows spanning over 7 years (2009-2015). I worked with the subset of that data with the year 2014, which has 8M rows.



## Machine Learning Pipeline

![Pipeline](Pipeline.png)



### Fare Outlier Removal

![fare amount before](fare amount before.png)  ![fare amount after](fare amount after.png)

#### Distance

    `from haversine import haversine
    
    def get_distance(df):
        a1 = df['pickup_latitude']
        a2 = df['dropoff_latitude']
    
    	b1 = df['pickup_longitude']
    	b2 = df['dropoff_longitude']
    
    	pick_up = (a1, b1) 
    	drop_off = (a2, b2)
    	return round(haversine(pick_up, drop_off,unit='mi'),2)`

### Distance Outlier Removal

![distance before](distance before.png)  ![distance after](distance after.png)







	`nycfare_2014_df['pickup_datetime'] = nycfare_2014_df['pickup_datetime'].str.replace(" UTC", "")
	nycfare_2014_df.pickup_datetime=pd.to_datetime(nycfare_2014_df.pickup_datetime,format='%Y-%m-%d %H:%M:%S')
	nycfare_2014_df['key'] = nycfare_2014_df['key'].str.replace(" UTC", "")
	nycfare_2014_df.key=pd.to_datetime(nycfare_2014_df.key,format='%Y-%m-%d %H:%M:%S')
	nycfare_2014_df['pickup_datetime']=nycfare_2014_df['pickup_datetime'].dt.tz_localize('UTC')
	nycfare_2014_df['pickup_datetime'] = nycfare_2014_df['pickup_datetime'].dt.tz_convert('US/Eastern')`
  
  
  
 ![Correlation Heatmap](Correlation Heatmap.png)
