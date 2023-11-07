def read_txt(path: str) -> list:
    data = []

    with open(path, 'r') as f:
        for line in f:
            data.append(line.rstrip())

    return data

def write_txt(path: str, data: list) -> None:

    with open(path, 'w') as f:
        for line in data:
            f.write(line)
            f.write('\n')