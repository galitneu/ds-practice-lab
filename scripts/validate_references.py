"""Execute reference notebooks only after an explicit solution-validation request."""
import os
from pathlib import Path
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

if os.getenv('USE_SOLUTIONS') != '1':
    raise SystemExit('Explicit reference mode required: USE_SOLUTIONS=1 python scripts/validate_references.py')
root = Path(__file__).resolve().parents[1]
for path in sorted((root / 'solutions').glob('*_reference.ipynb')):
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    ExecutePreprocessor(timeout=180, kernel_name='python3').preprocess(notebook, {'metadata': {'path': str(root)}})
    nbformat.write(notebook, path)
    print(f'OK {path.name}', flush=True)
