# main.py
import glob
import argparse
from src import generate


def main(**kwargs):
    for filename in glob.glob("studies/*/config.yml"):
        generate(filename, **kwargs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test",
        action="store_true",
        help="sets random seed for testing generated networks",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="writes the generated network data to study directories",
    )
    args = parser.parse_args()

    main(**vars(args))
