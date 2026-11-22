from pathlib import Path

ENTRY_TEXT = (
    "A brass desk lamp stays lit beside a dark, sleeping screen. "
    "Rain leans softly against the warm glass, and a wool blanket "
    "rests over the chair back. Nothing is waiting for an answer here. "
    "The room holds the quiet like a cupped pair of hands."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the deterministic entry text to /output/entry.txt."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
