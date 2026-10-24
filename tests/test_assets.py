"""Repository integrity checks independent of learner implementations."""
from pathlib import Path
import hashlib
import json
import nbformat

ROOT = Path(__file__).resolve().parents[1]

def test_local_data_integrity():
    manifest = json.loads((ROOT / 'data/manifest.json').read_text())
    for name, metadata in manifest.items():
        path = ROOT / 'data' / name
        assert path.stat().st_size == metadata['bytes'] < 5_000_000
        assert hashlib.sha256(path.read_bytes()).hexdigest() == metadata['sha256']

def test_starter_notebook_format():
    paths = sorted((ROOT / 'exercises').glob('*.ipynb'))
    assert len(paths) >= 12
    for path in paths:
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        assert any('TODO' in cell.source for cell in notebook.cells)
        assert any('<details>' in cell.source for cell in notebook.cells)
