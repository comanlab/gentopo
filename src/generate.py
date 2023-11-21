from . import validate_config
from . import visualize
from . import create_topology_dir
from . import write_topology_json
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
    config = validate_config(study_name)
    topology = config["topology"]

    try:
        network_generator = dispatcher[topology["family"]]
    except KeyError:
        raise ValueError(f"{topology['family']} is not a supported family of networks.")

    n = topology["n"]
    params = topology["params"]
    graph = network_generator(n, params)

    if write:
        # TODO: Need to add identifiers for each topology?
        topology_id = create_topology_dir(study_name)
        topology_path = f"studies/{study_name}/{topology_id}"
        visualize(graph, topology_path)
        write_topology_json(study_name, topology_id, graph)
    else:
        visualize(graph)

    return graph
