@echo off
color a
title ReleaseAdbProt
echo ========================
echo *** wulei 2018-04-12 ***
echo ***      v1.0.0      ***
echo ========================
echo ------------------------------
echo Checking adb port...
for /F "usebackq tokens=5" %%a in (`"netstat -ano | findstr "5037""`) do (
if not "%%a" =="0" call :ReleasePort %%a
)
echo ------------------------------
echo adb port has been released!
echo ------------------------------