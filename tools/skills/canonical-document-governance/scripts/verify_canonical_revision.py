#!/usr/bin/env python3
"""Conservative structural checks for canonical Markdown revisions.
A PASS is not proof of semantic equivalence.
"""
import argparse, re
from pathlib import Path

CATEGORIES = {
    "accepted/decisions": r"accepted|frozen|decision",
    "open/unresolved": r"open|unresolved|deliberately open",
    "rejected/corrected": r"rejected|corrected",
    "anti-goals": r"anti[- ]?goals?",
    "fitness": r"fitness",
    "handoff": r"handoff|continuation",
    "glossary": r"glossary|vocabulary",
    "scope/boundary": r"scope|boundary",
}

def headings(s):
    return [x.strip() for x in s.splitlines() if re.match(r"^#{1,6}\\s+\\S", x)]

def norm(h):
    h = re.sub(r"^#{1,6}\\s+", "", h)
    h = re.sub(r"\\bv?\\d+(?:\\.\\d+)+\\b", "<version>", h, flags=re.I)
    return re.sub(r"\\s+", " ", h).strip().lower()

def blocks(s):
    return re.findall(r"```(?:\\w+)?\\n(.*?)```", s, re.S)

ap = argparse.ArgumentParser()
ap.add_argument("old")
ap.add_argument("new")
a = ap.parse_args()
old = Path(a.old).read_text(encoding="utf-8")
new = Path(a.new).read_text(encoding="utf-8")
oh, nh = headings(old), headings(new)
nn = {norm(x) for x in nh}
missing = [x for x in oh if norm(x) not in nn]
ohs, nhs = "\\n".join(oh).lower(), "\\n".join(nh).lower()
lost_categories = [k for k,p in CATEGORIES.items()
                   if re.search(p, ohs, re.I) and not re.search(p, nhs, re.I)]

print("PayCrypto.Me Canonical Revision — Structural Verification")
print("="*60)
print(f"Old characters: {len(old):,}")
print(f"New characters: {len(new):,}")
print(f"Old headings: {len(oh)} | New headings: {len(nh)}")
print(f"Old fenced blocks: {len(blocks(old))} | New fenced blocks: {len(blocks(new))}")
print()
if missing:
    print("WARNING — prior headings not detected:")
    for x in missing: print(" -", x)
else:
    print("PASS — no prior heading loss detected by normalized comparison.")
if lost_categories:
    print("WARNING — prior section categories not detected:", ", ".join(lost_categories))
else:
    print("PASS — key section categories remain detectable.")
if len(blocks(new)) < len(blocks(old)):
    print("WARNING — fenced block count decreased; audit diagrams/examples manually.")
else:
    print("PASS — fenced block count did not decrease.")
print()
print("MANDATORY MANUAL GATES")
for x in [
    "Semantic preservation",
    "New-knowledge coverage",
    "Contradiction resolution",
    "Scope/boundary audit",
    "Diagram semantic audit",
    "Open-question preservation",
    "Rejected/negative-knowledge preservation",
    "Self-sufficient handoff",
]:
    print(" [ ]", x)
print("\\nMechanical PASS does NOT certify canonical completeness.")
