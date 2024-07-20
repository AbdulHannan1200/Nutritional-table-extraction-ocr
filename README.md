# FastAPI Modular Boilerplate

FastAPI is a modern, high-performance Python web framework that allows developers to build robust APIs for web services and RESTful APIs in Python quickly and efficiently.

#Structure Details

1. /app: this is the main folder for manage entire app's code

   a. app.py: this file contains all API functions and endpoints

   b. /Modules: this is the main directory of codes of all modules of app

   i) Module A: first module

   ii) Module B: second module

   c. /Storage: this is the directory to manage storage bucket related codes

   d. /Database: this is the directory to manage database connection & CRUDs functions

2. main.py: this is the main file to run the server via

```bash
python main.py
```

3. requirements.text: this holds app's dependencies and is installed via

```bash
pip install -r requirements.txt
```

4. .gitignore: this file holds names & extensions to avoid unnecessary or heavy files to be pushed on repo
