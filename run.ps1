if ( "$args" -eq "-v" )
{
    #verbose mode
    Set-Variable -Name "FILE1" -Value "frontend\results\NVDA_SOXX_BTC_GBT.csv"
    Set-Variable -Name "FILE2" -Value "frontend\results\NVDA_SOXX_BTC_NN.csv"
    
    if ( ! (test-Path -Path "$FILE1" -PathType Leaf ))
    {
        echo 'building GBT model'
        Set-Location frontend\model
        python GBT.py 
        Set-Location '..\..'
    }

    if ( ! (test-Path -Path "$FILE2" -PathType Leaf ))
    {
        echo 'building NN model'
        Set-Location frontend\model
        python neuralNet.py
        Set-Location '..\..'
    }

    python -m pip install --upgrade pip
    pip install -r frontend\requirements.txt
    Set-Location frontend
    python init_db.py
    Write-Output '######################################'
    Write-Output '##       Server is running on       ##'
    Write-Output '##       http://127.0.0.1:5000      ##'
    Write-Output '##       To quit, press Ctrl+C      ##'
    Write-Output '######################################'
    python -m flask run
    Write-Output 'Server is stopped'
    Set-Location ..

}

else
{

    Write-Output "runing quietly, to see output, please use run.sh -v"
    Set-Variable -Name "FILE1" -Value "frontend\results\NVDA_SOXX_BTC_GBT.csv"
    Set-Variable -Name "FILE2" -Value "frontend\results\NVDA_SOXX_BTC_NN.csv"
    
    if ( ! (test-Path -Path "$FILE1" -PathType Leaf ))
    {
        Set-Location frontend\model
        python GBT.py > $null
        Set-Location '..\..'
    }

    if ( ! (test-Path -Path "$FILE2" -PathType Leaf ))
    {
        Set-Location frontend\model
        python neuralNet.py > $null
        Set-Location '..\..'
    }


    python -m pip install --upgrade pip > $null 
    pip install -r  frontend\requirements.txt > $null 
    Set-Location frontend
    python init_db.py > $null 
    Write-Output '######################################'
    Write-Output '##       Server is running on       ##'
    Write-Output '##       http://127.0.0.1:5000      ##'
    Write-Output '##       To quit, press Ctrl+C      ##'
    Write-Output '######################################'
    python -m flask run  2>&1 > $null 
    }
   

