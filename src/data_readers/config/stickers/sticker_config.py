import json


PATH_CONFIG_STICKERS = "data/configs/stickers.json"


def remove_sticker(key: str) -> None:
    sticker_config = get_sticker_config()
    if key in sticker_config["stickers"].keys():  # type: ignore
        del sticker_config["stickers"][key]  # type: ignore
        set_sticker_config(sticker_config)


def add_sticker(key: str, value: str) -> None:
    sticker_config = get_sticker_config()
    sticker_config["stickers"][key] = value  # type: ignore

    set_sticker_config(sticker_config)


def set_main_sticker(sticker_key: str) -> None:
    sticker_config = get_sticker_config()

    if sticker_key in sticker_config["stickers"]:
        sticker_config["chosen_sticker"] = sticker_key
        set_sticker_config(sticker_config)
    else:
        raise ValueError("No such sticker in memory")


def get_main_sticker() -> str:
    sticker_config = get_sticker_config()
    chosen_sticker = sticker_config["chosen_sticker"]
    if isinstance(chosen_sticker, str):
        return chosen_sticker
    else:
        raise ValueError("Main sticker isn't set")


def get_sticker_config() -> dict[str, dict[str, str] | str]:
    with open(PATH_CONFIG_STICKERS, "r") as json_file:
        return json.load(json_file)


def set_sticker_config(sticker_dict: dict[str, dict[str, str] | str]) -> None:
    with open(PATH_CONFIG_STICKERS, "w") as json_file:
        json.dump(sticker_dict, json_file)
