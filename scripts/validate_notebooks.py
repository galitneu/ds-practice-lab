"""Validate and execute starters without invoking unfinished functions."""
from pathlib import Path
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
root = Path(__file__).resolve().parents[1]
for path in sorted((root / 'exercises').glob('*.ipynb')):
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    ExecutePreprocessor(timeout=120, kernel_name='python3').preprocess(notebook, {'metadata': {'path': str(root)}})
    print(f'OK {path.name}')
