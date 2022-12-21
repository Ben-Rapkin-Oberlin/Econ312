if ( "$args" -eq "-v" )
{
    #verbose mode
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    Set-Location frontend
    python init_db.py
    Write-Output '######################################'
    Write-Output '##       Server is running on       ##'
    Write-Output '##       http://127.0.0.1:5000      ##'
    Write-Output '##       To quit, press Ctrl+C      ##'
    Write-Output '######################################'
    python -m flask run
    Write-Output 'Server is stopped'
    Set-Location '..'

}
else
{

    Write-Output "runing quietly, to see output, please use run.ps1 -v"
    python -m pip install --upgrade pip > $null 
    pip install -r requirements.txt > $null 
    Set-Location frontend
    python init_db.py > $null 
    Write-Output '######################################'
    Write-Output '##       Server is running on       ##'
    Write-Output '##       http://127.0.0.1:5000      ##'
    Write-Output '##       To quit, press Ctrl+C      ##'
    Write-Output '######################################'
    python -m flask run
    }
   

