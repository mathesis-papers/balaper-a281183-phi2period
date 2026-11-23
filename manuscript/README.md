# Explicit onsets and residue certificates for Bala's period problem

The note gives an alternative binomial-lifting proof of the period theorem of
Lien-Hung Su, *Quadratic Derivations and Uniform Modular Periods for Six
Inverse-Function Sequences*, version 1, 31 October 2026,
DOI https://doi.org/10.5281/zenodo.23835577, Theorem 3.2 and Corollary 3.3.
The primary posing locator is Peter Bala's 16 February 2026 comment in
OEIS A281183, revision 60 of 6 November 2026. The coefficient recurrence is
credited to Seiichi Manyama in the posing entries.

## Results and coverage

For `D = (1+s^2)^2 d/ds` and every `f` in `Z[[s]]`, let
`b_f(n) = (D^(2n) f)(0)`. For `m >= 3`, the shift `phi(m)^2/2` is a
period modulo `m` for
`n >= N(m) = max(v_2(m), max_{odd p|m} ceil(v_p(m)/2))`.
For `m = 1,2`, shift one works after `N(1)=0`, `N(2)=1`.
Also `2^n` divides `b_f(n)`. The theorem covers all integral formal-series
observables, including positive and negative even powers of `C`.
A281183 uses `f=1+s^2`; A281180 uses `f=(1+s^2)^2` and its OEIS index is
one larger than the column index.

The note proves Bala's tentative polynomial nested-derivative identity and
the asserted secant-square and inverse-square-root derivative formulas, and supplies
dimension-bounded certificates for the seven least residue periods in its
table, as well as the constant residue of A281181 modulo 12. Those results
were previously proved by Su, Propositions 3.4--3.6.
For A281182, interleaving A281181 and A281180 proves an eventual shift
`phi(m)^2` for `m>=3`. Its least eventual period modulo 2 is 2. An all-modulus
totient-square extension was not asserted in that entry and fails at 2.
The coverage table distinguishes these written consequences from the
full-modulus results for A281181, A281184 and A281440 cited from Su.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively use a conventional LaTeX installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is contained in `note.tex`; BibTeX is not required.

## Exact computations

Python 3 and its standard library suffice:

```sh
python3 verify.py > computed-checks.json
cmp computed-checks.json checks.json
```

The checker compares Manyama's recurrence with direct polynomial
differentiation, tests the nested-derivative identity on the recorded finite
range, and compares 64 consecutive period congruences per modulus for each
of A281183 and A281180 for `1 <= m <= 60`. It also tests the integral-series
example `(1+s^2)^(-1)` and parity of the interleaved sequence.
These comparisons support their finite ranges, separately from the written
arbitrary-modulus lifting proof.

`checks.json` additionally gives the small matrix columns, zero-difference
identities and minimality witnesses for all seven residue-period certificates,
and for the five geometric-row identities. The matrices have rank at most 7.
The proof explains why exactly that many consecutive identities propagate
by Cayley--Hamilton; these are finite premises of all-index conclusions,
not extrapolations from numerical agreement.

## Formal declaration coverage

All links use source revision `92de86888730265f84e24d28bdb67546c543a966`.

- `BalaA281183TotientSquarePeriod.result` proves rational-series existence,
  integer factorial-scaled even coefficients of `C^2`, and the eventual shift
  `phi(m)^2` for every positive modulus:
  https://github.com/the-omega-institute/trureturing/blob/92de86888730265f84e24d28bdb67546c543a966/D5/S1/Recurrence/Periodic/BalaA281183TotientSquarePeriod.lean
- `BalaA281180TotientSquarePeriod.result` gives the corresponding formal
  series `S`, integer coefficients `(2n-1)! [x^(2n-1)] S` for `n>=1`, and
  eventual totient-square shift at that OEIS index:
  https://github.com/the-omega-institute/trureturing/blob/92de86888730265f84e24d28bdb67546c543a966/D5/S1/Recurrence/Periodic/BalaA281180TotientSquarePeriod.lean
- `BalaA281181TotientSquarePeriod.result` gives the analogous statement
  for `C`. In the same file, `BalaPolynomialSystem.even_sequence_period`
  covers nonnegative powers of `C` in the flows `H'=C^q`, `q=3` or `7`:
  https://github.com/the-omega-institute/trureturing/blob/92de86888730265f84e24d28bdb67546c543a966/D5/S1/Recurrence/Periodic/BalaA281181TotientSquarePeriod.lean
- `BalaTruncated.prime_power_derivative_period` covers `Delta=P d/ds`
  for integral `P` with `P(0)=1` and integral polynomial observables, with
  derivative-index shift `phi(p^r)^2` modulo `p^r` after index `p^(2r-1)`:
  https://github.com/the-omega-institute/trureturing/blob/92de86888730265f84e24d28bdb67546c543a966/D5/S1/Recurrence/Periodic/AutonomousDerivationTotientSquarePeriod.lean

The half-size shift, explicit onset, formal-series extension, conjugation
identity and interleaving consequence are covered by the note's written
proofs. The small-modulus certificates use exact finite identities and the
written Cayley--Hamilton reduction. General sharp onsets and least periods
outside the listed moduli remain open here.

## Authors and license

1. Haobo Ma — ChronoAI Pte Ltd, Singapore.
2. Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

Copyright 2026 Haobo Ma and Wenlin Zhang. The note and accompanying code are
licensed under Creative Commons Attribution 4.0 International (CC BY 4.0),
https://creativecommons.org/licenses/by/4.0/.
