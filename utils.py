# Read the yaml file to get paths
import os
import yaml
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError

def read_yaml(path_to_yaml_file: Path)-> ConfigBox:
    """reads a yaml file.

    Args:
        path_to_yaml_file (str): path-like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml_file, 'r') as file:
            data = yaml.safe_load(file)
            print(f"yaml file: {path_to_yaml_file} loaded successfully")
    except BoxValueError:
        raise ValueError("Yaml File is empty")
    except Exception as e:
        raise e
     
    return ConfigBox(data)

# Create neccessary directory(ies)
def create_directories(directory_names: list, verbose = True ):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in directory_names:
        os.makedirs(path, exist_ok = True)
        if verbose:
            print(f"created directory at {path}")
