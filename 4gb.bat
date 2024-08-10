@echo off
echo Checking requirements...
timeout /t 3 /nobreak >nul 2>&1

echo Requirements met!
timeout /t 2.5 /nobreak >nul 2>&1

echo Gathering RAM information in a list...
timeout /t 3 /nobreak >nul 2>&1

wmic pagefile list /format:list
echo Gathered success!
timeout /t 2.5 /nobreak >nul 2>&1

echo Exchanging local drive C:/ left space for RAM...
timeout /t 2.5 /nobreak >nul
wmic computersystem where name="%computername%" set AutomaticManagedPagefile=False
echo Success!
timeout /t 2.5 /nobreak >nul 2>&1

echo Changing the RAM data...
wmic pagefileset where name="C:\\pagefile.sys" set InitialSize=6144,MaximumSize=12288
timeout /t 2.5 /nobreak >nul 2>&1

echo Success!
timeout /t 2.5 /nobreak >nul 2>&1

echo -------------- RESTART IS NEEDED IN ORDER TO WORK ----------------
echo Get More RAM by Lam
echo made on 16/7/2024 in VN.
echo Installation complete
timeout /t 2.5 /nobreak >nul 2>&1

echo Closing window...