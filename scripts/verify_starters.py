"""Require every untouched exercise to fail specifically at its TODO."""
import os
from pathlib import Path
import subprocess
import sys
root = Path(__file__).resolve().parents[1]
env = dict(os.environ, USE_SOLUTIONS='0')
tests = sorted((root / 'tests').glob('test_ex*.py'))
for test in tests:
    result = subprocess.run([sys.executable, '-m', 'pytest', '-q', str(test)], cwd=root, env=env, capture_output=True, text=True)
    if result.returncode != 1 or 'NotImplementedError' not in result.stdout:
        print(result.stdout, result.stderr)
        raise SystemExit(f'Unexpected starter result: {test.name}')
print(f'All {len(tests)} starters fail at their intended TODO.')
