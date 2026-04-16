# ⚛️ Let's Learn Physics with National
## Complete Setup Guide

---

## 🚀 QUICKSTART (Read this first!)

### Step 1 — Install Python (one time only)
1. Go to **https://python.org/downloads**
2. Click the big yellow **"Download Python 3.x"** button
3. Run the installer
4. ✅ **IMPORTANT:** Check the box that says **"Add Python to PATH"**
5. Click Install Now

### Step 2 — Start the App
- **Windows:** Double-click **`START_APP.bat`**
- **Mac/Linux:** Open Terminal in this folder, type `bash start_app.sh`

### Step 3 — Open in Browser
- The app opens automatically at **http://localhost:8501**
- Works on any browser (Chrome, Edge, Firefox)

### Step 4 — Open on Phone (same WiFi)
- Find your computer's IP address (see below)
- Open **http://YOUR-IP:8501** on your phone

---

## 📱 How to Find Your IP (for phone access)

**Windows:**
1. Press `Win + R`, type `cmd`, press Enter
2. Type `ipconfig`
3. Look for "IPv4 Address" — e.g. `192.168.1.5`
4. On phone: go to `http://192.168.1.5:8501`

**Mac:**
1. Open Terminal
2. Type `ifconfig | grep "inet "`
3. Use the number that starts with `192.168.x.x`

---

## 🛠️ If Something Goes Wrong

### "Python is not installed"
→ Download from python.org, make sure to check "Add Python to PATH"

### "Port already in use"
→ Close other apps, or change port in START_APP.bat from 8501 to 8502

### App is slow
→ Close other browser tabs, use Chrome for best performance

### VS Code Users
1. Open the PhysicsApp folder in VS Code
2. Open the Terminal in VS Code (Ctrl + `)
3. Type: `pip install streamlit`
4. Then type: `streamlit run app.py`

---

## 📁 What's in This Folder

```
PhysicsApp/
├── app.py              ← The entire physics app (main file)
├── START_APP.bat       ← Windows: double-click to launch
├── start_app.sh        ← Mac/Linux: run in terminal
├── requirements.txt    ← Python packages needed
├── .streamlit/
│   └── config.toml    ← App settings (dark theme etc.)
└── HOW_TO_RUN.md      ← This file
```

---

## 🎮 What the App Contains

**Grades 8–12 Physics**

| Grade | Topics |
|-------|--------|
| 8 | Motion & Kinematics, Force & Pressure, Sound & Waves |
| 9 | Newton's Laws & Momentum, Gravitation & Orbits |
| 10 | Electricity & Circuits, Light & Optics |
| 11 | Thermodynamics |
| 12 | Quantum Physics, Nuclear Physics |

**7 Live Physics Simulations:**
- 🚀 Projectile Launcher (fire rockets, hit targets!)
- 💥 Elastic Collision Lab (momentum transfer)
- 🌌 Gravity Well (launch satellites into orbit)
- 〰️ Sound Wave Lab (see sound waves live)
- 🔌 Circuit Builder (Ohm's Law simulator)
- 🔍 Ray Tracer (lenses and mirrors)
- 💨 Gas Law Lab (molecules bouncing)

---

## 💡 Tips for Teachers

- Connect to same WiFi as students → share your IP → students open on phones
- Best on Chrome browser
- Can run offline (no internet needed after first install)
- Each topic: Story → Games → Notes → Quiz → Stars & XP

---

Built for National Tuition Centre | Grade 8–12 Physics
