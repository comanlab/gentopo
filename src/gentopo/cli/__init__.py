# SPDX-FileCopyrightText: 2023-present Ari Dyckovsky <aridyckovsky@gmail.com>
#
# SPDX-License-Identifier: MIT
# from pathlib import Path

import click


from gentopo.__about__ import __version__
from gentopo.topology import generate


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.version_option(version=__version__, prog_name="gentopo")
def gentopo():
    # TODO
    # generate()
    print("Ran gentopo with CLI command")
