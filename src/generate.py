import yaml
from . import visualize
from . import complete
from . import small_world


dispatcher = {
    "complete": complete,
    "small_world": small_world,
}


def generate(filename, test=False, write=False):
    """
    Generate network topologies from YAML configurations per study.
    """
    graphs = []
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

            params = network["params"]

            if test:
                try:
                    seed = network["test"]["seed"]
                except KeyError:
                    raise ValueError("Invalid input.")
                graph = network_generator(params, seed)
            else:
                graph = network_generator(params)

            if write:
                study_path = filename.split("config.yml")[0]
                visualize(graph, study_path + "topology.png")
            else:
                visualize(graph)

            graphs.append(graph)

    return graphs
