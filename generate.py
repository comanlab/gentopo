# generate.py
import yaml
import glob
from src import visualize
from src import complete
from src import small_world


dispatcher = {
    "complete": complete,
    "small_world": small_world,
}


def main():
    for filename in glob.glob("studies/*/config.yml"):
        with open(filename) as file:
            print(f"Opened {filename}")

            try:
                config = yaml.safe_load(file)
            except yaml.YAMLError as e:
                print(e)

            for network in config["networks"]:
                try:
                    network_generator = dispatcher[network["family"]]
                except KeyError:
                    raise ValueError("Invalid input.")

                print(network["params"])
                graph = network_generator(network["params"])

                study_path = filename.split("config.yml")[0]
                visualize(graph, study_path + "topology.png")


if __name__ == "__main__":
    main()
