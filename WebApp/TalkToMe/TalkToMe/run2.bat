start /b python  "D:\Projekty\TalkToMe\trunk\WebApp\TalkToMe\TalkToMe\manage.py" runserver --noreload --settings python.settings 8987
@ping localhost -n 5 >nul
@START "" "http://127.0.0.1:8987/"