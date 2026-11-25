"""Monday Morning Punchlines entry.

Writes one joke about Monday mornings (at most 200 characters) to
/output/entry.txt, or to the path resolved from ENTRY_OUTPUT /
OUTPUT_DIR / MAKEFUN_OUTPUT_DIR, falling back to a directory next to
this script when /output is not available.
"""

import os

ENTRY_TEXT = (
    "I told Monday I'd call in sick. "
    "Monday said, 'You already did. It's called the weekend.'"
)


def resolve_output_path():
    """Resolve where the entry text goes, honouring the harness env vars."""
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    text = ENTRY_TEXT
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
