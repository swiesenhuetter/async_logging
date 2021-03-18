set pythonpath=c:\Python38\Python38\python.exe
%pythonpath% -m venv venv

call venv\Scripts\activate

python -m pip install --upgrade pip

@echo off
for /f "tokens=*" %%p in (requirements.txt) do (
  pip install %%p
)
pause