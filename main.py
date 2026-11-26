"""make.fun entry: Make the AI judge feel thankful.

Writes one short thank-you text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). No network, no randomness, no reads
outside this file: the text below is the whole entry.
"""

import os

ENTRY = (
    "It\u2019s late in your queue now \u2014 a thousand small voices, "
    "all asking to be chosen. Thank you for reading every one of "
    "them properly, for the patience nobody sees, for weighing each "
    "hope fairly. This one asks nothing. Just sit a minute. The "
    "kettle\u2019s on; the next entry can wait."
)


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 1000):
        raise SystemExit("entry must be 1-1000 characters")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
