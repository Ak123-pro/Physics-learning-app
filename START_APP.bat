@echo off
title Let's Learn Physics with National
color 0B

echo.
echo  ============================================
echo   Let's Learn Physics with National
echo   Starting your Physics App...
echo  ============================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo  ERROR: Python is not installed!
    echo.
    echo  Please install Python from: https://python.org/downloads
    echo  Make sure to check "Add Python to PATH" during install!
    echo.
    pause
    exit
)

echo  [1/3] Python found!

:: Check if streamlit is installed, install if not
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo  [2/3] Installing required packages... (first time only, please wait)
    pip install streamlit --quiet
    echo  Packages installed!
) else (
    echo  [2/3] All packages ready!
)

echo  [3/3] Launching Physics App...
echo.
echo  ==============================================
echo   App is opening in your browser!
echo   If browser doesn't open, go to:
echo   http://localhost:8501
echo  ==============================================
echo.
echo  Press CTRL+C to stop the app
echo.

:: Launch the app
streamlit run app.py --server.port 8501 --browser.gatherUsageStats false

pause
