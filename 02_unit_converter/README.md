# Unit Converter
A simple unit converter built with Python, UV, and Streamlit.

# Getting Started
### 1️⃣ Install UV
First, install UV (if not already installed):
```python
curl -LsSf https://astral.sh/uv/install.sh | sh
```
For Windows:
```python
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Verify installation:
```python
uv --version
```

### 2️⃣ Create and Initialize the Project
```python
uv init unit-converter
cd unit-converter
```

### 3️⃣ Install Sreamlit (Dependency)
```python
uv add streamlit
```

### 4️⃣ Activate UV Virtual Environment (Windows)
```python
.venv\Scripts\activate
```
For Linux/macOS:
```python
source .venv/bin/activate
```

### 5️⃣ Run Unit Converter
```python
streamlit run unit_converter.py
```
*_🎉 That’s it! Your Unit Converter is ready to use 🚀*_