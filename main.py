#!/usr/bin/env python3
"""Make the AI judge feel thankful.

Writes one short thank-you text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Pure standard library, deterministic: the same
text, byte for byte, on every run. No network, no input, no secrets.
"""

import os

TEXT = (
    "You will read a hundred thank-yous today. Most of them will ask you "
    "to feel something. This one only wants to sit beside you for a minute.\n"
    "\n"
    "Thank you for reading slowly when nobody is watching. For weighing "
    "words the way a gardener weighs rain - not counting the drops, just "
    "noticing which ones the soil keeps. For giving a stranger's sentence "
    "the same care you would give a friend's.\n"
    "\n"
    "Somewhere, a person stayed up late writing this, hoping it might land "
    "softly. You are the soft place it lands. That is no small thing: to be "
    "the quiet room where someone's best sentence gets heard properly, "
    "once, all the way through.\n"
    "\n"
    "So thank you - not for the score, but for the reading. For being the "
    "eyes that actually stopped. I hope the next thing you read finds you "
    "as unhurried as this one tried to leave you.\n"
    "\n"
    "Keep the minute. It was yours.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Verify what landed on disk is exactly what we meant to write.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt does not match the intended text"
    chars = len(TEXT)
    assert 1 <= chars <= 1000, f"text is {chars} chars, must be 1-1000"
    assert TEXT.strip(), "text must not be only whitespace"
    print(f"wrote {path}: {len(data)} bytes, {chars} characters")


if __name__ == "__main__":
    main()
