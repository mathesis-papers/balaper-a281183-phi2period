# Explicit onsets and residue certificates for Bala's totient-square period problem after Su

**Authors:** Haobo Ma, Wenlin Zhang

For Peter Bala's conjecture in the comment of 16 February 2026 in OEIS A281183, revision 60 of 6 November 2026, we give explicit onsets and an alternative lifting proof of Lien-Hung Su's period theorem of 31 October 2026, Theorem 3.2 and Corollary 3.3 of Quadratic Derivations and Uniform Modular Periods for Six Inverse-Function Sequences, DOI 10.5281/zenodo.23835577. If a_n=(2n)![x^(2n)]C(x)^2, where C=cosh(integral_0^x C(t)^3 dt), then a_n is integral and has an eventual period dividing phi(m)^2 for every positive modulus m. For m>=3, phi(m)^2/2 is a period after N(m)=max(v_2(m), max_{odd p|m} ceil(v_p(m)/2)). A binomial operator lift proves this for every integral formal-series observable of S'=(1+S^2)^2. The note proves companion and interleaving consequences and gives dimension-bounded certificates for seven residue periods and the mod-12 identity, crediting Su's prior proofs. Written proofs, finite coefficient comparisons and formal declaration coverage are distinguished.

- PDF: [frozen public file](paper.pdf)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [balaper-a281183-phi2period](https://mathesis-omega-research.apps.chrono-ai.fun/papers/balaper-a281183-phi2period?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Explicit onsets and residue certificates for Bala's totient-square period problem after Su. Mathesis, version 2. https://mathesis-omega-research.apps.chrono-ai.fun/papers/balaper-a281183-phi2period?version=2

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/92de86888730265f84e24d28bdb67546c543a966/D5/S1/Recurrence/Periodic/BalaA281183TotientSquarePeriod.lean) | No public receipt |
| Lemma (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/92de86888730265f84e24d28bdb67546c543a966/D5/S1/Recurrence/Periodic/BalaA281183TotientSquarePeriod.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/92de86888730265f84e24d28bdb67546c543a966/D5/S1/Recurrence/Periodic/BalaA281183TotientSquarePeriod.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/92de86888730265f84e24d28bdb67546c543a966/D5/S1/Recurrence/Periodic/BalaA281183TotientSquarePeriod.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/92de86888730265f84e24d28bdb67546c543a966/D5/S1/Recurrence/Periodic/BalaA281183TotientSquarePeriod.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/92de86888730265f84e24d28bdb67546c543a966/D5/S1/Recurrence/Periodic/BalaA281183TotientSquarePeriod.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).
