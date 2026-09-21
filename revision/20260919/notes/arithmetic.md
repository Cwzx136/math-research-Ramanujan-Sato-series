# Arithmetic rewrite coverage

## Deliverables

- `sections/arithmetic.tex`: intrinsic main text, 470 lines at initial delivery.
- `appendices/arithmetic_details.tex`: supporting arguments, 470 lines at initial delivery.
- `notes/arithmetic_source_check.md`: independent primary-source audit of Tang and Maulik–Poonen.

The original `paper.tex`, `paper.pdf`, and Hint files were not edited.

## Main-text architecture

1. Canonical finite polynomial and de Rham identity line, related by a semilinear Cartier diagram and the conjugate-filtration exact sequence.
2. Tang's theorem with its full geometric, analytic, weighted-density, and limsup hypotheses; naturality under field extension and rational-prime transport.
3. Universal vector extension theorem: a full algebraic Hodge complement has Zariski-dense exponential leaf, yielding the 3/4 lower-density bound. The former separate closure lemma and elliptic corollary are consolidated into the proof and theorem. The proof is by restriction of the universal extension class, not coordinates.
4. Q-curve supersingular density, weighted-density CM forcing, CM eigenline density dichotomy, and unconditional arithmetic classification of the 36 rows. Detailed residual-image counting is in the appendix.
5. One-prime exact Hodge/Frobenius CM criterion. The graph argument is rewritten through polarization, the natural Hodge obstruction, and a Picard/endomorphism specialization diagram; the explicit 2-by-2 matrix is removed. Full Maulik–Poonen hypotheses are retained, including ramification, p-power lifting, and formal GAGA.

## Appendix coverage against original lines 4979–6427

| Original conclusion | Revised location / treatment |
|---|---|
| Rational level-four descent model | `lem:rational-descent`, inside proof of unweighted parameter classification; model, discriminant, j, and Elkies implication retained. |
| Level-four density classification and infinitude | Consolidated in `prop:density` / `prop:infinite-congruences`; four special level-four denominators follow from existing 36-row tables. |
| Finite tests cannot certify CM | Explicit C=256+kM family and nonintegral j retained. |
| Supersingular finite-field projective order | `lem:B-supersingular-frobenius`, full slopes/Hasse proof. |
| Arbitrary non-CM Q-curve rational-prime density | Main theorem plus `rev:qcurve-proof`, full projective construction and O(1/lambda) counting; no degree-one-prime shortcut. |
| Finite Clausen tests for levels 1–3 | Unified with all levels in `prop:levels123-density`; source parameter/j dictionary and geometric-isogeny equivalence retained. |
| Finite Clausen and reflection mod p^2 | `thm:brstt-polynomial-packet`, full source conclusion and reflection upgrade proof. |
| Weighted finite Clausen identity | Main displayed formula and appendix source theorem; derivative proof retained. |
| Normalized Cartier calculation | `rev:cartier-calculation`, exact-differential coefficient extraction, Hasse normalization, Legendre case, and geometric exact-sequence argument retained. |
| Local slope mod p^2 | `prop:local-slope-p2`, invariant etale algebra proof retained. |
| CM slope first-order drift | Source CM assumptions and strict |z|<1 domain retained; equations and p=7 counterexample retained. Auxiliary explicit U_7 polynomial omitted as redundant certificate data. |
| Failure of universal mod p^3 Clausen | 75 x^6 mod 125 counterexample retained. |
| p-adic divergence of original series | `lem:padic-divergence`, digit-block proof retained; numerical four values u_l(1) omitted because finiteness, not their values, is used. |
| Raw truncation is not a unit root | Exact p=5, C=72 example retained. |
| One-prime exact criterion | Main `thm:one-prime-c`; complete conceptual proof. |
| Finite precision cannot suffice | `prop:one-prime-precision-c`, entire E_N family, ordinary trace, non-CM proof, analytic deformation argument retained. |
| Common Galois tensor iff CM | `prop:galois-tensor`, intrinsic End^0 identification plus exact Faltings conclusion; local eigenvalue warning retained. |
| Tang order conventions and elliptic sharpness | `subsec:B-growth-sharp`, full characteristic convention, sigma/zeta upper bound and projection lower bound retained. |
| Difference between exact Hodge preservation and mod-p complement stability | Explicit in main concluding remark; no claimed complex-to-arithmetic transfer. |

## External dependencies and labels

Main references existing section `sec:enumeration`, `sec:standard`, and classification labels `eq:cm-canonical-splitting`, `prop:cm-matrix-certificate`. These labels already appear in the classification rewrite. The standard models and the nonzero Gauss–Manin off-diagonal coefficient are supplied by the period-theory rewrite; formulas are restated intrinsically without a cross-reference that depends on a provisional label.

Citation keys used: `BRSTT`, `Tang`, `Serre`, `Deuring`, `Elkies`, `Faltings`, `MaulikPoonen`. No new bibliography entry is required.

Consolidated aliases preserved: `lem:complement-density-bound` and `lem:B-full-complement-dense` now refer to the general complement theorem, while `cor:weighted-clausen-p2` refers to the unified finite-Clausen theorem. `lem:rational-descent` is now an equation label for the explicit model rather than a separate lemma. No current rewritten section cites these aliases by a incompatible named theorem type.

Old displayed-equation labels deliberately not retained because no revised cross-reference uses them: `eq:finite-clausen-modp`, `eq:noncm-supercongruence`. Their mathematical assertions are retained.

## Source audit

The independent source-check agent read archived Tang and Maulik–Poonen primary texts and confirmed no hypothesis gap. Its exact findings are in `arithmetic_source_check.md`. The arithmetic section distinguishes p-semilinear mod-p Frobenius in the density theorem from the residue-degree linear iterate Phi in the one-prime theorem. It retains every-place rational-prime transport, all complex embeddings, and the upper bad-place density required by Tang.

## Quality scope

No new unconditional CM forcing is asserted. The arithmetic classification has an explicit prime-density hypothesis; the one-prime criterion has an exact Hodge-preservation hypothesis. The complex-to-arithmetic comparison remains unresolved. Numerical examples are exact modular identities from the already audited source, not new experimental evidence.
