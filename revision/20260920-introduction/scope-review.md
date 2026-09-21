# Introduction scope review

Date: 2026-09-20

Result: **PASS**. The expanded introduction accurately distinguishes the conditional converse from the unconditional results in the main text. No mathematical correction is required. One wording refinement is recommended below.

Reviewed `revision/20260919/sections/introduction.tex` against the complete sections `02_periods.tex`, `comparison.tex`, `classification.tex`, `arithmetic.tex`, and `scarcity.tex`. The introduction hash at review was `40EDE35B12933A0F437B6002D9438E32A833276779051013F65E6FEA01C753D6`.

## Preservation check

The entire pre-existing formal block, from the hypergeometric definition through the explanation following the unconditional uniqueness theorem, is identical to `before/introduction.tex` after normalizing Windows line endings and trailing whitespace. Both versions contain 4,041 characters in this block. Thus the definition, quadratic-period independence hypothesis, classification theorem, its proof, the unconditional uniqueness theorem, and their labels/formulas have not changed.

## Scope checks

- **Conditional versus unconditional:** the unrestricted classification explicitly assumes quadratic-period independence. Uniqueness, nonvanishing, CM existence, rational descent, CM enumeration, arithmetic tests, and scarcity are correctly identified as unconditional.
- **Primitive coefficients and branches:** the unchanged definition uses `gcd(A,B)=1`, the standard germ, and ordinary convergence. The introductory discussion does not broaden these conventions.
- **Unique slope:** the identity-line theorem proves at most one algebraic projective coefficient direction at every admissible algebraic fiber. The introduction does not claim existence away from CM.
- **36 and 35:** the CM classification gives 36 primitive standard classes; Euler transport retains precisely the 35 interior classes because no nonzero companion pair converges at either endpoint.
- **Finite degree:** for the rational denominator problem, the correspondence degrees are `(1,2,2,1)`, so the elliptic invariant has degree at most one or two. The asserted reduction through CM reciprocity and class-number bounds matches the proof. It is understood in the stated rational-parameter setting.
- **Canonical CM line:** the period section identifies the unique identity line with the complementary CM eigenline; the classification section proves rational descent using the involution and isogeny covariance. The introduction describes these mechanisms accurately.
- **Comparison tensors:** the scalar relation supplies only part of a complete comparison tensor. The introduction preserves the distinction and does not infer an endomorphism from one scalar coordinate.
- **Weighted prime criterion:** the relevant threshold is lower natural density strictly greater than `3/4` for weighted zeros at rational primes. The arithmetic classification proves that this selects exactly the standard rows on the stated convergence domain. The introduction keeps this hypothesis separate from the complex identity.
- **One-prime criterion:** the introductory statement specifies good ordinary reduction and exact preservation of the Hodge line by the residue-field power of crystalline Frobenius. This agrees with the theorem, including its distinction from modulo-prime stability of a complementary line.
- **Separation:** bounded degree is imposed on the squared multiplier `alpha^2`; gaps tend to infinity jointly across the four levels and both signs. No coefficient-height bound is silently added.
- **Counting:** the subpower assertion is explicitly limited to complete arithmetic height windows and compact parameter intervals. It is not advertised as finiteness, unrestricted counting by denominator, or a pointwise CM theorem.
- **Organization:** the section references match the actual order and subject matter. The appendix description correctly locates models, certificates, tables, arithmetic detail, refinements, further settings, and limitations.

## Recommended wording refinement

The sentence “Quadratic-period independence expresses precisely the numerical exclusion needed for the original families” could be read as claiming necessity for the integer-coefficient classification. The period section correctly observes that excluding every algebraic coefficient direction is stronger than excluding rational directions alone. A precise replacement is:

> Quadratic-period independence excludes all algebraic coefficient identities on the specified non-CM fibers.

This is a refinement of introductory wording; the unchanged formal statements already have the correct sufficient-hypothesis scope.

## Review limits

This review checks consistency with the already audited proofs. It does not repeat the prior complete proof audit or independently reverify the historical claims against every cited publication.

## Final wording confirmation

The two revised statements have been inspected in the current source: “The quadratic-period independence sufficient for the CM converse is stronger than the particular consequences of these theorems used here” and “Quadratic-period independence gives an explicit numerical exclusion sufficient for the original families.” Both accurately state sufficiency and resolve the precision recommendation above. **Final scope verdict: PASS, with no outstanding recommendation.**

Current introduction SHA256: `619A1F0D47BDE2A1111FFC27F6C59CA35CF156DBA2A4B4FE13E689F4CC5E6B39`.
