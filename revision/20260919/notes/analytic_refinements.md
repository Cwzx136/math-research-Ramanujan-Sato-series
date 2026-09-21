# Analytic-refinements appendix rewrite

File: `appendices/analytic_refinements.tex`.

The appendix is now organized by three geometric/arithmetic restrictions (cusp lattice, algebraic curves, isogeny classes) and one differential-incidence calculation. The original manuscript was not changed.

## Conceptual changes

- Combined the two independent cusp proofs: polynomial avoidance is the general lattice-separation theorem, and the small-coefficient theorem is its corollary. Both original result labels remain.
- Stated Northcott's exact finiteness conclusion at its use. Retained the precise Zeilberger--Zudilin irrationality-measure bound and the reason a uniform rational lower bound follows.
- Replaced the repeated expanded quadratic contact calculations by the projective coordinate `r=G/F` and the degree-two differential operator `D_{A,B}`. All three original transversality/contact conclusions follow from degree and the field equality supplied by value independence.
- Kept the algebraic-curve theorem in its full original scope, including arbitrary algebraic `s`, possibly transcendental real points, the positive endpoint via its quadratic local cover, and coefficient comparison at the algebraic cusp.
- Recast fixed-isogeny-class finiteness as an equivariant injection of finite Galois sets. The Serre open-image input and the absence of an isogeny-descent assumption are explicit.
- Preserved the rounding and Zariski-density counterexamples, with their exact scope (neither claims a new inverse-pi identity).

## Coverage

Preserved labels/results: `prop:polynomial-avoidance`, `prop:cusp-finiteness`, `prop:growing-rational-height`, `lem:logderivative-nonalgebraic`, `thm:curve-finiteness`, `prop:C-slope-transverse`, `prop:C-varying-transverse`, `cor:C-derivative-independent`, `thm:fixed-isogeny-degree-finiteness`, plus fixed standard-isogeny-class corollary. All original equation labels used in this appendix remain.

No new mathematical claim beyond the original theorem package is introduced. The standard-isogeny-class corollary now explicitly says "smooth fiber", making its implicit domain precise. Independent audit by delegated checker `audit_analytic_theorems` passed the final source SHA256 `FDC9D83023AA7F946E1E49E92B942DFD04549B272226EB7C7293F9F0DDBA15FF`; see `audits/analytic_refinements_mathematics.md`. Its optional presentation suggestions (cusp consolidation and nonintegrality explanation) are incorporated.


Static verification: 394 source lines; all theorem/proof/display environments balanced. Root build/reference/visual QA remains responsible for complete manuscript compilation.
