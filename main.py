"""Thank-you note for the make.fun gratitude judge.

The program assembles one short text from its sentences and writes it
to entry.txt in the output directory. It never touches the network,
never reads anything from disk, and always produces the same bytes.
"""

import os

SENTENCES = [
    "It\u2019s late in your queue now \u2014 a thousand small voices, "
    "all asking to be chosen.",
    "Thank you for reading every one of them properly, for the "
    "patience nobody sees, for weighing each hope fairly.",
    "This one asks nothing.",
    "Just sit a minute.",
    "The kettle\u2019s on; the next entry can wait.",
]

MAX_CHARS = 1000


def build_text():
    return " ".join(SENTENCES)


def check_text(text):
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds 1000 characters")


def output_path():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, "entry.txt")


def main():
    text = build_text()
    check_text(text)
    with open(output_path(), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
