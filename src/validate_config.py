import yaml
from jsonschema import validate


schema = {
    "type": "object",
    "properties": {
        "project": {"type": "string"},
        "topology": {
            "type": "object",
            "properties": {
                "family": {
                    "default": "complete",
                    "enum": ["complete", "random", "small_world", "lattice"],
                },
            },
            "allOf": [
                {
                    "if": {
                        "properties": {
                            "family": {"const": "small_world"},
                        },
                    },
                    "then": {
                        "properties": {
                            "omega_range": {
                                "type": "array",
                                "items": {"type": "number"},
                            },
                        },
                    },
                },
            ],
        },
        "interactions": {"type": "object"},
    },
}


def validate_config(study_name):
    """
    Validate a config.yml for a given study_name.

    Returns config in dict format if no error
    """
    with open(f"studies/{study_name}/config.yml") as file:
        print(f"Opened {study_name} config.yml")

        try:
            config = yaml.safe_load(file)
            validate(instance=config, schema=schema)
            return config
        except yaml.YAMLError as e:
            print(e)
