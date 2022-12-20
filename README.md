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

**model/trainingSets** holds the csv files that the ML algorithms are trained on

**model/results** holds the information for graphing the line plots

**models/GBT.py** holds the GBT script

**models/neuralNet.py** holds the NN script

**old_files** holds files that were used to build this project, but not necessary to run it. They are saved for posterity's sake  








