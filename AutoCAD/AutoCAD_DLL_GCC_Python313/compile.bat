@echo off
set PYTHON_ROOT=C:\Users\TESO\AppData\Local\Programs\Python\Python313
set GCC_BIN=D:\work\mingw64\bin

%GCC_BIN%\gcc -shared -o acadwrapper.dll acad_wrapper.c -I%PYTHON_ROOT%\include -L%PYTHON_ROOT%\libs -lpython313 -fPIC
echo ? DLL 빌드 완료: acadwrapper.dll
pause