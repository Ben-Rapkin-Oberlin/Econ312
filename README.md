# Econ312 Final Project

This project is an attempt to make a stock prediction tool using mixed datasets.
There is a front end included with the project, please see below!

**To Run**
(optionally make a virtual environment)
$ pip install -r requirements.txt
$ cd frontend
$ python init_db.py
$ python -m flash run
go to http://127.0.0.1:5000 on the browser of your choice

**requirements.txt** All of the dependencies

**frontend** houses the front end and most functional elements of the project. 

**AllData/Datasets** contains all initially scraped and downloaded data This includes finical metrics in the economics folder
and tweets in in both tweet_scrape and twitter scraping

**AllData/mergedData** holds intermediate csv files and scripts used
to process the raw data


**AllData/trainingSets** holds the csv files that the ML algorithms are trained on

**AllData/results** holds the information for graphing the lineplots

**models/main.py** holds the GBT script

**models/nn2.py** holds the NN script

All other models/ files are related to earlier attempts at implementing the algorithms and/or code related to hyperparameter
optimization, which has not been implemented for this demo. This is related to the .neptune repository

All other folders are related to flask. Please let me know if you are interested in an explanation! 








