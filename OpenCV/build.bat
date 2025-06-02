@echo off
chcp 65001 >nul
echo [🔧 Nuitka Build Start...]

set SCRIPT=test_tesseract_OCR.py
set OUTDIR=build_output

nuitka ^
  %SCRIPT% ^
  --standalone ^
  --remove-output ^
  --enable-plugin=tk-inter ^
  --include-package=pytesseract ^
  --show-progress ^
  --output-dir=%OUTDIR% ^
  --nofollow-import-to=PyQt6 ^
  --windows-disable-console

echo [✅ Build Completed. Output is in .\%OUTDIR%]
pause
