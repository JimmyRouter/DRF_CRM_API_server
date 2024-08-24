@echo off
cd C:\FILES_C\progs\DRF_CRM_API_server\venv\Scripts\
call activate.bat
cd C:\FILES_C\progs\DRF_CRM_API_server\octocrm\
python manage.py runserver
