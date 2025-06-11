# Time Zone App
A simple time zone app built with Python, UV, and Streamlit.

# Getting Started
### 1️⃣ Install UV
First, install UV (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
For Windows:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Verify installation:
```bash
uv --version
```

### 2️⃣ Create and Initialize the Project
```bash
uv init time-zone-app
cd time-zone-app
```

### 3️⃣ Install Sreamlit (Dependency)
```bash
uv add streamlit
```

### 4️⃣ Activate UV Virtual Environment (Windows)
```bash
.venv\Scripts\activate
```
For Linux/macOS:
```bash
source .venv/bin/activate
```

### 5️⃣ Run Time Zone App
```bash
streamlit run main.py
```
*🎉 That’s it! Your Time Zone App is ready to use 🚀*