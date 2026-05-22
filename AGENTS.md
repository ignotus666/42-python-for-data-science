# AGENTS.md — 42 Python for Data Science

## Repository structure

Two independent modules, each with standalone `exNN/` exercises. No shared packages between exercises — each directory is self-contained.

- `0_starting/ex00`–`ex09` — Python fundamentals
- `1_array/ex00`–`ex03` — NumPy and image processing

## Running code

```bash
python3 <exercise>/<file>.py          # run a script
python3 <exercise>/tester.py          # run the exercise's test harness
```

No test framework (no pytest). Each `tester.py` imports the module directly and calls its functions. Run from the exercise directory or with the full path.

## Dependencies

No `requirements.txt` or lockfiles. Install manually:

```bash
pip install numpy Pillow tqdm
```

- `1_array/*` — needs `numpy` and `Pillow`
- `0_starting/ex08/Loading.py` and its `tester.py` — needs `tqdm`

## Build / package (ex09 only)

`0_starting/ex09` is a standalone package-building exercise:

```bash
cd 0_starting/ex09
python3 -m build                           # produces dist/ft_package-0.0.1.tar.gz + .whl
python3 -m pip install ./dist/ft_package-0.0.1.tar.gz
python3 -m pip show -v ft_package
```

## Code conventions

- **Error handling**: 42-style — `assert` for validation, `assert False, "message"` for failure, caught via `try`/`except AssertionError`/`except Exception`
- **Entrypoints**: `main()` function guarded by `if __name__ == "__main__":`
- **Style**: Type hints, docstrings, 4-space indent
- **`tester.py`**: Imports the exercise's public function(s) and calls them with sample data, printing results

## Gotchas

- `.gitignore` exists — rebuild it if patterns grow stale.
- `1_array/ex03/zoom.py` has an empty `try` block in `main()` — work in progress; reads from `load_image.py` in the same directory.
- `0_starting/ex03/NULL_not_found.py` uses `type(obj) is type(None)` (not `is None`) to distinguish `None` from `False`/`0` — required by the subject.
- Each `exNN` directory is independent — importing across exercises is not expected.
