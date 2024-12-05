def parse_date(day: int) -> list[str]:
    file = f"input_day_{day}.txt"
    with open(file, 'r') as f:
        content = f.read()
    return content.split('\n')