rd /q /s dist
pyinstaller --icon=app.ico --workpath=for_building --noconsole --onefile --version-file=version.rc
mkdir dist\data
xcopy.exe /y data dist\data