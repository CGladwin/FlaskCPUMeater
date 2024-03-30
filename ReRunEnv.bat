@REM This batch file allows for quick restarting of venv
@RD /S /Q env
python -m venv env
call env\Scripts\activate.bat
env\Scripts\pip.exe install -r requirements.txt