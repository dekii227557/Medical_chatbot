import os 
from pathlib import Path
import logging 

# Logging de ghi ra thong tin loi
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Danh sach cac file can duoc tao
list_of_files = [
    "src/_init_.py",
    "src/helper.py",
    "src/prompts.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "template.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass   
            logging.info(f"Created empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")