import json
import gzip
from pathlib import Path


def load_candidates(path):
    """
    Load candidate data from a JSON, JSONL, or JSONL.GZ file.

    Returns:
        list: A list of candidate dictionaries.
    """

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix == ".json":
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    elif path.suffix == ".jsonl":
        candidates = []

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    candidates.append(json.loads(line))

        return candidates

    elif path.suffix == ".gz":
        candidates = []

        with gzip.open(path, "rt", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    candidates.append(json.loads(line))

        return candidates

    else:
        raise ValueError(f"Unsupported file format: {path}")