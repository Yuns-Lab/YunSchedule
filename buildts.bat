@echo off
cls
color b
set "file=%1"
@echo Build Log:
@echo.

E:/Linguist_v6.6.1/lupdate.exe %file% -ts zh_CN.ts

:: delay exit
ping 127.0.0.1 -n 6 > nul
color
cls