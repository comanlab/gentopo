import yaml
from . import visualize
from . import complete
from . import small_world


dispatcher = {
    "complete": complete,
    "small_world": small_world,
}


def generate(study_name, test=False, write=False):
    """
    Generate network topologies from YAML configurations per study.
    """
    graphs = []
    with open(f"studies/{study_name}/config.yml") as file:
        print(f"Opened {study_name} config.yml")

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
                # TODO: Need to add identifiers for each topology?
                build_id = "t00001"
                topology_path = f"studies/{study_name}/{build_id}/topology.png"
                visualize(graph, topology_path)
            else:
                visualize(graph)

            graphs.append(graph)

    return graphs
