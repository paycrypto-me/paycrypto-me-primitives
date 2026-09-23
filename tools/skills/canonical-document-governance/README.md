# PayCrypto.Me Canonical Document Governance

Governance skill for humans and AI agents working on canonical architecture
documents inside public PayCrypto.Me repositories.

The skill treats each public repository's declared domain as its documentary
universe. It preserves all in-scope architectural knowledge while preventing
unnecessary leakage or inference about architecture outside that public scope.

Run the structural helper with:

```bash
python scripts/verify_canonical_revision.py previous.md candidate.md
```

Mechanical checks never replace semantic preservation, new-knowledge,
contradiction, scope-containment, diagram, and handoff review.
