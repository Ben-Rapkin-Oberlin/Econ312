#!/bin/sh


if [ "$1" != "-v" ] ; then 
    echo runing quietly, to see output, please use run.sh -v
    python -m pip install --upgrade pip > /dev/null 
    pip install -r frontend/requirements.txt > /dev/null 
    FILE1=frontend/results/NVDA_SOXX_BTC_GBT.csv
    FILE2=frontend/results/NVDA_SOXX_BTC_NN.csv
    File3=frontend/results/combined_GBT.csv
    File4=frontend/results/combined_NN.csv
    if !(test -f "$FILE1"); then
        #echo 'building GBT model'
        cd frontend/model
        python GBT.py NVDA_SOXX_BTC.csv 2>&1> /dev/null
        cd '../..'
    fi

    if !(test -f "$FILE2"); then
        #echo 'building NN model'
        cd frontend/model
        python neuralNet.py NVDA_SOXX_BTC.csv 2>&1> /dev/null
        cd '../..'
    fi
    if !(test -f "$FILE3"); then
        #echo 'building GBT model'
        cd frontend/model
        python GBT.py combined.csv 2>&1> /dev/null
        cd '../..'
    fi

    if !(test -f "$FILE4"); then
        #echo 'building NN model'
        cd frontend/model
        python neuralNet.py combined.csv 2>&1> /dev/null
        cd '../..'
    fi

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
    python -m pip install --upgrade pip || (echo "python -m pip install --upgrade pip failed" && exit 1)
    pip install -r frontend/requirements.txt || (echo "pip install failed" && exit 1)
    FILE1=frontend/results/NVDA_SOXX_BTC_GBT.csv
    FILE2=frontend/results/NVDA_SOXX_BTC_NN.csv
    FILE3=frontend/results/combined_GBT.csv
    FILE4=frontend/results/combined_NN.csv
    if !(test -f "$FILE1"); then
        echo 'building GBT model 1'
        cd frontend/model
        python GBT.py NVDA_SOXX_BTC.csv
        cd '../..'
    fi
    if !(test -f "$FILE2"); then
        echo 'building NN model1 1'
        cd frontend/model
        python neuralNet.py NVDA_SOXX_BTC.csv
        cd '../..'
    fi
     if !(test -f "$FILE3"); then
        echo 'building GBT model 2'
        cd frontend/model
        python GBT.py combined.csv
        cd '../..'
    fi

    if !(test -f "$FILE4"); then
        echo 'building NN model 2'
        echo $FILE4
        cd frontend/model
        python neuralNet.py combined.csv
        cd '../..'
    fi

    cd frontend || (echo "cd frontend failed" && exit 1)
    python init_db.py || (echo "python init_db.py failed" && exit 1)
    python -m flask run || (echo "python -m flask run failed" && exit 1)
    cd '..'
fi
