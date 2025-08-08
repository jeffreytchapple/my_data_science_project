# Bootstrap cell for notebooks (use if not using editable install)
from pathlib import Path
import sys

PROJECT_ROOT = Path.cwd().parent if (Path.cwd().name == "notebooks") else Path.cwd()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Optional: load .env
from dotenv import load_dotenv
load_dotenv(PROJECT_ROOT / ".env")
