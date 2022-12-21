#!/bin/sh


if [ "$1" != "-v" ] ; then 
    echo runing quietly, to see output, please use run.sh -v
    FILE1=frontend/results/NVDA_SOXX_BTC_GBT.csv
    FILE2=frontend/results/NVDA_SOXX_BTC_NN.csv
    if !(test -f "$FILE1"); then
        #echo 'building GBT model'
        cd frontend/model
        python GBT.py 2>&1> /dev/null
        cd '../..'
    fi

    if !(test -f "$FILE2"); then
        #echo 'building NN model'
        cd frontend/model
        python neuralNet.py 2>&1> /dev/null
        cd '../..'
    fi
    python -m pip install --upgrade pip > /dev/null 
    pip install -r frontend/requirements.txt > /dev/null 
    cd frontend
    python init_db.py > /dev/null 
    echo '######################################'
    echo '##       Server is running on       ##'
    echo '##       http://127.0.0.1:5000      ##'
    echo '##       To quit, press Ctrl+C      ##'
    echo '######################################'
    python -m flask run > /dev/null 2>&1
    cd '..'

else
    FILE1=frontend/results/NVDA_SOXX_BTC_GBT.csv
    FILE2=frontend/results/NVDA_SOXX_BTC_NN.csv
    if !(test -f "$FILE1"); then
        echo 'building GBT model'
        cd frontend/model
        python GBT.py 2>&1> /dev/null
        cd '../..'
    fi

    if !(test -f "$FILE2"); then
        echo 'building NN model'
        cd frontend/model
        python neuralNet.py 2>&1> /dev/null
        cd '../..'
    fi
    python -m pip install --upgrade pip || (echo "python -m pip install --upgrade pip failed" && exit 1)
    pip install -r frontend/requirements.txt || (echo "pip install failed" && exit 1)
    cd frontend || (echo "cd frontend failed" && exit 1)
    python init_db.py || (echo "python init_db.py failed" && exit 1)
    python -m flask run || (echo "python -m flask run failed" && exit 1)
    cd '..'
fi
