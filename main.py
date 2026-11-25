# Entry concept: the weirdest job titles are the ones that sound grand and
# vaguely corporate while describing a job everyone actually recognises.
# "Executive Director" borrows boardroom authority, but the portfolio is
# "Other People's Emergencies" -- the friend, parent, or coworker who gets
# the 2 a.m. phone call whenever something breaks. The joke is the gap
# between the inflated title and the unpaid, always-on-call reality, and the
# apostrophe in "People's" keeps it feeling like a real line on a real
# business card.
import os

ENTRY = "Executive Director of Other People's Emergencies"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
