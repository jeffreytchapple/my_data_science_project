

## 📦 Editable Install for Development
To make `src/` imports work everywhere (including Jupyter notebooks):

```bash
pip install -e .
```

Then in notebooks or scripts, you can just:

```python
from src.data_loader import load_data
```
