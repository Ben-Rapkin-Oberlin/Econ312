# Econ312 Final Project  

This project is an attempt to make a stock prediction tool using mixed datasets.
There is a front end included with the project, please see below!  

## **Website (currently out dated)**  
http://benrapkin.pythonanywhere.com/

## **Run Locally**  
If you would like to host the website locally, there are included bash and powershell scripts to start the project.  

**Linux**  
        ./run.sh  

**Windows**  
        ./run.ps1  

These scripts will start the server locally. Additionally, they will ensure that the models have been run.

## **Notable Directories and Files**

**requirements.txt**  
[File] List of all the dependencies. This is installed via the shell scripts above

**frontend**  
[Directory] Houses the front end and most functional elements of the project. 

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
 
**old_files**  
[Directory] Holds depreciated files that were used to build this project, but are no longer necessary. These are included in case of specific questions about data, preprocess, or other small facets of the project. 








