Write-Host "Start Runner" -ForegroundColor Green

Write-Host "Activating Django5 virtual environment" -ForegroundColor Yellow
workin django5
Write-Host "Opening browser" -ForegroundColor Yellow
Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "http://localhost:8000/"
Write-Host "Starting local Django server" -ForegroundColor Green
python manage.py runserver


# mkvirtualenv --python=python3.9 tinka