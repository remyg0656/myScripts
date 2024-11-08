::script de compilation de mouseMve.py pour creer un executable

set CURRENT=%~dp0
echo %CURRENT%  

set BUILDDIR=%CURRENT%\build
set DISTDIR=%CURRENT%\dist
SET EXENAME=mouseMove

IF EXIST  %BUILDDIR% rmdir %BUILDDIR% /s /q >nul
::rmdir /S /Q %CURRENT%\build
IF EXIST  %DISTDIR% rmdir /S /Q %DISTDIR%

set MOVESPEC=%CURRENT%\%EXENAME%.spec
IF EXIST %MOVESPEC% del %MOVESPEC%
pyinstaller.exe  %CURRENT%."\..\\"%EXENAME%.py ^
                --noconsole ^
                --noconfirm ^
                --onefile ^
                --clean ^
                --distpath %DISTDIR% ^
                --workpath %BUILDDIR% ^
                --name %EXENAME%

%DISTDIR%\%EXENAME%.exe
