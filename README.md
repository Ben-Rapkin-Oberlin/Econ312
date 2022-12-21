# Econ312 Final Project  

This project is an attempt to make a stock prediction tool using mixed datasets. There is a frontend included with the project, please see below!  

Please Note that 1Password1 is Ben Rapkin

## **Website (currently out dated)**  
http://benrapkin.pythonanywhere.com/

## **Run Locally**  
If you would like to host the website locally, there are included bash and PowerShell scripts to run the project. These scripts will initialize the SQL database, ensure that the models have made their predictions, and start the server.

**Linux**  
```
$ ./run.sh  
```
**Windows**  
```
> ./run.ps1 
``` 


## **Notable Files and Directories**


### Machine Learning and Data   

**frontend**  
[Directory] Houses the front end and most functional elements of the project. 

**frontend/requirements.txt**  
[File] List of all the dependencies. This is installed via the shell scripts above

**frontend/model**  
[Directory] Holds the algorithms and their corresponding csv files.

**model/GBT.py**  
[File] Holds the script for the Gradient Boosted Tree. This was implemented via Lightgbm

**model/neuralNet.py**  
[File] Holds the script for the Neural Network. This was implemented via sklearn

**model/getData.py**  
[File] Reads in the data file (model/NVDA_SOXX_BTC.csv) and preprocesses it
 
**frontend/results**   
[Directory] Contains the predicted vs actual data from the Machine Learning Models


### Website   

**frontend/app.py**    
[File] This file routes http addresses and converts pandas dataframes into json files

**frontend/init_db.py**
[File] this file initialized the database for the financial and twitter data. 

**frontend/static**
[Directory] image file and CSS 

**frontend/templates**
[Directory] This folder holds the html files that form the basis of each page. They make use of the Jinja2 engine to allow for python-like loops.


### Other 
**old_files**  
[Directory] Holds depreciated files that were used to build this project, but are no longer necessary. These are included in case of specific questions about data, preprocess, or other small facets of the project. 
