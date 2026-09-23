---
name: paycrypto-canonical-doc-governance
description: Safely create, revise, review, consolidate, and supersede PayCrypto.Me canonical architecture documents without silent semantic loss. Use for domain canonicals such as Primitives, Core, SDK, Consumers, or platform architecture.
---

# PayCrypto.Me Canonical Document Governance

## Purpose

Use this skill whenever a PayCrypto.Me canonical architecture document is created or revised.

A canonical is an architectural source of truth, not ordinary prose and not merely documentation of current code. It preserves accepted decisions, invariants, boundaries, rationale, vocabulary, meaningful diagrams, rejected/corrected approaches, anti-goals, unresolved questions, fitness tests, continuation instructions, contribution conventions, and contextual relationships needed to understand the governed domain.

> **A revision may improve, clarify, reorganize, correct, or supersede the canonical, but architectural knowledge must never disappear silently.**

Canonical evolution is **replacement-based, not composition-based**. The newest accepted version must be self-sufficient and supersede the previous current version. Git/history may retain old versions, but readers must not need multiple historical canonicals to reconstruct the current architecture.

---

# 1. Governing invariants

## 1.1 No silent loss

Never remove a still-valid accepted decision, invariant, rationale, rejected alternative, open question, boundary, convention, fitness test, diagram meaning, or continuation requirement merely to shorten, polish, reorganize, or clean up a canonical.

**Absence is not a migration mechanism.**

If a statement is no longer correct, supersede it explicitly:

```text
previous decision
      |
      v
new evidence / requirement / correction
      |
      v
superseding decision
      |
      +-- what changed
      +-- why
      +-- what remains valid
      `-- impact/migration if relevant
```

## 1.2 Latest canonical is self-sufficient

Do not require a reader to consult v1.1 to understand v1.2. Carry forward all still-relevant rationale and knowledge.

Historical versions explain chronology; they must not be dependencies of the current source of truth.

## 1.3 Domain scope is explicit

Every canonical must say which domain it governs.

Neighboring domains may be referenced only where needed to clarify boundaries, dependency direction, incoming requirements, outgoing responsibilities, product constraints, or integration assumptions.

Use a scope note near the beginning. Example:

> Core, SDK and Consumers are referenced only where their relationship with this domain is necessary to establish boundaries, dependency direction, requirements, constraints, or responsibilities. Their internal architecture belongs to their own canonical documents.

Do not accidentally freeze another domain's internals through a contextual reference.

## 1.4 Canonical decisions are stronger than code shape

Source code shows what exists. The canonical explains **why it exists in that form and how it may legitimately evolve**.

Humans and coding agents must not infer extension rules solely by copying existing classes, folders, or patterns when the canonical establishes semantic rules.

## 1.5 Precision over compression

Canonical documents may be long. Optimize in this order:

1. correctness;
2. completeness;
3. unambiguous scope;
4. preservation of reasoning;
5. future recoverability;
6. safe continuation without the original conversation;
7. readability.

Remove duplication only when no meaning, nuance, exception, rationale, or historical correction is lost.

---

# 2. Information classes

Classify material before editing.

## Accepted / frozen
An adopted architectural baseline. Preserve unless explicitly superseded.

## Context
Information about adjacent domains or product constraints needed to explain this domain. Context must not silently become normative internal design for another domain.

## Evidence
Observed behavior from current code, tests, standards, experiments, or production constraints. Evidence motivates architecture but is not automatically architecture.

> **Existing code is evidence of required behavior, not authority over new architecture.**

## Proposal / candidate
An option under consideration. Never silently promote it to accepted status.

## Open / unresolved
A deliberately undecided matter. Preserve until resolved.

## Rejected / corrected
A path intentionally rejected or corrected. Preserve it when forgetting it could cause a future contributor to repeat the mistake.

---

# 3. Mandatory revision workflow

## Phase A — Establish the baseline

Before rewriting:

1. identify the exact current canonical;
2. read the complete document;
3. record version and governed domain;
4. inventory headings;
5. inventory accepted decisions and invariants;
6. inventory open questions;
7. inventory rejected/corrected approaches and anti-goals;
8. inventory fitness tests and handoff instructions;
9. identify contextual references to neighboring domains;
10. identify diagrams whose topology carries architectural meaning.

Do not revise from snippets when the complete canonical is available.

## Phase B — Classify every requested change

Use:

```text
ADD        new architectural knowledge
CLARIFY    same decision, more precise expression
REFINE     better/narrower model preserving intent
CORRECT    prior statement was wrong or misleading
SUPERSEDE  accepted decision intentionally replaced
REORGANIZE documentary/structural change
REMOVE     truly obsolete or provably redundant material
```

`REMOVE` receives the highest scrutiny. Before removing anything ask:

- Is its information fully preserved elsewhere?
- Does it contain unique rationale?
- Is it the only record of a rejected approach?
- Is it an unresolved question?
- Could its absence permit a known mistake?
- Does it constrain implementation despite looking repetitive?
- Is it needed to understand a boundary?

If uncertain, preserve it.

## Phase C — Additive first, consolidate second

For substantial changes, first copy the current canonical and add/refine knowledge without destructive rewriting.

Only after the new knowledge is represented should you consolidate wording or deduplicate.

This is the preferred safety strategy:

```text
current canonical
      |
      v
