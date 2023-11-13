# generate.py
import yaml
import glob


def main():
    for filename in glob.glob("studies/*/config.yml"):
        print("Running internal")
        with open(filename) as file:
            print(f"Opened {filename}")
            config = yaml.safe_load(file)
            print(config)


if __name__ == "__main__":
    main()
