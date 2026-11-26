"""Funniest One-Line Performance Review — make.fun entry.

Writes the winning one-liner to /output/entry.txt.
The review: a man promoted twice in 18 months lands on a performance
plan for 'visibility', because his best work kept happening in rooms
his boss wasn't in. Real review machinery — promotions, PIPs, the
visibility criterion — followed one step into absurdity.

Why this line won the draft round: it is the only candidate where the
punishment is caused by the achievement itself. The promotions prove
the work is excellent; the plan proves nobody with power saw it. The
specific span (twice, 18 months) keeps it a scene, not a slogan, and
the punch waits for the final clause.
"""

import os

ENTRY = "Promoted twice in 18 months, then put on a performance plan for 'visibility': his best work kept happening in rooms his boss wasn't in."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