exact working copy
      |
      +-- preserve existing content
      +-- add new accepted knowledge
      +-- mark contradictions/supersessions
      +-- reorganize if useful
      +-- deduplicate only with semantic proof
      |
      v
candidate
```

## Phase D — Resolve contradictions explicitly

Never append a new rule while leaving an incompatible old normative rule appearing equally valid.

Record, when useful:

```text
Old position:
New position:
Reason for change:
What remains valid:
Impact:
```

Then make the normative text unambiguous.

## Phase E — Scope audit

Ask:

- Is this still a canonical for the intended domain?
- Did contextual material become accidental internal design for another domain?
- Did a weak reference become a strong contract without evidence?
- Did we lose context necessary to understand this domain?
- Does the title accurately identify the governed scope?

## Phase F — Structural preservation gate

Compare at minimum:

- headings;
- accepted/frozen decisions;
- open/unresolved decisions;
- rejected/corrected approaches;
- anti-goals;
- fitness tests;
- handoff/continuation instructions;
- glossary/vocabulary;
- diagrams;
- scope/boundary notes.

Mechanical checks are evidence, not proof.

## Phase G — Semantic preservation gate

Ask:

> **Could a reader using only the candidate make a materially different architectural decision because something from the previous canonical silently disappeared?**

If yes, FAIL.

## Phase H — New-knowledge gate

Verify every newly accepted conclusion that motivated the revision appears in the candidate.

Preserving the past perfectly while omitting the new decision is still a failed revision.

## Phase I — Contradiction gate

Search the entire candidate for stale wording that conflicts with the new decision.

If old text is retained for history, label it historical/superseded.

## Phase J — Diagram semantic gate

Diagrams are semantic artifacts, not decoration. Compare:

- nodes;
- relationships;
- directionality;
- boundaries;
- labels;
- visual hierarchy.

Check whether a diagram accidentally implies inheritance, ownership, dependency, or hierarchy that prose rejects.

## Phase K — Handoff test

Pretend the conversation, memories, authors, and previous canonical versions disappeared.

Ask:

> **Can a competent engineer or AI agent continue this domain safely using only this canonical and the concrete sources it explicitly references?**

If not, FAIL.

## Phase L — Superseding release

The candidate must state:

- its version;
- what prior current canonical it supersedes;
- principal additions/clarifications/corrections;
- deliberately unresolved matters where relevant;
- a preservation statement.

Only promote after every gate passes.

---

# 4. Preservation report

Every substantial revision should produce a report such as:

```text
Baseline: canonical vX.Y
Candidate: canonical vX.Z

Structural preservation:
  prior headings: N/N retained or explicitly superseded
  accepted decisions: checked
  open decisions: checked
  rejected approaches: checked
  anti-goals: checked
  fitness tests: checked
  handoff: checked
  diagrams: checked

Semantic preservation: PASS / FAIL
New-knowledge coverage: PASS / FAIL
Contradiction audit: PASS / FAIL
Scope audit: PASS / FAIL
Diagram audit: PASS / FAIL
Self-sufficient handoff: PASS / FAIL
```

Never equate `N/N headings retained` with semantic equivalence.

---

# 5. Mechanical verification

When Markdown files are available, run:

```bash
python scripts/verify_canonical_revision.py OLD.md NEW.md
```

The bundled checker reports structural preservation signals.

A successful result means only:

> **No obvious structural loss was detected by these checks.**

It never means:

> **The revision is guaranteed complete.**

Semantic review remains mandatory.

---

# 6. Revision record

Every superseding canonical should contain a concise revision record:

```markdown
# Revision record

