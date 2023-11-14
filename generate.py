# generate.py
import yaml
import glob
import matplotlib.pyplot as plt
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

                positions = nx.circular_layout(graph)

                plt.figure(figsize=(10, 10))
                topology_visual = nx.draw_networkx(graph, positions)


if __name__ == "__main__":
    main()
