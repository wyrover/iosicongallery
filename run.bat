@echo off
if [%1] == [] goto runbat_args

:runbat
color 0A
@set path=C:\Python27;C:\Python27\Scripts;C:\OpenSSL-Win32\bin;D:\MinGW\bin;D:\tools\editplus\tools\depot_tools;%PATH%
python -c "import sys;print sys.path"
cd /d "%~dp0"
echo "��ʼִ��scrapy..."
scrapy crawl iosicon
echo "scrapy�������."

goto exit

:runbat_args
start run.bat 111


:exit