# Bootstrap cell to ensure src/ is importable in Jupyter
import sys
from pathlib import Path

# Go up to project root if running from notebooks/
project_root = Path.cwd()
if project_root.name == "notebooks":
    project_root = project_root.parent

sys.path.insert(0, str(project_root))

print(f"Project root added to sys.path: {project_root}")
