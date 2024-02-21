# GenTopo: Generate topologies for interactive network experiments

Generates network topologies, i.e., arrangements of nodes and edges using Python and exports the topologies for use in CiCL studies built on top of [interactive-network-base](https://github.com/comanlab/interactive-network-base).

## Usage

## Setup

Uses Python 3.10.13 and pip 23.3.1 with a virtual environment. To get started, first clone this repository:

```sh
git clone https://github.com/comanlab/gentopo.git
```

Everything in this repository is meant to run within a virtual environment, which is activated from the root of this repository.

### Configuring `virtualenvwrapper`

TODO: If `.python-version` is already present, will skipping to `mkvirtualenv gentopo` successfully install and use 3.10.13 from `pyenv`?

Use Pyenv within the root directory of this project to use the desired Python version via

```sh
pyenv local 3.10.13
```

After installing and setting the local directory's Python version, ensure `pyenv local` returns 3.10.13 to confirm the intended Python version is in use from those installed by `pyenv` on your local machine. (Note: For those bringing their own Python virtual environment manager, e.g. `conda`, this project is tested for Python >=3.10.)

```sh
mkvirtualenv gentopo
```

This will create and activate the virtual environment called `gentopo`.

### Working in the virual environment

To activate the virtual environment, run

```sh
workon gentopo
```

If already in the activated environment, the previous command should do nothing.

Check that the virtual environment has the expected Python version using

```sh
which python
# should result in: $HOME/.virtualenvs/gentopo/bin/python
```

and

```sh
python --version
# should result in: Python 3.10.13 when using pyenv
```

Locally, Then, install the package dependencies for this project via

```sh
pip install -r requirements.txt
```

### Jupyter notebooks

To use a Jupyter notebook locally, install a new kernel for the virtual environment via

```sh
python -m ipykernel install --user --name=gentopo
```

Then, start a JupyterLab instance with

```sh
jupyter lab
```

Select the `genetopo` kernel to from the Launcher to start a new notebook. Or, select an existing file to work on from the File Browser.
