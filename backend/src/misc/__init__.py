import tomli
from typing import TypedDict, List


class Info(TypedDict):
    version: str
    description: str
    name: str
    authors: List[str]


def get_project_info() -> Info:

    info: Info = {
        "version": '',
        "description": '',
        "name": '',
        'authors': ['']
    }

    with open("pyproject.toml", "rb") as toml_file:
        toml_data = tomli.load(toml_file)
        info['version'] = toml_data["tool"]["poetry"]["version"]
        info['description'] = toml_data["tool"]["poetry"]["description"]
        info['name'] = toml_data["tool"]["poetry"]["name"]
        info['authors'] = toml_data["tool"]["poetry"]["authors"]

    return info
