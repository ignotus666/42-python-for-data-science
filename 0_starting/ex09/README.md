Building and installing the package:

1. Make sure `build` is available in the Python environment you will use for building.
   - `pip install build`

2. Build the package from the project directory.
   - `python3 -m build`

3. Install the generated distribution with `pip`.
   - `pip install ./dist/ft_package-0.0.1.tar.gz`
   - `pip install ./dist/ft_package-0.0.1-py3-none-any.whl`

4. Check the package from the same environment that installed it.
   - `pip list`
   - `pip show -v ft_package`

If your system Python is externally managed, run the install commands inside a virtual environment instead:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install ./dist/ft_package-0.0.1.tar.gz
```

Uninstalling:

 1. Run the commands:
    - `pip uninstall ft_package`
    - `rm -rf dist build *.egg-info`
