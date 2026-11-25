"""One-Line Office Joke Laugh-Off entry.

Chosen line (74 characters, gate 1-200):
    "I asked IT for help and they sent me a ticket, so now I have two problems."

Decision record
---------------
Candidates weighed against the judge's brief (one-line office joke first;
sharp surprising punchline; clear on one read; fresh; tight):

A. "Our office printer only works when nobody needs it, which HR calls
   'work-life balance'."
   Loses: the punchline is a label pasted onto the observation, not a twist.
   "Work-life balance" is a worn phrase, and the joke is a mild observation
   about a printer rather than a moment with a person in it.

B. "The office plant died, so we held a meeting about it, and now the
   meeting is also dying."
   Loses: two beats and a setup that has to be carried across the line. The
   second half explains the first instead of surprising it, and "meeting
   about a meeting" is one of the most written office jokes there is.

C. "I asked IT for help and they sent me a ticket, so now I have two
   problems."
   CHOSEN. A real office moment everyone recognises: asking IT for help and
   getting a ticket number instead of help. The punchline turns on the word
   "ticket" doing double duty -- it is both the help-desk artefact and a
   second problem of its own. The twist lands on the last two words, the
   line needs no setup, and it is not a reply-all / "per my last email" /
   meeting-could-have-been-an-email cliche.

D. "My calendar is so full I have a meeting to discuss why I have no time
   for meetings."
   Loses: the "meeting about meetings" shape is exhausted, and the line
   states its own joke twice ("so full" and "no time") instead of letting
   the punchline do the work.

Writing passes on the winner
----------------------------
Pass 1: the first draft read "I asked IT for help and they gave me a
ticket, so now I have two problems." "Gave" was changed to "sent": a
ticket is sent/issued, so "sent me a ticket" is the voice IT actually
uses, and it tightens the rhythm of the middle clause.

Pass 2: an ending "and neither one is fixed" was tried and dropped. It
explains the joke the line has already made -- the reader already knows
neither problem is solved -- and ending on "two problems" lets the twist
land instead of trailing off into commentary.
"""

import os

ENTRY = "I asked IT for help and they sent me a ticket, so now I have two problems."

MAX_CHARS = 200


def check_gate(text):
    """Mirror the sealed gate: 1-200 UTF-8 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.rstrip("\n") or "\r" in text:
        raise ValueError("entry must be a single line")


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(ENTRY)
    path = entry_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
