#!/bin/sh
FILE1=frontend/results/NVDA_SOXX_BTC_GBT.csv
FILE2=frontend/results/NVDA_SOXX_BTC_NN.csv
if !(test -f "$FILE1"); then
    ./frontend/model/makeResults.sh
    echo 'nfound1'
fi
if !(test -f "$FILE2"); then
    ./frontend/model/makeResults.sh
    echo 'nfound2'
fi

if [ "$1" != "-v" ] ; then 
    echo runing quietly, to see output, please use run.sh -v



    python -m pip install --upgrade pip > /dev/null 
    pip install -r requirements.txt > /dev/null 
    cd frontend
    python init_db.py > /dev/null 
    echo '######################################'
    echo '##       Server is running on       ##'
    echo '##       http://127.0.0.1:5000      ##'
    echo '##       To quit, press Ctrl+C      ##'
    echo '######################################'
    python -m flask run > /dev/null 2>&1

else
    python -m pip install --upgrade pip || (echo "python -m pip install --upgrade pip failed" && exit 1)
    pip install -r requirements.txt || (echo "pip install failed" && exit 1)
    cd frontend || (echo "cd frontend failed" && exit 1)
    python init_db.py || (echo "python init_db.py failed" && exit 1)
    python -m flask run || (echo "python -m flask run failed" && exit 1)
fi
