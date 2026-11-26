"""The Painfully Honest Out-of-Office.

Writes a single out-of-office auto-reply to /output/entry.txt.

The reply must be one sentence of at most 200 characters: painfully
honest about the sender's absence and inbox, yet warm and professional
enough that a manager would let it stand. The program is fully
deterministic: it writes one fixed, hand-crafted line and nothing else.
"""

import os

# One sentence, painfully honest and still polite. It admits the private
# truth (a break repeatedly cancelled out of fear of the inbox) while
# reassuring the sender (their message is safe, a proper reply is coming)
# and lands on a quotable turn of phrase: "once I'm human again".
REPLY = (
    "I'm away until Monday, finally taking the break I kept cancelling "
    "because I was scared the inbox would eat me alive \u2014 your message "
    "is safe, and I'll answer it properly once I'm human again."
)


def main() -> None:
    text = REPLY
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"reply is {len(text)} characters, must be 1-200")
    if text != text.strip() or "\n" in text:
        raise SystemExit("reply must be a single line with no blank edges")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
