from pathlib import Path


def get_resource(name: str) -> Path:
    return Path("bot", "resources", name)
