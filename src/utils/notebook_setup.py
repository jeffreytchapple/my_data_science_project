from pathlib import Path
import sys
from dotenv import load_dotenv

def ensure_project_on_path():
    """Add project root to sys.path (useful if not using editable install)."""
    project_root = Path(__file__).resolve().parents[2]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    return project_root

def load_env():
    """Load .env from project root."""
    project_root = Path(__file__).resolve().parents[2]
    env_path = project_root / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
