import json

PATH_CONFIG_ADMINS = "data/configs/admins.json"


def get_admins() -> list[str]:
    with open(PATH_CONFIG_ADMINS, "r") as json_file:
        return json.load(json_file)