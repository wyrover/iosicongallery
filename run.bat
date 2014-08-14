@echo off
if [%1] == [] goto runbat_args

:runbat
color 0A
@set path=C:\Python27;C:\Python27\Scripts;C:\OpenSSL-Win32\bin;D:\MinGW\bin;D:\tools\editplus\tools\depot_tools;%PATH%
python -c "import sys;print sys.path"
cd /d "%~dp0"
echo "开始执行scrapy..."
scrapy crawl iosicon
echo "scrapy运行完毕."

goto exit

:runbat_args
start run.bat 111


:exit