This revision supersedes vX.Y.

## Added
- ...

## Clarified
- ...

## Corrected / superseded
- ...

## Still deliberately open
- ...

## Preservation statement
All still-valid decisions, invariants, rationale, rejected alternatives,
open questions, fitness tests, and handoff requirements from vX.Y were
carried forward or explicitly superseded.
```

The revision record does not replace updates to normative sections.

---

# 7. Terminology governance

When renaming a concept:

- determine whether the change is editorial or architectural;
- update glossary, diagrams, examples, and normative prose;
- search for stale terminology;
- record aliases/migration wording when useful;
- avoid leaving two names that appear to denote distinct concepts.

Do not normalize vocabulary owned by neighboring domains unless this canonical actually governs it.

---

# 8. Evidence and external facts

Keep these distinct:

```text
ARCHITECTURAL DECISION
  what PayCrypto.Me chooses

OBSERVED EVIDENCE
  what current code/system does

EXTERNAL FACT
  what a standard/library/runtime specifies

OPEN ASSUMPTION
  what still requires verification
```

Do not turn a temporary property of an external dependency into a permanent invariant.

When an external fact may have changed, verify it before using it to revise the canonical.

---

# 9. Open-source contribution safety

For open-source domains, the canonical must make extension rules discoverable without private history.

A contributor should be able to determine:

- what justifies a new abstraction;
- what does not;
- where behavior belongs;
- which boundaries must not leak;
- which dependencies are acceptable;
- what evidence/tests are required;
- which approaches were intentionally rejected;
- how an architectural change should update the canonical.

If code changes an architectural invariant, the canonical must be updated or the architectural change must be explicitly proposed. Code drift must never silently redefine architecture.

---

# 10. AI-agent rules

When an AI agent modifies a canonical:

1. Never summarize away prior architectural content merely for concision.
2. Never assume "cleaner" is better when cleanup removes rationale.
3. Never replace concrete decisions with generic best practices.
4. Never invent missing decisions to make a document look complete.
5. Never silently reconcile contradictions.
6. Never treat current code structure as stronger than an explicit canonical invariant.
7. Never promote a proposal/open idea without evidence of acceptance.
8. Never erase negative knowledge that prevents predictable regressions.
9. Never broaden another domain's architecture because it is mentioned for context.
10. Never claim preservation from a mechanical diff alone.
11. Always preserve uncertainty honestly.
12. Always leave the newest canonical self-sufficient.

---

# 11. Canonical quality tests

## Loss test
What knowledge in the prior canonical can no longer be recovered? Expected: none, except explicitly superseded material with rationale.

## Stranger test
Can a competent engineer unfamiliar with the history understand the architecture and its reasons?

## Agent-imitation test
Could an agent copy visible code patterns and violate an invariant because the canonical failed to explain the extension rule?

## Neighbor-domain test
Could a reader think this canonical governs internals of an adjacent domain mentioned only as context?

## Archaeology test
Does understanding an important decision require old chats, memories, or superseded versions?

## Contradiction test
Are there normative statements that cannot both be true?

## Implementation-independence test
Did evidence from a current library/framework accidentally become an architectural dependency?

## Open-question test
Were unresolved questions preserved rather than accidentally answered or deleted?

## Negative-knowledge test
Were rejected approaches and anti-goals retained so known mistakes are not repeated?

## Revision-motivation test
Can a reader identify what genuinely changed in this version and why?

## Source-of-truth test
Would two current documents need to be composed to recover the architecture? If yes, FAIL.

---

# 12. Definition of done

A canonical revision is complete only when:

- domain and scope are explicit;
- every still-valid prior decision is present;
- necessary rationale is present;
- rejected/corrected approaches worth remembering are present;
- unresolved questions remain visible;
- all newly accepted knowledge is represented;
- superseded decisions are explicit;
- contradictions are resolved;
- diagrams and prose agree;
- neighboring domains remain contextual unless in scope;
- terminology is coherent;
- the document is self-sufficient;
- mechanical checks were run where possible;
- semantic preservation was reviewed;
- a revision record is present;
- the new version explicitly supersedes the prior current version.

If any item fails, do not promote the candidate to canonical.

---

# 13. Governing maxims

> **A canonical document may evolve aggressively, but architectural knowledge must never disappear accidentally.**

> **The newest canonical must contain everything a future contributor needs to preserve the architecture without needing the people, chats, memories, or previous canonical versions that created it.**
