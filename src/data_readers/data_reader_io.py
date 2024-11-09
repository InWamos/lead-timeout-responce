import json
from datetime import datetime
import os


def is_timespan_long_enough(client_id: int, receiver_id: int) -> bool:
    memory = read_memory(client_id)
    receiver_id_str = str(receiver_id)

    if receiver_id_str not in memory.keys():
        return True
    else:
        time_now = datetime.now()
        date_last_schedule = datetime.fromisoformat(memory[receiver_id_str]["last_schedule"])  # type: ignore
        time_passed = time_now - date_last_schedule

        if time_passed.days >= 1:
            return True
        else:
            return False


def add_client(client_id: int, receiver_id: int, custom_datetime_isoformat: str | None = None) -> None:
    memory = read_memory(client_id)
    receiver = str(receiver_id)
    if receiver in memory:
        memory[receiver]["last_schedule"] = datetime.now().isoformat()
    else:
        datetimeiso = custom_datetime_isoformat if custom_datetime_isoformat else datetime.now().isoformat()
        memory[receiver] = {"last_schedule": datetimeiso}

    with open(
        get_path_to_memory_file(client_id), mode="w", encoding="utf-8"
    ) as received_json:
        json.dump(memory, received_json)


def read_memory(client_id: int) -> dict[str, dict[str, str]]:
    path_to_memory = get_path_to_memory_file(client_id)

    if not os.path.exists(path_to_memory):
        with open(path_to_memory, "w", encoding="utf-8") as received_json:
            json.dump({}, received_json)
        return {}

    else:
        with open(path_to_memory, "r", encoding="utf-8") as received_json:
            memory = json.load(received_json)
            return memory


def get_path_to_memory_file(client_id: int) -> str:
    return f"data/stats/{client_id}.json"
