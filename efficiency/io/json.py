import json


def read_json(path: str) -> dict:
    with open(path, "r") as f:
        data = json.load(f)
    return data


def write_json(path: str, data: dict, indent: int = 4) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=indent)


def read_jsonl(path: str) -> list:
    data = []

    with open(path, "r") as f:
        for line in f:
            data.append(json.loads(line))

    return data


def write_jsonl(path: str, data: list, indent: int = 4) -> None:
    with open(path, "w") as f:
        for line in data:
            json.dump(line, f, indent=indent)
            f.write("\n")
