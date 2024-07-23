@echo off
setlocal

set script_dir=%~dp0
python "%script_dir%_loopfail.py" %*

endlocal