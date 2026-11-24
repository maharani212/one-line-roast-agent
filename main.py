#!/usr/bin/env python3
"""Write one short text to /output/entry.txt for Roast Your Own Agent.

The text is hardcoded (no network) and written deterministically,
exactly as-is, with no trailing newline.
"""

TEXT = 'My agent apologizes so much, it said sorry to the error message, then asked the error message how IT was feeling.'


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
