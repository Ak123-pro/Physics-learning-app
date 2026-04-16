#!/bin/bash

echo ""
echo "============================================"
echo " Let's Learn Physics with National"
echo " Starting your Physics App..."
echo "============================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed!"
    echo "Install it from: https://python.org/downloads"
    exit 1
fi

echo "[1/3] Python found!"

# Install streamlit if needed
python3 -c "import streamlit" &> /dev/null
if [ $? -ne 0 ]; then
    echo "[2/3] Installing packages (first time only)..."
    pip3 install streamlit --quiet
    echo "      Done!"
else
    echo "[2/3] All packages ready!"
fi

echo "[3/3] Launching Physics App..."
echo ""
echo "App is opening at: http://localhost:8501"
echo "Press CTRL+C to stop"
echo ""

# Run the app
streamlit run app.py --server.port 8501 --browser.gatherUsageStats false
