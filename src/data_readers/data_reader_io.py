import json
from datetime import datetime
import os


def is_timespan_long_enough(client_id: int, receiver_id: int) -> bool:
    memory = read_memory(client_id)
    receiver = memory.get(receiver_id)

    if not receiver:
        return True
    else:
        time_now = datetime.now()
        date_last_schedule = datetime.fromisoformat(receiver.get("last_schedule"))  # type: ignore
        time_passed = time_now - date_last_schedule

        if time_passed.days >= 1:
            return True
        else:
            return False


def add_client(client_id: int, receiver_id: int) -> None:
    memory = read_memory(client_id)
    memory[receiver_id] = {"last_schedule": datetime.now().isoformat()}

    with open(
        get_path_to_memory_file(client_id), mode="w", encoding="utf-8"
    ) as received_json:
        json.dump(memory, received_json)


def read_memory(client_id: int) -> dict[int, dict[str, str]]:
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
