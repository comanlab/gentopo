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

TODO.

```sh
mkvirtualenv gentopo
```

This will create and activate the virtual environment called `gentopo`.

### Working in the virual environment

To activate the virtual environment, run

```sh
workon gentopo
```

If already in the activated environment, the previous command should do nothing. Then, install the package dependencies for this project via

```sh
pip install -r requirements.txt
```
