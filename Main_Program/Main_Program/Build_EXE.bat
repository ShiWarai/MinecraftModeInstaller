rd /q /s dist
pyinstaller main.pyw --icon=app.ico --workpath=for_building --noconsole --onefile
mkdir dist\data
xcopy.exe /y data dist\data